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

#pastas = ['4']
#pastas = ['1', '2', '3', '4', '5']
#pastas = ['0', '0.25', '0.5', '0.75', '1']
#pastas = ['0.5', '0.75', '1', '1.5', '2', '3']
#pasta = pastas[4]
#pasta = 'IDPSO_ELM_B (condicao) - limite/Omega = 3/50'
#pasta = 'IDPSO_ELM_B (condicao) - limite/Omega = 10/50'
pasta = 'ELM_FEDD(Param)/1'

caminho_bases = "Tabelas/ZExperimentos/" + pasta

class Tabela_testes():
    def __init__(self):
        self.wb = Workbook()
        self.nome = ""
    
    def Gerar_tabela_final(self):
        '''
        metodo para agrupar os resultados que estavam em subpastas e salvar em um arquivo final
        '''
        
        #caminho = "E:/Workspace2/IDPSO_ELM/Tabelas/ZExperimentos/Sensores (nivel) - qtd sensores/"
        #caminho = "E:/Workspace2/IDPSO_ELM/Tabelas/ZExperimentos/IDPSO_ELM_B (condicao) - limite/"
        caminho = "E:/Workspace2/IDPSO_ELM/Tabelas/ZExperimentos/ELM_FEDD(Param)/"
        #pasta = "Nivel = 0.75/"
        #pasta = "Omega = 10/"
        #tabela_final = "Resultados - Sensores - qtd sensores.xls"
        #tabela_final = "Resultados - IDPSO_ELM_B (Condição) - Limite.xls"
        tabela_final = "Resultados - ELM-FEDD - nivel.xls"
        #caminho_tabfinal = caminho + pasta + tabela_final
        caminho_tabfinal = caminho + tabela_final
        
        #caminho_pastas = caminho + pasta
        caminho_pastas = caminho
        #subpasta = ["1", "5", "10", "20", "30"]
        #subpasta = ["1", "5", "10", "25", "50"]
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
        
        qtd_bases = 30
        
        tabelas = ["/tabela_atrasos.xls.xls", "/tabela_falsos_alarmes.xls.xls", "/tabela_mape.xls.xls", "/tabela_tempo.xls.xls"]
        
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
                shw.write(sep, 0,  'Lineares')
                shw.write(sep+1, 0,  'Não lineares')
                shw.write(sep+2, 0,  'Sazonais')
                shw.write(sep+3, 0,  'Hibridas')
                shw.write(sep+4, 0,  'Geral')
                
                for j in range(1, n_cols):
                    valores = []
                    for k in range(1, n_linhas):
                        valor = sh.cell_value(rowx=k, colx=j)
                        valores.append(valor)
                    
                    shw.write(sep, j,  np.mean(valores[0:qtd_bases]))
                    shw.write(sep+1, j,  np.mean(valores[qtd_bases+1:2*qtd_bases]))
                    shw.write(sep+2, j,  np.mean(valores[2*qtd_bases+1:3*qtd_bases]))
                    shw.write(sep+3, j,  np.mean(valores[3*qtd_bases+1:]))
                    shw.write(sep+4, j,  np.mean(valores))
                    
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
    
    def bases_linear(self, numero):
        '''
        metodo para abrir um arquivo de resultado para as bases lineares
        :param: numero: numero do arquivo
        :return: retorna a string do caminho da base
        '''
        
        base = (caminho_bases + '/Lineares/lin-' + str(numero) + '.xls.xls')
        self.nome = 'lin-' + str(numero)
        return base
    
    def bases_nlinear(self, numero):
        '''
        metodo para abrir um arquivo de resultado para as bases não lineares
        :param: numero: numero do arquivo
        :return: retorna a string do caminho da base
        '''
        
        base = (caminho_bases + '/LinearesN/lin_n-' + str(numero) + '.xls.xls')
        self.nome = 'lin_n-' + str(numero)
        return base
    
    def bases_sazonal(self, numero):
        '''
        metodo para abrir um arquivo de resultado para as bases sazonais
        :param: numero: numero do arquivo
        :return: retorna a string do caminho da base
        '''
        
        base = (caminho_bases + '/Sazonais/saz-' + str(numero) + '.xls.xls')
        self.nome = 'saz-' + str(numero)
        return base
    
    def bases_hibrida(self, numero):
        '''
        metodo para abrir um arquivo de resultado para as bases hibridas
        :param: numero: numero do arquivo
        :return: retorna a string do caminho da base
        '''
        
        base = (caminho_bases + '/Hibridas/hib-' + str(numero) + '.xls.xls')
        self.nome = 'hib-' + str(numero)
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
        g_linha_media = 6
        variacoes = 31
        
        tabela = Tabela_excel()
        
        for z in metricas:
            
            if(z == 0):
                nome = 'E:/Workspace2/IDPSO_ELM/Tabelas/ZExperimentos/'+pasta+ '/tabela_falsos_alarmes.xls'
            elif(z == 1):
                nome = 'E:/Workspace2/IDPSO_ELM/Tabelas/ZExperimentos/'+pasta+ '/tabela_atrasos.xls'
            elif(z == 2):
                nome = 'E:/Workspace2/IDPSO_ELM/Tabelas/ZExperimentos/'+pasta+ '/tabela_mape.xls'
            elif(z == 3):
                nome = 'E:/Workspace2/IDPSO_ELM/Tabelas/ZExperimentos/'+pasta+ '/tabela_tempo.xls'
                
            folhas = ["sheet1"]
            #cabecalho = ["Bases", "ELM_DDM", "CompoIDPSO_ELM_BLM_ECDD", "Sensores", "CompoIDPSO_ELM_Bor", "ELM_ECDD Perfeito", "ELM Sem Detecção"]
            #cabecalho = ["Bases", "ComportIDPSO_ELM_B, "ComportIDPSO_ELM_B"]
            #cabecalho = ["Bases", "Sensores (ECDD)"]
            cabecalho = ["Bases", "ELM-ECDD"]
            largura_col = 5000
            tabela.Criar_tabela(nome, folhas, cabecalho, largura_col)
            
            #sheet = [10, 0, 1]
            sheet = [10, 0]
            vez = [0, 1, 2, 3]
            variacao = range(1, variacoes)
            #variacao = range(1, 30)
            
            
            col_falsos_alarmes = z
            linha_media = g_linha_media
            
            for i in sheet:
                contador = 0
                
                if(i == 10):
                    for j in vez:
                        for l in variacao:
                                
                            contador += 1
                                
                            parte4 = str(l)
                                
                            if(j == 0):
                                parte2 = "Linear - " + parte4
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                                    
                            elif(j == 1):
                                parte2 = "Nlinear - " + parte4
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                                    
                            elif(j == 2):
                                parte2 = "Sazonal - " + parte4
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                                            
                            elif(j == 3):
                                parte2 = "Hibrida - " + parte4
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                
                               
                                
                
                else:
                    
                    for j in vez:
                        for l in variacao:
                                
                            contador += 1
                                
                            parte1 = cabecalho[i+1] + " - "
                                
                            if(j == 0):
                                parte2 = "linear - "
                                valor = self.ler(self.bases_linear(l), i, linha_media, col_falsos_alarmes)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                                    
                            elif(j == 1):
                                parte2 = "nlinear - "
                                valor = self.ler(self.bases_nlinear(l), i, linha_media, col_falsos_alarmes)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                                            
                            elif(j == 2):
                                parte2 = "sazonal - "
                                valor = self.ler(self.bases_sazonal(l), i, linha_media, col_falsos_alarmes)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                                            
                            elif(j == 3):
                                parte2 = "hibrida - "
                                valor = self.ler(self.bases_hibrida(l), i, linha_media, col_falsos_alarmes)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                
                            parte4 = str(l)
                                
                            print(parte1+parte2+parte4)
            
            tabela.Calcular_Medias2(variacao*4)
   
def main():
    tbt = Tabela_testes()
    #tbt.Criar_tabelas()
    #tbt.Calcular_estatisticas_bases()
    #tbt.Gerar_tabela_final()
    
          
if __name__ == "__main__":
    main()
    