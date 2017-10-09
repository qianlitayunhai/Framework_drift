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
from teste_estatistico.Nemenyi import NemenyiTestPostHoc, Ler_dados

c = Constantes('dentro')
pasta = c.pasta
caminho_bases = c.caminho_bases + pasta

class Tabela_testes():
    def __init__(self):
        self.wb = Workbook()
        self.nome = ""
    
    def Arquivo_tabela_final_artificiais(self):
        '''
        metodo para gerar a tabela que vai conter os resultados finais dos experimentos com parametros
        '''
        
        tabela = Tabela_excel()
        nome = c.caminho_bases + c.pasta + "/Resultados"
        folhas = c.folhas
        largura_col = 5000
        tabela.Criar_tabela(nome, folhas, largura_col=largura_col)
            
        metricas = ['Falsos Alarmes', 'MAE', 'Atrasos', 'Tempo']
        pastas = ['[1]', '[2]', '[3]', '[4]']
        cabecalhos = ['Bases', 
                      'Lineares Graduais', 
                      'Lineares Abruptas', 
                      'Não Lineares Graduais', 
                      'Não Lineares Abruptas', 
                      'Sazonais', 
                      'Híbridas', 
                      'Média Geral']    
        
        for i in range(len(c.folhas)):

            # escrevendo o bloco de falsos alarmes
            tabela.Adicionar_dado(i, 0, 0, metricas[0])
            linha = 1
            for j in range(len(cabecalhos)):
                tabela.Adicionar_dado(i, 0, linha, cabecalhos[j])
                linha += 1
            for k in range(len(pastas)):
                tabela.Adicionar_dado(i, k+1, 1, pastas[k])
        
        
        
            # escrevendo o bloco de MAE
            linha += 1
            bases = linha + 1
            tabela.Adicionar_dado(i, 0, linha, metricas[1])
            for j in range(len(cabecalhos)):
                linha += 1
                tabela.Adicionar_dado(i, 0, linha, cabecalhos[j])
            for k in range(len(pastas)):
                tabela.Adicionar_dado(i, k+1, bases, pastas[k])
                
            
            
            # escrevendo o bloco de Atrasos
            linha += 2
            bases = linha + 1
            tabela.Adicionar_dado(i, 0, linha, metricas[2])
            for j in range(len(cabecalhos)):
                linha += 1
                tabela.Adicionar_dado(i, 0, linha, cabecalhos[j])
            for k in range(len(pastas)):
                tabela.Adicionar_dado(i, k+1, bases, pastas[k])
            
            
            
            # escrevendo o bloco de Tempo
            linha += 2
            bases = linha + 1
            tabela.Adicionar_dado(i, 0, linha, metricas[3])
            for j in range(len(cabecalhos)):
                linha += 1
                tabela.Adicionar_dado(i, 0, linha, cabecalhos[j])
            for k in range(len(pastas)):
                tabela.Adicionar_dado(i, k+1, bases, pastas[k])
                
    def Arquivo_tabela_final_reais(self):
        '''
        metodo para gerar a tabela que vai conter os resultados finais dos experimentos com parametros
        '''
        
        tabela = Tabela_excel()
        nome = c.caminho_bases + c.pasta + "/Resultados"
        folhas = c.folhas
        largura_col = 5000
        tabela.Criar_tabela(nome, folhas, largura_col=largura_col)
            
        metricas = ['Falsos Alarmes', 'MAE', 'Atrasos', 'Tempo']
        pastas = ['[1]', '[2]', '[3]', '[4]']
        cabecalhos = ['Bases', 
                      'Down-drift', 
                      'S&P500-drift', 
                      'Média Geral']    
        
        for i in range(len(c.folhas)):

            # escrevendo o bloco de falsos alarmes
            tabela.Adicionar_dado(i, 0, 0, metricas[0])
            linha = 1
            for j in range(len(cabecalhos)):
                tabela.Adicionar_dado(i, 0, linha, cabecalhos[j])
                linha += 1
            for k in range(len(pastas)):
                tabela.Adicionar_dado(i, k+1, 1, pastas[k])
        
        
            # escrevendo o bloco de MAE
            linha += 1
            bases = linha + 1
            tabela.Adicionar_dado(i, 0, linha, metricas[1])
            for j in range(len(cabecalhos)):
                linha += 1
                tabela.Adicionar_dado(i, 0, linha, cabecalhos[j])
            for k in range(len(pastas)):
                tabela.Adicionar_dado(i, k+1, bases, pastas[k])
                
            
            # escrevendo o bloco de Atrasos
            linha += 2
            bases = linha + 1
            tabela.Adicionar_dado(i, 0, linha, metricas[2])
            for j in range(len(cabecalhos)):
                linha += 1
                tabela.Adicionar_dado(i, 0, linha, cabecalhos[j])
            for k in range(len(pastas)):
                tabela.Adicionar_dado(i, k+1, bases, pastas[k])
            
            
            # escrevendo o bloco de Tempo
            linha += 2
            bases = linha + 1
            tabela.Adicionar_dado(i, 0, linha, metricas[3])
            for j in range(len(cabecalhos)):
                linha += 1
                tabela.Adicionar_dado(i, 0, linha, cabecalhos[j])
            for k in range(len(pastas)):
                tabela.Adicionar_dado(i, k+1, bases, pastas[k])
                
    def Gerar_tabela_final_artificiais(self):
        '''
        metodo para agrupar os resultados que estavam em subpastas e salvar em um arquivo final para as series artificiais
        '''
        
        # gerando a tabela final
        self.Arquivo_tabela_final_artificiais()
        
        # definindo algumas variaveis padrões
        caminho = c.caminho_bases + c.pasta + "/"
        tabela_final = "Resultados.xls"
        caminho_tabfinal = caminho + tabela_final
        caminho_pastas = caminho
        subpasta = ["[1]", "[2]", "[3]", "[4]"]
        arquivos = ["/tabela_atrasos.xls", "/tabela_falsos_alarmes.xls", "/tabela_mape.xls", "/tabela_tempo.xls"]
        
        # criando as estatisticas das subpastas
        self.Criar_tabelas_subpastas(subpasta, artificiais=True)
        
        # abrindo o arquivo onde os dados serão inscritos
        book_final = xlrd.open_workbook(caminho_tabfinal)
        folhas = len(book_final.sheet_names())
        wb = copy(book_final)
                
        # for para quantidade de folhas da tabela
        for z in range(folhas):
            #for para as subpastas [1]...
            for i in range(len(subpasta)):
                # for para entrar em cada arquivo de dados FA, MAE...
                for j in range(len(arquivos)):
                
                    # abrindo um arquivo por vez e salvando em book para poder coletar as informações
                    book = xlrd.open_workbook(caminho_pastas + subpasta[i] + arquivos[j])
                    
                    # obtendo a folha principal da tabela
                    sh = book.sheet_by_index(0)
                    # salvando a quantiade de linhas do arquivo
                    n_linhas = sh.nrows
                    
                    # contando da ultima linha salvando as informacoes de medias do arquivo
                    lineares_grad = sh.cell_value(rowx = n_linhas-7, colx = z+1)
                    lineares_abt = sh.cell_value(rowx = n_linhas-6, colx = z+1)
                    nlineares_grad = sh.cell_value(rowx = n_linhas-5, colx = z+1)
                    nlineares_abt = sh.cell_value(rowx = n_linhas-4, colx = z+1)
                    sazonais = sh.cell_value(rowx = n_linhas-3, colx = z+1)
                    hibridas = sh.cell_value(rowx = n_linhas-2, colx = z+1)
                    geral = sh.cell_value(rowx = n_linhas-1, colx = z+1)
                    
                    
                    # obtendo a folha referente do arquivo Resultados
                    shw = wb.get_sheet(z)
                    
                    # de acordo com a métrica escreve no local especifico
                    # atrasos
                    if(j == 0):
                        shw.write(22, i+1, lineares_grad)
                        shw.write(23, i+1, lineares_abt)
                        shw.write(24, i+1, nlineares_grad)
                        shw.write(25, i+1, nlineares_abt)
                        shw.write(26, i+1, sazonais)
                        shw.write(27, i+1, hibridas)
                        shw.write(28, i+1, geral)
                        wb.save(caminho_tabfinal)
                    
                    # falsos alarmes
                    elif(j == 1):
                        shw.write(2, i+1, lineares_grad)
                        shw.write(3, i+1, lineares_abt)
                        shw.write(4, i+1, nlineares_grad)
                        shw.write(5, i+1, nlineares_abt)
                        shw.write(6, i+1, sazonais)
                        shw.write(7, i+1, hibridas)
                        shw.write(8, i+1, geral)
                        wb.save(caminho_tabfinal)
                    
                    # mae
                    elif(j == 2):
                        shw.write(12, i+1, lineares_grad)
                        shw.write(13, i+1, lineares_abt)
                        shw.write(14, i+1, nlineares_grad)
                        shw.write(15, i+1, nlineares_abt)
                        shw.write(16, i+1, sazonais)
                        shw.write(17, i+1, hibridas)
                        shw.write(18, i+1, geral)
                        wb.save(caminho_tabfinal)
                    
                    # tempo
                    elif(j == 3):
                        shw.write(32, i+1, lineares_grad)
                        shw.write(33, i+1, lineares_abt)
                        shw.write(34, i+1, nlineares_grad)
                        shw.write(35, i+1, nlineares_abt)
                        shw.write(36, i+1, sazonais)
                        shw.write(37, i+1, hibridas)
                        shw.write(38, i+1, geral)
                        wb.save(caminho_tabfinal)
    
    def Gerar_tabela_final_reais(self):
        '''
        metodo para agrupar os resultados que estavam em subpastas e salvar em um arquivo final para as series reais com drifts
        '''
        
        # gerando a tabela final
        self.Arquivo_tabela_final_reais()
        
        # definindo algumas variaveis padrões
        caminho = c.caminho_bases + c.pasta + "/"
        tabela_final = "Resultados.xls"
        caminho_tabfinal = caminho + tabela_final
        caminho_pastas = caminho
        subpasta = ["[1]", "[2]", "[3]", "[4]"]
        arquivos = ["/tabela_atrasos.xls", "/tabela_falsos_alarmes.xls", "/tabela_mape.xls", "/tabela_tempo.xls"]
        
        # criando as estatisticas das subpastas
        self.Criar_tabelas_subpastas(subpasta, reais=True)
        
        # abrindo o arquivo onde os dados serão inscritos
        book_final = xlrd.open_workbook(caminho_tabfinal)
        folhas = len(book_final.sheet_names())
        wb = copy(book_final)
                
        # for para quantidade de folhas da tabela
        for z in range(folhas):
            #for para as subpastas [1]...
            for i in range(len(subpasta)):
                # for para entrar em cada arquivo de dados FA, MAE...
                for j in range(len(arquivos)):
                
                    # abrindo um arquivo por vez e salvando em book para poder coletar as informações
                    book = xlrd.open_workbook(caminho_pastas + subpasta[i] + arquivos[j])
                    
                    # obtendo a folha principal da tabela
                    sh = book.sheet_by_index(0)
                    # salvando a quantiade de linhas do arquivo
                    n_linhas = sh.nrows
                    
                    # contando da ultima linha salvando as informacoes de medias do arquivo
                    down = sh.cell_value(rowx = n_linhas-3, colx = z+1)
                    sp = sh.cell_value(rowx = n_linhas-2, colx = z+1)
                    geral = sh.cell_value(rowx = n_linhas-1, colx = z+1)
                    
                    
                    # obtendo a folha referente do arquivo Resultados
                    shw = wb.get_sheet(z)
                    
                    # de acordo com a métrica escreve no local especifico
                    # atrasos
                    if(j == 0):
                        shw.write(14, i+1, down)
                        shw.write(15, i+1, sp)
                        shw.write(16, i+1, geral)
                        wb.save(caminho_tabfinal)
                    
                    # falsos alarmes
                    elif(j == 1):
                        shw.write(2, i+1, down)
                        shw.write(3, i+1, sp)
                        shw.write(4, i+1, geral)
                        wb.save(caminho_tabfinal)
                    
                    # mae
                    elif(j == 2):
                        shw.write(8, i+1, down)
                        shw.write(9, i+1, sp)
                        shw.write(10, i+1, geral)
                        wb.save(caminho_tabfinal)
                    
                    # tempo
                    elif(j == 3):
                        shw.write(20, i+1, down)
                        shw.write(21, i+1, sp)
                        shw.write(22, i+1, geral)
                        wb.save(caminho_tabfinal)
    
    def Calcular_estatisticas_bases_artificiais(self):
        '''
        metodo para computar as estatisticas como media de desvio padrao das subpastas
        '''
        
        print("Computando estatisticas...")
        
        qtd_bases = c.variacao_final-1
        
        tabelas = ["/tabela_atrasos.xls", "/tabela_falsos_alarmes.xls", "/tabela_mape.xls", "/tabela_tempo.xls"]
        
        for z in range(len(tabelas)):
            
            nome = caminho_bases + tabelas[z]
            book = xlrd.open_workbook(nome)
            wb = copy(book)
            
            n_sheets = len(book.sheet_names())
            
            for i in range(n_sheets):
                sh = book.sheet_by_index(i)
                sh.width = 10000
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
                    shw.write(sep, j,  c.folhas[j-1])
                    shw.write(sep+1, j,  np.mean(valores[0:qtd_bases]))
                    shw.write(sep+2, j,  np.mean(valores[qtd_bases:2*qtd_bases]))
                    shw.write(sep+3, j,  np.mean(valores[2*qtd_bases:3*qtd_bases]))
                    shw.write(sep+4, j,  np.mean(valores[3*qtd_bases:4*qtd_bases]))
                    shw.write(sep+5, j,  np.mean(valores[4*qtd_bases:5*qtd_bases]))
                    shw.write(sep+6, j,  np.mean(valores[5*qtd_bases:]))
                    shw.write(sep+7, j,  np.mean(valores))
                    
                    wb.save(nome)
    
    def Calcular_estatisticas_bases_reais(self):
        '''
        metodo para computar as estatisticas como media de desvio padrao das subpastas para as series reais com drift
        '''
        
        print("Computando estatisticas...")
        
        qtd_bases = c.variacao_final-1
        
        tabelas = ["/tabela_atrasos.xls", "/tabela_falsos_alarmes.xls", "/tabela_mape.xls", "/tabela_tempo.xls"]
        
        for z in range(len(tabelas)):
            
            nome = caminho_bases + tabelas[z]
            book = xlrd.open_workbook(nome)
            wb = copy(book)
            
            n_sheets = len(book.sheet_names())
            
            for i in range(n_sheets):
                sh = book.sheet_by_index(i)
                sh.width = 10000
                n_linhas = sh.nrows
                n_cols = sh.ncols
                sep = n_linhas + 2 
                
                shw = wb.get_sheet(i)
                shw.write(sep+1, 0,  'Down-drift')
                shw.write(sep+2, 0,  'S&P500-drift')
                shw.write(sep+3, 0,  'Geral')
                
                for j in range(1, n_cols):
                    valores = []
                    for k in range(1, n_linhas-1):
                        valor = sh.cell_value(rowx=k, colx=j)
                        valores.append(valor)
                    
                    #correto
                    shw.write(sep, j,  c.folhas[j-1])
                    shw.write(sep+1, j,  np.mean(valores[0:1]))
                    shw.write(sep+2, j,  np.mean(valores[1:2]))
                    shw.write(sep+3, j,  np.mean(valores))
                    
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
    
    def bases_reais(self, numero):
        '''
        metodo para abrir um arquivo de resultado para as bases reais
        :param: numero: numero do arquivo
        :return: retorna a string do caminho da base
        '''
        
        if(numero == 0):
            base = (caminho_bases + '/Reais/dow.xls')
        
        elif(numero == 1):
            base = (caminho_bases + '/Reais/nasdaq.xls')
            
        elif(numero == 2):
            base = (caminho_bases + '/Reais/SP500.xls')
        
        return base

    def bases_reais_drift(self, numero, retorno = None):
        '''
        metodo para abrir um arquivo de resultado para as bases reais com drift
        :param: numero: numero do arquivo
        :return: retorna a string do caminho da base
        '''
        
        if(retorno == None):
            if(numero == 0):
                base = (caminho_bases + '/Reais/Down-1972to1975.xls')
            
            elif(numero == 1):
                base = (caminho_bases + '/Reais/S&P500-1986to2002.xls')
        
        else:
        
            if(numero == 0):
                base = (caminho_bases + '/Reais/Dow-drift.xls')
            
            elif(numero == 1):
                base = (caminho_bases + '/Reais/S&P500-drift.xls')
        
        return base
    
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
   
    def Criar_tabelas_artificiais(self):
        '''
        linha 11 - linha das medias
        coluna 0 - falsos alarmes
        coluna 1 - atrasos
        coluna 2 - MAPE
        coluna 3 - tempo_execucao
        '''   
        
        metricas = [0, 1, 2, 3]
        linha_media = c.qtd_execucoes
        variacoes = c.variacao_final
        
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
            
            tabela.Calcular_Medias3(variacao[-1]*len(vez))
            
        # computando as estatisticas opor bases
        self.Calcular_estatisticas_bases_artificiais()
        self.Img_teste_artificial()
        
    def Criar_tabelas_reais_drift(self):
        '''
        linha 11 - linha das medias
        coluna 0 - falsos alarmes
        coluna 1 - atrasos
        coluna 2 - MAPE
        coluna 3 - tempo_execucao
        '''   
        
        metricas = [0, 1, 2, 3]
        linha_media = c.qtd_execucoes + 1
        variacoes = 2
        
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
            vez = [0, 1]
            variacao = range(1, variacoes)
            
            col_metrica = z
            
            for i in sheet:
                contador = 0
                
                if(i == 10):
                    for j in vez:
                        for l in variacao:
                                
                            contador += 1
                                
                            if(j == 0):
                                parte2 = "Down-drift- " + str(l)
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                                    
                            elif(j == 1):
                                parte2 = "S&P500-drift- " + str(l)
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                                
                                
                
                else:
                    
                    for j in vez:
                        for l in variacao:
                                
                            contador += 1
                                
                            parte1 = cabecalho[i+1] + " - "
                            
                            if(j == 0):
                                parte2 = "Down-drift- "
                                valor = self.ler(self.bases_reais_drift(j), i, linha_media, col_metrica)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                                    
                            elif(j == 1):
                                parte2 = "S&P500-drift- "
                                valor = self.ler(self.bases_reais_drift(j), i, linha_media, col_metrica)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                                
                            parte4 = str(l)
                                
                            print(parte1+parte2+parte4)
            
            tabela.Calcular_Medias3(variacao[-1]*len(vez))
            
        # computando as estatisticas opor bases
        self.Calcular_estatisticas_bases_reais()
        self.Img_teste_reais()
   
    def Criar_tabelas_reais(self):
        '''
        linha 11 - linha das medias
        coluna 0 - falsos alarmes
        coluna 1 - atrasos
        coluna 2 - MAPE
        coluna 3 - tempo_execucao
        '''   
        
        metricas = [2]
        
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
            
            sheet = [100] + list(range(0, len(c.folhas)))
            vez = [0, 1, 2]
            
            col_metrica = z
            
            for i in sheet:
                contador = 0
                
                if(i == 100):
                    for j in vez:
                        for l in range(c.qtd_execucoes):
                            contador += 1
                                    
                            if(j == 0):
                                parte2 = "Down- " +str(l)
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                                        
                            elif(j == 1):
                                parte2 = "Nasdaq- " +str(l)
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                                    
                            elif(j == 2):
                                parte2 = "S&P500- " +str(l)
                                tabela.Adicionar_dado(0, 0, contador, parte2)
                                    
                else:
                    
                    for j in vez:
                        
                        for l in range(1, c.qtd_execucoes+1):
                                
                            contador += 1
                                    
                            parte1 = cabecalho[i+1] + " - "
                                
                            if(j == 0):
                                parte2 = "Down - " +str(l)
                                valor = self.ler(self.bases_reais(j), i, l, col_metrica)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                                        
                            elif(j == 1):
                                parte2 = "Nasdaq - " +str(l)
                                valor = self.ler(self.bases_reais(j), i, l, col_metrica)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                                    
                            elif(j == 2):
                                parte2 = "S&P500 - " +str(l)
                                valor = self.ler(self.bases_reais(j), i, l, col_metrica)
                                tabela.Adicionar_dado(0, i+1, contador, valor)
                                        
                            print(parte1+parte2)
            
            linha_media = c.qtd_execucoes*len(vez)
            tabela.Calcular_Medias3(linha_media)
            
        # computando as estatisticas opor bases
        tbt = Ler_dados()
        labels, acuracias = tbt.obter_dados_arquivo(c.caminho_bases + c.pasta + '/tabela_mape.xls', [1, linha_media], [1, len(c.folhas)]) 
        nemenyi = NemenyiTestPostHoc(labels, acuracias)
        nemenyi.gerar_plot("/friedman_series_fin", c.caminho_bases + c.pasta)
   
    def Criar_tabelas_subpastas(self, sub_pastas, artificiais=None, reais=None):
        global caminho_bases
        copia = caminho_bases
        
        for i in sub_pastas:
            caminho_bases = copia
            caminho_bases = caminho_bases +"/"+ i
            
            if(artificiais == True):
                self.Criar_tabelas_artificiais()
            elif(reais == True):
                self.Criar_tabelas_reais_drift()
                
    def Img_teste_artificial(self):
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
            n_linhas = (c.variacao_final-1) * 6
            
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
            global caminho_bases
            caminho = caminho_bases
            nemenyi.gerar_plot(nome, caminho)
    
    def Img_teste_reais(self):
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
            n_linhas = (c.variacao_final-1) * 2
            
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
            global caminho_bases
            caminho = caminho_bases
            nemenyi.gerar_plot(nome, caminho)
    
def main():
    gerar_teste_acuracia_reais = True
    gerar_teste_acuracia = False
    gerar_planilhas_parametros_artificiais = False
    gerar_planilhas_parametros_reais = False
    
    tbt = Tabela_testes()
    
    if(gerar_teste_acuracia_reais):
        tbt.Criar_tabelas_reais()
        
    if(gerar_teste_acuracia):
        tbt.Criar_tabelas_artificiais()
        
    if(gerar_planilhas_parametros_artificiais):
        tbt.Gerar_tabela_final_artificiais()
        
    if(gerar_planilhas_parametros_reais):
        tbt.Gerar_tabela_final_reais()
    
          
if __name__ == "__main__":
    main()
    
    