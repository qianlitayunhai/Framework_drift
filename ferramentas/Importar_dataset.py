# -*- coding: UTF-8 -*-

'''
Created on 8 de fev de 2017

@author: gusta
'''
import pandas as pd
import matplotlib.pyplot as plt

#caminho onde se encontram as bases xlsx

class Datasets():
    def __init__(self, alocacao):
        if(alocacao == 'fora'):
            self.caminho_bases = 'series'
        elif(alocacao == 'dentro'):
            self.caminho_bases = '../series'
        
    '''
    classe que armazena as series com drifts
    '''
    

    def Leitura_dados(self, caminho, excel = None, csv = None):
        '''
        Metodo para fazer a leitura dos dados
        :param caminho: caminho da base que sera importada
        :return: retorna a serie temporal que o caminho direciona
        '''
        #leitura da serie dinamica
        
        if(excel == True):
            print(caminho)
            stream = pd.read_excel(caminho, header = None)
            stream = stream[0]
            stream = stream.as_matrix()
            return stream
        
        elif(csv == True):
            print(caminho)
            stream = pd.read_csv(caminho, header = None)
            stream = stream[0]
            stream = stream.as_matrix()
            return stream
    
    def bases_linear_graduais(self, numero):
        '''
        Metodo para mostrar o caminho das bases lineares graduais
        :param tipo: tipo das series lineares, podem ser dos tipos: 1, 2 e 3
        :param numero: numero das variacoes das series, pode variar entre [30,49]
        :return: retorna o caminho da base
        '''
        
        base = (self.caminho_bases + '/Series Geradas Permanentes/lineares_grad_abt/graduais/lin-grad' + str(numero)+ '.csv') 
        return base
    
    def bases_linear_abruptas(self, numero):
        '''
        Metodo para mostrar o caminho das bases lineares abruptas
        :param tipo: tipo das series lineares, podem ser dos tipos: 1, 2 e 3
        :param numero: numero das variacoes das series, pode variar entre [30,49]
        :return: retorna o caminho da base
        '''
        
        base = (self.caminho_bases + '/Series Geradas Permanentes/lineares_grad_abt/abruptas/lin-abt' + str(numero)+ '.csv') 
        return base
    
    def bases_nlinear_graduais(self, numero):
        '''
        Metodo para mostrar o caminho das bases nao lineares graduais
        :param tipo: tipo das series lineares, podem ser dos tipos: 1, 2 e 3
        :param numero: numero das variacoes das series, pode variar entre [30,49]
        :return: retorna o caminho da base
        '''
        
        base = (self.caminho_bases + '/Series Geradas Permanentes/nlineares_grad_abt/graduais/nlin-grad' + str(numero)+ '.csv')
        return base
    
    def bases_nlinear_abruptas(self, numero):
        '''
        Metodo para mostrar o caminho das bases nao lineares abruptas
        :param tipo: tipo das series lineares, podem ser dos tipos: 1, 2 e 3
        :param numero: numero das variacoes das series, pode variar entre [30,49]
        :return: retorna o caminho da base
        '''
        
        base = (self.caminho_bases + '/Series Geradas Permanentes/nlineares_grad_abt/abruptas/nlin-abt' + str(numero)+ '.csv') 
        return base
    
    def bases_hibridas(self, numero):
        '''
        Metodo para mostrar o caminho das bases hibridas
        :param numero: numero das variacoes das series, pode variar entre [1, 10]
        :return: retorna o caminho da base
        '''
        
        base = (self.caminho_bases + '/Series Geradas Permanentes/hibridas/hib-' + str(numero) + '.csv')
         
        return base
    
    def bases_lineares(self, numero):
        '''
        Metodo para mostrar o caminho das bases hibridas
        :param numero: numero das variacoes das series, pode variar entre [1, 10]
        :return: retorna o caminho da base
        '''
        
        base = (self.caminho_bases + '/Series Geradas Permanentes/lineares/lin-' + str(numero) + '.csv')
         
        return base
    
    def bases_nlineares(self, numero):
        '''
        Metodo para mostrar o caminho das bases hibridas
        :param numero: numero das variacoes das series, pode variar entre [1, 10]
        :return: retorna o caminho da base
        '''
        
        base = (self.caminho_bases + '/Series Geradas Permanentes/nlineares/nlin-' + str(numero) + '.csv')
         
        return base
    
    def bases_sazonais(self, numero):
        '''
        Metodo para mostrar o caminho das bases hibridas
        :param numero: numero das variacoes das series, pode variar entre [1, 10]
        :return: retorna o caminho da base
        '''
        
        base = (self.caminho_bases + '/Series Geradas Permanentes/sazonais/saz-' + str(numero) + '.csv')
         
        return base
    
    def bases_reais(self, tipo):
        '''
        Metodo para mostrar o caminho das bases reais
        :param tipo: tipo de séris utilizada
        :1 = Dow 30
        :2 = Nasdaq
        :3 = S&P 500
        :return: retorna o caminho da base
        '''
        
        if(tipo == 1):
            base = (self.caminho_bases + '/Series Reais/Dow.csv')
        if(tipo == 2):
            base = (self.caminho_bases + '/Series Reais/Nasdaq.csv')
        if(tipo == 3):
            base = (self.caminho_bases + '/Series Reais/S&P500.csv')
        if(tipo == 4):
            base = (self.caminho_bases + '/Series Reais/Dow-drift.csv')    
        return base
    
    def Plotar_serie(self, serie):
        plt.plot(serie)
        plt.show()

