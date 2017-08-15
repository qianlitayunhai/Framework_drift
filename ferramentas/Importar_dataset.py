# -*- coding: UTF-8 -*-

'''
Created on 8 de fev de 2017

@author: gusta
'''
import pandas as pd
import matplotlib.pyplot as plt

#caminho onde se encontram as bases xlsx
caminho_bases = '../series'

class Datasets():
    '''
    classe que armazena as series com drifts
    '''
    pass

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
    
    def bases_linear_graduais(self, tipo, numero):
        '''
        Metodo para mostrar o caminho das bases lineares graduais
        :param tipo: tipo das series lineares, podem ser dos tipos: 1, 2 e 3
        :param numero: numero das variacoes das series, pode variar entre [30,49]
        :return: retorna o caminho da base
        '''
        
        base = (caminho_bases + '/Lineares/Graduais/lin' + str(tipo) + '_grad' + str(numero)+ '.xlsx') 
        return base
    
    def bases_linear_abruptas(self, tipo, numero):
        '''
        Metodo para mostrar o caminho das bases lineares abruptas
        :param tipo: tipo das series lineares, podem ser dos tipos: 1, 2 e 3
        :param numero: numero das variacoes das series, pode variar entre [30,49]
        :return: retorna o caminho da base
        '''
        
        base = (caminho_bases + '/Lineares/Abruptas/lin' + str(tipo) + '_abt' + str(numero)+ '.xlsx') 
        return base
    
    def bases_nlinear_graduais(self, tipo, numero):
        '''
        Metodo para mostrar o caminho das bases nao lineares graduais
        :param tipo: tipo das series lineares, podem ser dos tipos: 1, 2 e 3
        :param numero: numero das variacoes das series, pode variar entre [30,49]
        :return: retorna o caminho da base
        '''
        
        base = (caminho_bases + '/Lineares Não/Graduais/lin' +str(tipo)+ '_n_grad' +str(numero)+ '.xlsx') 
        return base
    
    def bases_nlinear_abruptas(self, tipo, numero):
        '''
        Metodo para mostrar o caminho das bases nao lineares abruptas
        :param tipo: tipo das series lineares, podem ser dos tipos: 1, 2 e 3
        :param numero: numero das variacoes das series, pode variar entre [30,49]
        :return: retorna o caminho da base
        '''
        
        base = (caminho_bases + '/Lineares Não/Abruptas/lin' + str(tipo) + '_n_abt' + str(numero)+ '.xlsx') 
        return base
    
    def bases_hibridas(self, numero):
        '''
        Metodo para mostrar o caminho das bases hibridas
        :param numero: numero das variacoes das series, pode variar entre [1, 10]
        :return: retorna o caminho da base
        '''
        
        base = (caminho_bases + '/Series Geradas Permanentes Permanentes/hibridas/hib-' + str(numero) + '.csv')
         
        return base
    
    def bases_lineares(self, numero):
        '''
        Metodo para mostrar o caminho das bases hibridas
        :param numero: numero das variacoes das series, pode variar entre [1, 10]
        :return: retorna o caminho da base
        '''
        
        base = (caminho_bases + '/Series Geradas Permanentes/lineares/lin-' + str(numero) + '.csv')
         
        return base
    
    def bases_nlineares(self, numero):
        '''
        Metodo para mostrar o caminho das bases hibridas
        :param numero: numero das variacoes das series, pode variar entre [1, 10]
        :return: retorna o caminho da base
        '''
        
        base = (caminho_bases + '/Series Geradas Permanentes/nlineares/nlin-' + str(numero) + '.csv')
         
        return base
    
    def bases_sazonais(self, numero):
        '''
        Metodo para mostrar o caminho das bases hibridas
        :param numero: numero das variacoes das series, pode variar entre [1, 10]
        :return: retorna o caminho da base
        '''
        
        base = (caminho_bases + '/Series Geradas Permanentes/sazonais/saz-' + str(numero) + '.csv')
         
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
            base = (caminho_bases + '/Series Reais/Dow.csv')
        if(tipo == 2):
            base = (caminho_bases + '/Series Reais/Nasdaq.csv')
        if(tipo == 3):
            base = (caminho_bases + '/Series Reais/S&P500.csv')
        if(tipo == 4):
            base = (caminho_bases + '/Series Reais/Dow-drift.csv')    
        return base
    
    def Plotar_serie(self, serie):
        plt.plot(serie)
        plt.show()

def main():
    
    dtst = Datasets()
    caminho = dtst.bases_reais(4)
    dataset = dtst.Leitura_dados(caminho, csv=True)
    plt.plot(dataset)
    plt.show()
    
    '''
    deteccoes = [2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000, 18000]
    i = 6
    
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
        
    '''
    dataset = dtst.Leitura_dados(dtst.bases_linear_graduais(3, 40), excel=True)
    dtst.Plotar_serie(dataset)
    '''    
    
if __name__ == "__main__":
    main()
    