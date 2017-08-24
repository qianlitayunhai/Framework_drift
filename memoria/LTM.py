#-*- coding: utf-8 -*-
'''
Created on 16 de ago de 2017

@author: gusta
'''
import scipy.spatial.distance as sp
import numpy as np
from ferramentas.Particionar_series import Particionar_series
from ferramentas.Importar_dataset import Datasets
from regressores.IDPSO_ELM import IDPSO_ELM
from sklearn.metrics.regression import mean_absolute_error
import copy
import matplotlib.pyplot as plt
#plt.style.use('ggplot')


class Ambiente():
    def __init__(self, particulas, gbest):
        '''
        Classe para armazenar ambientes, cada ambiente é formado por um enxame
        :param particulas: particulas do enxame
        :param gbest: melhor particula do enxame
        '''
        
        self.particulas = particulas
        self.gbest = gbest

class LTM():
    def __init__(self, qtd_memoria, limiar_exclusao, tx_espalhar):
        '''
        Classe para lidar com a Long Term Memory, memória de longo prazo
        :param qtd_memoria: tamanho que a memória vai possuir
        :param limiar_exclusao: limiar_exclusao para excluir um ambiente
        :param limiar_lembranca: limiar para definir se um modelo vai ser treinado
        :param tx_espalhar: porcentagem entre 0 e 1 para definir quantos % do enxame será reinicializado 
        '''
        
        self.tamanho_max_memoria = qtd_memoria
        
        self.limiar_exclusao = limiar_exclusao
        self.tx_espalhar = tx_espalhar
        
        self.qtd_memoria = 0
        self.vetor_ambientes = []
    
    def Distancia_vetores(self, a, b):
        '''
        método para calcular a distancia entre dois arrays 
        :param a: primeiro array
        :param b: segundo array
        :return: retorna a distancia entre os dois 
        '''
        
        distancia = sp.norm(a-b)
        return distancia
    
    def Adicionar_ambiente(self, ambiente):
        '''
        método para adicionar um ambiente na memória
        :param: ambiente: ambiente a ser adicionado na memória 
        '''
        
        if(self.qtd_memoria < self.tamanho_max_memoria):
            #adicionar ambiente na memoria
            #print("Ambiente adicionado!")
            self.vetor_ambientes.append(ambiente)
            self.qtd_memoria +=1
            
        else:
            #calcular a distancia do novo ambiente para os antigos
            vetor_distancias = []
            for i in self.vetor_ambientes:
                distancia = self.Distancia_vetores(ambiente.gbest.pesos, i.gbest.pesos)
                vetor_distancias.append(distancia)

            #print("vetor de distancias: ", vetor_distancias)
            
            #indice do ambiente mais similar
            j = np.argmin(vetor_distancias)
            #print("Menor valor: ", vetor_distancias[j])
            
            
            # com a memória cheia, se o ambiente novo for muito diferente
            if(vetor_distancias[j] < self.limiar_exclusao):
                
                # então o mais próximo é apagado
                #print("Ambiente [", j, "] apagado")
                del self.vetor_ambientes[j]
                
                # e adicionasse o novo
                #print("Ambiente antigo substituido!")
                self.vetor_ambientes.append(ambiente)

    def Relembrar_ambiente(self, enxame_atual, dados, lags):
        '''
        metodo para relembrar um ambiente, caso o enxame não seja suficiente retreina a partir da melhor solução
        :param: enxame_atual: enxame atual que será substituido
        :param: dados: dados para avaliar a acuracia dos modelos armazenados
        :param: lags: quantidade de lags para modelar os dados de entrada da rede
        :return: retorna o melhor enxame para os dados passados
        '''
        
        particao = Particionar_series(dados, [1, 0, 0], lags)
        [dados_x, dados_y] = particao.Part_train()
        
        #print("Quantidade de dados para treinamento: ", len(dados_y))
        
        acuracias = []
        if(self.qtd_memoria != 0):
            for i in self.vetor_ambientes:
                previsao = i.gbest.Predizer(dados_x)
                acuracias.append(mean_absolute_error(dados_y, previsao))
            #print("Acuracias: ", acuracias)
            
            previsao = enxame_atual.Predizer(dados_x)
            erro_atual = mean_absolute_error(dados_y, previsao)
            #print("Acuracia do modelo atual: ", erro_atual)
            
            j = np.argmin(acuracias)
            #print("Acuracia do melhor modelo da memória: ", erro_atual)
            
            if(acuracias[j] < erro_atual):
                #print("Melhor solução encontrada na memória [", j, "]: ", acuracias[j])
                enxame_atual.particulas = copy.deepcopy(self.vetor_ambientes[j].particulas)
                enxame_atual.Atualizar_bestmodel(self.vetor_ambientes[j].gbest) 
                #print("Comparacao modelos: ", enxame_atual.best_elm == self.vetor_ambientes[j].gbest)
                return enxame_atual
            
            else:
                
                return enxame_atual
                '''
                # criando uma instancia do modelo atual
                novo = copy.deepcopy(enxame_atual)
                novo.tx_espalhar = self.tx_espalhar
                novo.Retreinar()
                
                # espalhando as soluções e fazendo uma nova busca
                previsao = enxame_atual.Predizer(dados_x)
                erro_atual = mean_absolute_error(dados_y, previsao)
                #print("Acuracia do modelo atual: ", erro_atual)
                
                # realizando a previsao para o conjunto de dados atual
                previsao = novo.Predizer(dados_x)
                erro_novo = mean_absolute_error(dados_y, previsao)
                #print("Acuracia do modelo atualizado:", erro_novo)
                
                # se a solucao treinada for melhor que a solucao atual entao ela é atualizada
                if(erro_novo < erro_atual):
                    enxame_atual = novo
                
                # retorna a melhor solucao
                return enxame_atual
                '''
    
    def Relembrar_acurado(self, enxame_atual, dados, lags):
        '''
        metodo para relembrar um ambiente, caso o enxame não seja suficiente retreina a partir da melhor solução
        :param: enxame_atual: enxame atual que será substituido
        :param: dados: dados para avaliar a acuracia dos modelos armazenados
        :param: lags: quantidade de lags para modelar os dados de entrada da rede
        :return: retorna o melhor enxame para os dados passados
        '''
        
        particao = Particionar_series(dados, [1, 0, 0], lags)
        [dados_x, dados_y] = particao.Part_train()
        
        print("Quantidade de dados para treinamento: ", len(dados_y))
        
        acuracias = []
        if(self.qtd_memoria != 0):
            for i in self.vetor_ambientes:
                previsao = i.gbest.Predizer(dados_x)
                acuracias.append(mean_absolute_error(dados_y, previsao))
            print("Acuracias: ", acuracias)
            
            previsao = enxame_atual.Predizer(dados_x)
            erro_atual = mean_absolute_error(dados_y, previsao)
            print("Acuracia do modelo atual: ", erro_atual)
            
            j = np.argmin(acuracias)
            print("Acuracia do melhor modelo da memória: ", erro_atual)
            
            if(acuracias[j] < erro_atual):
                print("Melhor solução encontrada na memória [", j, "]: ", acuracias[j])
                enxame_atual.particulas = self.vetor_ambientes[j].particulas.copy()
                enxame_atual.best_elm = self.vetor_ambientes[j].gbest
                print("Comparacao modelos: ", enxame_atual.best_elm == self.vetor_ambientes[j].gbest)
                return enxame_atual
            
            else:
                
                # caso não tenha um melhor verificar as partículas
                best_model = self.Avaliar_particulas(enxame_atual, dados, lags)
                enxame_atual.Atualizar_bestmodel(best_model)
                
                # retorna a melhor solucao
                return enxame_atual
            
        else:
            print("memoria zerada.")
    
    def Avaliar_particulas(self, enxame_atual, dados, lags):
        '''
        metodo para avaliar cada particula para um determinado conceito, retorna a melhor particula
        :param: enxame_atual: enxame atual que será substituido
        :param: dados: dados para avaliar a acuracia dos modelos armazenados
        :param: lags: quantidade de lags para modelar os dados de entrada da rede
        :return: retorna a melhor particula para o determinado conceito
        '''
        
        particao = Particionar_series(dados, [1, 0, 0], lags)
        [dados_x, dados_y] = particao.Part_train()
        
        #print("Quantidade de dados para treinamento: ", len(dados_y))
        
        acuracias = []
        for i in range(len(enxame_atual.sensores)):
            previsao = enxame_atual.Predizer(dados_x, i)
            erro = mean_absolute_error(dados_y, previsao)
            #print("Sensor [", i, "]:", erro)
            acuracias.append(erro)
            
            
        j = np.argmin(acuracias)
        #print("Melhor particula: [",j,"]: ", acuracias[j])

        '''
        sequencia = range(0, len(acuracias))
        plt.bar(sequencia, acuracias, 0.6, align='center', color = 'Blue', label = "Partículas - MAE")
        plt.ylabel('MAE')
        plt.xlabel('Partículas')
        plt.xticks(range(len(acuracias)))
        limiar = min(acuracias) * 0.0005
        plt.axis([-1, len(acuracias), min(acuracias) - limiar, max(acuracias) + limiar])
        plt.legend()
        plt.show()
        '''
        
        return enxame_atual.sensores[j]
            