def main():
    dtst = Datasets('dentro')
    
    '''
    caminho = dtst.bases_linear_graduais(1)
    #caminho = dtst.bases_linear_abruptas(1)
    #caminho = dtst.bases_nlinear_graduais(1)
    #caminho = dtst.bases_nlinear_abruptas(1)
    dataset = dtst.Leitura_dados(caminho, csv=True)
    plt.plot(dataset)
    plt.show()
    '''
    for z in range(30):
        # codigo para printar varias series em uma imagem
        deteccoes = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000]
        i = z+1
        
        lin_grad = dtst.Leitura_dados(dtst.bases_linear_graduais(i), csv=True)
        lin_abt = dtst.Leitura_dados(dtst.bases_linear_abruptas(i), csv=True)
        nlin_grad = dtst.Leitura_dados(dtst.bases_nlinear_graduais(i), csv=True)
        nlin_abt = dtst.Leitura_dados(dtst.bases_nlinear_abruptas(i), csv=True)
        sazonais = dtst.Leitura_dados(dtst.bases_sazonais(i), csv=True)
        hibridas = dtst.Leitura_dados(dtst.bases_hibridas(i), csv=True)
    
        tamanho = 10
        fonte = 11
        linha = 1
    
        figura = plt.figure()
        g1 = figura.add_subplot(2, 3, 1)
        g1.plot(lin_grad)
        for i in range(len(deteccoes)):
            plt.axvline(deteccoes[i], linewidth=linha, color='r')
        g1.set_title("Linear gradual time series", fontsize = fonte)
        plt.tick_params(labelsize= tamanho)
        
        g2 = figura.add_subplot(2, 3, 2)
        g2.plot(lin_abt)
        for i in range(len(deteccoes)):
            plt.axvline(deteccoes[i], linewidth=linha, color='r')
        g2.set_title("Linear abrupt time series", fontsize = fonte)
        plt.tick_params(labelsize= tamanho)
        
        g3 = figura.add_subplot(2, 3, 3)
        g3.plot(nlin_grad)
        for i in range(len(deteccoes)):
            plt.axvline(deteccoes[i], linewidth=linha, color='r')
        g3.set_title("Non-linear gradual time series", fontsize = fonte)
        plt.tick_params(labelsize= tamanho)
        
        g4 = figura.add_subplot(2, 3, 4)
        g4.plot(nlin_abt)
        for i in range(len(deteccoes)):
            plt.axvline(deteccoes[i], linewidth=linha, color='r')
        g4.set_title("Non-linear abrupt time series", fontsize = fonte)
        
        g5 = figura.add_subplot(2, 3, 5)
        g5.plot(sazonais)
        for i in range(len(deteccoes)):
            plt.axvline(deteccoes[i], linewidth=linha, color='r')
        g5.set_title("Linear seasonal time series", fontsize = fonte)
        plt.tick_params(labelsize= tamanho)
        
        g6 = figura.add_subplot(2, 3, 6)
        g6.plot(hibridas)
        for i in range(len(deteccoes)):
            plt.axvline(deteccoes[i], linewidth=linha, color='r')
        g6.set_title("Hybrid time series", fontsize = fonte)
        
        plt.tick_params(labelsize= tamanho)
        plt.show()
    
    '''
    # codigo para printar varias series em uma imagem
    deteccoes = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000]
    i = 1
    
    lineares = dtst.Leitura_dados(dtst.bases_lineares(i), csv=True)
    #gerador.Plotar(dataset, deteccoes)
    
    nlineares = dtst.Leitura_dados(dtst.bases_nlineares(i), csv=True)
    #gerador.Plotar(dataset, deteccoes)
    
    sazonais = dtst.Leitura_dados(dtst.bases_sazonais(i), csv=True)
    #gerador.Plotar(dataset, deteccoes)

    hibridas = dtst.Leitura_dados(dtst.bases_hibridas(i), csv=True)
    #gerador.Plotar(dataset, deteccoes)

    tamanho = 20
    fonte = 18
    linha = 2

    figura = plt.figure()
    g1 = figura.add_subplot(2, 2, 1)
    g1.plot(lineares)
    for i in range(len(deteccoes)):
        plt.axvline(deteccoes[i], linewidth=linha, color='r')
    g1.set_title("Linear time series", fontsize = fonte)
    plt.tick_params(labelsize= tamanho)
    
    g2 = figura.add_subplot(2, 2, 2)
    g2.plot(nlineares)
    for i in range(len(deteccoes)):
        plt.axvline(deteccoes[i], linewidth=linha, color='r')
    g2.set_title("Nonlinear time series", fontsize = fonte)
    plt.tick_params(labelsize= tamanho)
    
    g3 = figura.add_subplot(2, 2, 3)
    g3.plot(sazonais)
    for i in range(len(deteccoes)):
        plt.axvline(deteccoes[i], linewidth=linha, color='r')
    g3.set_title("Linear seasonal time series", fontsize = fonte)
    plt.tick_params(labelsize= tamanho)
    
    g4 = figura.add_subplot(2, 2, 4)
    g4.plot(hibridas)
    for i in range(len(deteccoes)):
        plt.axvline(deteccoes[i], linewidth=linha, color='r')
    g4.set_title("Hybrid time series", fontsize = fonte)
    
    plt.tick_params(labelsize= tamanho)
    plt.show()
    '''  
    
if __name__ == "__main__":
    main()
    