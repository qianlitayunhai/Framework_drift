#-*- coding: utf-8 -*-
'''
Created on 2 de mar de 2017

@author: gusta
'''

from xlwt import Workbook
import xlrd
from xlutils.copy import copy
from geradores_tabela.Tabela_excel import Tabela_excel
import numpy as np
from experimentos.Constantes import Constantes
from teste_estatistico.Nemenyi import NemenyiTestPostHoc

c = Constantes('dentro')
pasta = c.pasta
caminho_bases = c.caminho_bases + pasta

class Tabela_testes():
    def __init__(self):
        self.wb = Workbook()
        self.nome = ""
    
    def Gerar_tabela_final(self):
        '''
        metodo para agrupar os resultados que estavam em subpastas e salvar em um arquivo final
        '''
        
        caminho = c.caminho_bases + c.pasta
        tabela_final = "Resultados.xls"
        caminho_tabfinal = caminho + tabela_final
        caminho_pastas = caminho
        subpasta = ["0", "0.25", "0.5", "0.75", "1"]
        tabelas = ["/tabela_atrasos.xls.xls", "/tabela_falsos_alarmes.xls.xls", "/tabela_mape.xls.xls", "/tabela_tempo.xls.xls"]
        
        book_final = xlrd.open_workbook(caminho_tabfinal)
        folhas = len(book_final.sheet_names())
        wb = copy(book_final)
                
        for z in range(folhas):
        
            for i in range(len(subpasta)):
                
                for j in range(len(tabelas)):
                
                    book = xlrd.open_workbook(caminho_pastas + subpasta[i] + tabelas[j])
                    
                    sh = book.sheet_by_index(0)
                    n_linhas = sh.nrows
                    
                    lineares = sh.cell_value(rowx = n_linhas-5, colx = z+1)
                    nlineares = sh.cell_value(rowx = n_linhas-4, colx = z+1)
                    sazonais = sh.cell_value(rowx = n_linhas-3, colx = z+1)
                    hibridas = sh.cell_value(rowx = n_linhas-2, colx = z+1)
                    geral = sh.cell_value(rowx = n_linhas-1, colx = z+1)
                    
                    
                    shw = wb.get_sheet(z)
                    
                    if(j == 0):
                        shw.write(21, i+1, lineares)
                        shw.write(22, i+1, nlineares)
                        shw.write(23, i+1, sazonais)
                        shw.write(24, i+1, hibridas)
                        shw.write(25, i+1, geral)
                        wb.save(caminho_tabfinal)
                        
                    elif(j == 1):
                        shw.write(3, i+1, lineares)
                        shw.write(4, i+1, nlineares)
                        shw.write(5, i+1, sazonais)
                        shw.write(6, i+1, hibridas)
                        shw.write(7, i+1, geral)
                        wb.save(caminho_tabfinal)
                        
                    elif(j == 2):
                        shw.write(12, i+1, lineares)
                        shw.write(13, i+1, nlineares)
                        shw.write(14, i+1, sazonais)
                        shw.write(15, i+1, hibridas)
                        shw.write(16, i+1, geral)
                        wb.save(caminho_tabfinal)
                        
                    elif(j == 3):
                        shw.write(30, i+1, lineares)
                        shw.write(31, i+1, nlineares)
                        shw.write(32, i+1, sazonais)
                        shw.write(33, i+1, hibridas)
                        shw.write(34, i+1, geral)
                        wb.save(caminho_tabfinal)
    
    def Calcular_estatisticas_bases(self):
        '''
        metodo para computar as estatisticas como media de desvio padrao das subpastas
        '''
        
        qtd_bases = c.variacao-1
        
        tabelas = ["/tabela_atrasos.xls", "/tabela_falsos_alarmes.xls", "/tabela_mape.xls", "/tabela_tempo.xls"]
        
        for z in range(len(tabelas)):
            
            nome = caminho_bases + tabelas[z]
            
            book = xlrd.open_workbook(nome)
            wb = copy(book)
            
            n_sheets = len(book.sheet_names())
            
            for i in range(n_sheets):
                sh = book.sheet_by_index(i)
                n_linhas = sh.nrows
                n_cols = sh.ncols
                sep = n_linhas + 2 
                
                shw = wb.get_sheet(i)
                shw.write(sep+1, 0,  'Lineares Graduais')
                shw.write(sep+2, 0,  'Lineares Abruptas')
                shw.write(sep+3, 0,  'Não Lineares Graduais')
                shw.write(sep+4, 0,  'Não lineares Abruptas')
                shw.write(sep+5, 0,  'Sazonais')
                shw.write(sep+6, 0,  'Hibridas')
                shw.write(sep+7, 0,  'Geral')
                
                for j in range(1, n_cols):
                    valores = []
                    for k in range(1, n_linhas-1):
                        valor = sh.cell_value(rowx=k, colx=j)
                        valores.append(valor)
                    
                    #correto
                    shw.write(sep+1, j,  np.mean(valores[0:qtd_bases]))
                    
                    
                    shw.write(sep+2, j,  np.mean(valores[qtd_bases:2*qtd_bases]))
                    shw.write(sep+3, j,  np.mean(valores[2*qtd_bases:3*qtd_bases]))
                    shw.write(sep+4, j,  np.mean(valores[3*qtd_bases:4*qtd_bases]))
                    shw.write(sep+5, j,  np.mean(valores[4*qtd_bases:5*qtd_bases]))
                    shw.write(sep+6, j,  np.mean(valores[5*qtd_bases:]))
                    shw.write(sep+7, j,  np.mean(valores))
                    
                    wb.save(nome)
                
    def ler(self, arq_xls, folha, linha, coluna):
        '''
        método para ler um valor de uma celula especifica
        :param: arq_xls: nome do arquivo
        :param: folha: folha em que o dado se encontra
        :param: linha: linha referente
        :param: coluna: coluna referente
        :return: celula buscada
        '''
        te = Tabela_excel()
        
        return te.ler(arq_xls, folha, linha, coluna) 
    
    def bases_linear_graduais(self, numero):
        '''
        metodo para abrir um arquivo de resultado para as bases lineares
        :param: numero: numero do arquivo
        :return: retorna a string do caminho da base
        '''
        
        base = (caminho_bases + '/Lineares-Graduais/lin-grad-' + str(numero) + '.xls')
        return base
    
    def bases_linear_abruptas(self, numero):
        '''
        metodo para abrir um arquivo de resultado para as bases lineares
        :param: numero: numero do arquivo
        :return: retorna a string do caminho da base
        '''
        
        base = (caminho_bases + '/Lineares-Abruptas/lin-abt-' + str(numero) + '.xls')
        return base
    
    def bases_nlinear_graduais(self, numero):
        '''
        metodo para abrir um arquivo de resultado para as bases não lineares
        :param: numero: numero do arquivo
        :return: retorna a string do caminho da base
        '''
        
        base = (caminho_bases + '/LinearesN-Graduais/lin_n-grad-' + str(numero) + '.xls')
        return base
    
    def bases_nlinear_abruptas(self, numero):
        '''
        metodo para abrir um arquivo de resultado para as bases não lineares
        :param: numero: numero do arquivo
        :return: retorna a string do caminho da base
        '''
        
        base = (caminho_bases + '/LinearesN-Abruptas/lin_n-abt-' + str(numero) + '.xls')
        return base
    
    def bases_sazonal(self, numero):
        '''
        metodo para abrir um arquivo de resultado para as bases sazonais
        :param: numero: numero do arquivo
        :return: retorna a string do caminho da base
        '''
        
        base = (caminho_bases + '/Sazonais/saz-' + str(numero) + '.xls')
        return base
    
    def bases_hibrida(self, numero):
        '''
        metodo para abrir um arquivo de resultado para as bases hibridas
        :param: numero: numero do arquivo
        :return: retorna a string do caminho da base
        '''
        
        base = (caminho_bases + '/Hibridas/hib-' + str(numero) + '.xls')
        return base
   
    def Criar_tabelas(self):
        '''
        linha 11 - linha das medias
        coluna 0 - falsos alarmes
        coluna 1 - atrasos
        coluna 2 - MAPE
        coluna 3 - tempo_execucao
        '''   
        
        metricas = [0, 1, 2, 3]
        linha_media = c.qtd_execucoes
        variacoes = c.variacao
        
        for z in metricas:
            
            if(z == 0):
                nome = caminho_bases+ '/tabela_falsos_alarmes'
            elif(z == 1):
                nome = caminho_bases+ '/tabela_atrasos'
            elif(z == 2):
                nome = caminho_bases+ '/tabela_mape'
            elif(z == 3):
                nome = caminho_bases+ '/tabela_tempo'
            
            tabela = Tabela_excel()
            folhas = ["sheet1"]
            cabecalho = ["Bases"] + c.folhas
            largura_col = 5000
            tabela.Criar_tabela(nome, folhas, cabecalho, largura_col)
            
            sheet = [10] + list(range(0, len(c.folhas)))
            vez = [0, 1, 2, 3, 4, 5]
            variacao = range(1, variacoes)
            
            col_metrica = z
            
            for i in sheet:
                contador = 0
                
                if(i == 10):
                    for j in vez:
                        for l in variacao:
                                
                            contador += 1
                                
                            if(j == 0):
                                parte2 = "Linear-Gradual- " + str(l)
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                                    
                            elif(j == 1):
                                parte2 = "Linear-Abrupta- " + str(l)
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                                
                            elif(j == 2):
                                parte2 = "NLinear-Gradual- " + str(l)
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                                    
                            elif(j == 3):
                                parte2 = "NLinear-Abrupta- " + str(l)
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                                    
                            elif(j == 4):
                                parte2 = "Sazonal - " + str(l)
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                                            
                            elif(j == 5):
                                parte2 = "Hibrida - " + str(l)
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                
                               
                                
                
                else:
                    
                    for j in vez:
                        for l in variacao:
                                
                            contador += 1
                                
                            parte1 = cabecalho[i+1] + " - "
                            
                            if(j == 0):
                                parte2 = "linear-grad - "
                                valor = self.ler(self.bases_linear_graduais(l), i, linha_media, col_metrica)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                                    
                            elif(j == 1):
                                parte2 = "linear-abt - "
                                valor = self.ler(self.bases_linear_abruptas(l), i, linha_media, col_metrica)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                                
                            elif(j == 2):
                                parte2 = "nlinear-grad - "
                                valor = self.ler(self.bases_nlinear_graduais(l), i, linha_media, col_metrica)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                                    
                            elif(j == 3):
                                parte2 = "nlinear-abt - "
                                valor = self.ler(self.bases_nlinear_abruptas(l), i, linha_media, col_metrica)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                                            
                            elif(j == 4):
                                parte2 = "sazonal - "
                                valor = self.ler(self.bases_sazonal(l), i, linha_media, col_metrica)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                                            
                            elif(j == 5):
                                parte2 = "hibrida - "
                                valor = self.ler(self.bases_hibrida(l), i, linha_media, col_metrica)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                
                            parte4 = str(l)
                                
                            print(parte1+parte2+parte4)
            
            tabela.Calcular_Medias2(variacao[-1]*len(vez))
   
    def Img_teste(self):
        '''
        método para gerar plots do teste estatístico
        '''
        
        # tabela para calcular o teste estatistico
        tabelas = ["/tabela_mape.xls"]
        
        for z in range(len(tabelas)):
            
            # caminho referente a tabela
            nome = caminho_bases + tabelas[z]
            
            # abrindo um workbook e copiando ele em uma variavel auxiliar
            book = xlrd.open_workbook(nome)
            
            # obtendo a quantidade de folhas 
            i = len(book.sheet_names())
            
            # abrindo a folha existente
            sh = book.sheet_by_index(i-1)
            
            # obtendo a quantidade linhas dentro da folha
            n_linhas = (c.variacao-1) * 6
            
            # obtendo a quantidade colunas dentro da folha
            n_cols = sh.ncols
            
            # variavel para salvar a primeira coluna das tabelas
            labels = []
            acuracias = []
            
            # for para a quantidade de colunas
            for j in range(1, n_cols):
                
                # variavel para salvar os valores de cada coluna
                valores = []
                
                # for para percorrer as linhas de cada coluna
                for k in range(0, n_linhas+1):
                    
                    # copiando o valor referente a linah e coluna passada
                    valor = sh.cell_value(rowx=k, colx=j)
                    
                    # se for a primeira coluna salva em labels
                    if(k == 0):
                        labels.append(valor)
                        
                    # caso nao salva as acuracias em valores
                    else:                                                           
                        valores.append(valor)
                
                # salvando o conjunto de acuracias    
                acuracias.append(np.asarray(valores))
                
            # convertendo a lista final em um array
            acuracias = np.asarray(acuracias)
            
            #computando o nemenyi posthuc
            nemenyi = NemenyiTestPostHoc(labels, acuracias)
            nome = "/friedman_mape"
            caminho = c.caminho_bases+c.pasta
            nemenyi.gerar_plot(nome, caminho)
        
        
def main():
    tbt = Tabela_testes()
    #tbt.Criar_tabelas()
    tbt.Calcular_estatisticas_bases()
    #tbt.Gerar_tabela_final()
    #tbt.Img_teste()  
    
          
if __name__ == "__main__":
    main()
    