def main():
    
    #importando o dataset
    dtst = Datasets()
    serie = dtst.Leitura_dados(dtst.bases_linear_graduais(3), csv=True)
    particao = Particionar_series(serie, [0.0, 0.0, 0.0], 0)
    serie = particao.Normalizar(serie)

    # instanciando a memoria
    memoria = LTM(2, 0.5, 0.1)

    # criando o primeiro modelo
    serie1 = serie[:500]
    enxame1 = IDPSO_ELM(serie1, [0.8, 0.2, 0], 5, 10)
    enxame1.Treinar() 
    memoria.Avaliar_particulas(enxame1, serie1, 5)
    
    # criando o primeiro ambiente
    ambiente1 = Ambiente(enxame1.particulas, enxame1.best_elm)
    memoria.Adicionar_ambiente(ambiente1)
    
    # criando o segundo modelo
    serie2 = serie[500:1000]
    enxame2 = IDPSO_ELM(serie2, [0.8, 0.2, 0], 5, 10)
    enxame2.Treinar() 
    
    # criando o segundo ambiente
    ambiente2 = Ambiente(enxame2.particulas, enxame2.best_elm)
    memoria.Adicionar_ambiente(ambiente2)
    
    # criando o segundo modelo
    serie3 = serie[1000:1500]
    enxame3 = IDPSO_ELM(serie3, [0.8, 0.2, 0], 5, 10)
    enxame3.Treinar() 
    
    # criando o segundo ambiente
    ambiente3 = Ambiente(enxame3.particulas, enxame3.best_elm)
    memoria.Adicionar_ambiente(ambiente3)
    
    # relembrando um modelo passado
    serie4 = serie[1500:2000]
    enxame3 = memoria.Relembrar_ambiente(enxame3, serie4, 5)
    
    # criando o segundo modelo
    serie5 = serie[2000:2500]
    enxame4 = IDPSO_ELM(serie5, [0.8, 0.2, 0], 5, 10)
    enxame4.Treinar() 
        
    # avaliando as particulas para um determinado conceito, atualiza o gbest se tiver uma particula melhor
    serie6 = serie[2500:3000]
    particao = Particionar_series(serie6, [1, 0, 0], 5)
    [dados_x, dados_y] = particao.Part_train()
    
    memoria.Avaliar_particulas(enxame1, serie6, 5)
    previsao = enxame1.Predizer(dados_x)
    mae = mean_absolute_error(dados_y, previsao)
    print("\ngbest anterior - mae: ", mae)
    
    
    best_model = memoria.Avaliar_particulas(enxame1, serie6, 5)
    enxame1.Atualizar_bestmodel(best_model)
    previsao = enxame1.Predizer(dados_x)
    mae = mean_absolute_error(dados_y, previsao)
    print("gbest posterior - mae: ", mae)
    
if __name__ == "__main__":
    main()