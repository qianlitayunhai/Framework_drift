#-*- coding: utf-8 -*-
'''
Created on 6 de fev de 2017

@author: gusta
'''
from ferramentas.Janela_deslizante import Janela
from ferramentas.Importar_dataset import Datasets
from ferramentas.Particionar_series import Particionar_series
from metricas.Metricas_deteccao import Metricas_deteccao
from otimizador.IDPSO import IDPSO_ELM
from detectores.S import S
from graficos.Graficos_execucao import Grafico
from sklearn.metrics.regression import mean_absolute_error
import time

#parametros IDPSO
it = 50
inercia_inicial = 0.8
inercia_final = 0.4
c1 = 2
c2 = 2
crit_parada = 2


class Algoritmo_sensores():
    def __init__(self, dataset, n, lags, qtd_neuronios, numero_particulas, qtd_sensores, c):
        '''
        construtor do algoritmo que detecta a mudanca de ambiente por meio de sensores
        :param dataset: serie temporal que o algoritmo vai executar
        :param qtd_train_inicial: quantidade de exemplos para o treinamento inicial
        :param tamanho_janela: tamanho da janela de caracteristicas para identificar a mudanca
        :param n: tamanho do n para reavaliar o metodo de deteccao
        :param lags: quantidade de lags para modelar as entradas da RNA
        :param qtd_neuronios: quantidade de neuronios escondidos da RNA
        :param numero_particulas: numero de particulas para serem usadas no IDPSO
        :param qtd_sensores: quantidade de sensores utilizados para detectar uma mudanca de conceito
        '''
        
        self.dataset = dataset
        self.n = n
        self.lags = lags
        self.qtd_neuronios = qtd_neuronios
        self.numero_particulas = numero_particulas
        self.qtd_sensores = qtd_sensores
        
        self.c = c
        
    def Executar(self, grafico = None):
        '''
        Metodo para executar o procedimento do algoritmo
        :param grafico: variavel booleana para ativar ou desativar o grafico
        :return: retorna 5 variaveis: [falsos_alarmes, atrasos, falta_deteccao, MAPE, tempo_execucao]
        '''
        
        ################################################################################################################################################
        ################################# CONFIGURACAO DO DATASET ######################################################################################
        ################################################################################################################################################
        
        #dividindo os dados da dataset dinamica para treinamento_inicial inicial e para uso do stream dinâmico
        treinamento_inicial = self.dataset[0:self.n]
        stream = self.dataset[self.n:]
    
        ################################################################################################################################################
        ################################# PERIODO ESTATICO #############################################################################################
        ################################################################################################################################################
        
        #criando e treinando um modelo_vigente para realizar as previsões
        enxame = IDPSO_ELM(treinamento_inicial, [1, 0, 0], self.lags, self.qtd_neuronios)
        enxame.Parametros_IDPSO(it, self.numero_particulas, inercia_inicial, inercia_final, c1, c2, crit_parada)
        enxame.Treinar()  
       
        #ajustando com os dados finais do treinamento a janela de predicao
        janela_predicao = Janela()
        janela_predicao.Ajustar(enxame.dataset[0][(len(enxame.dataset[0])-1):])
        predicao = enxame.Predizer(janela_predicao.dados)
        
        #janela com o atual conceito, tambem utilizada para armazenar os dados de retreinamento
        janela_caracteristicas = Janela()
        janela_caracteristicas.Ajustar(treinamento_inicial)
    
        #ativando os sensores de acordo com a primeira janela de caracteristicas
        s = S(self.qtd_sensores, self.c)
        s.armazenar_conceito(janela_caracteristicas.dados, self.lags, enxame)
            
        ################################################################################################################################################
        ################################# PERIODO DINAMICO #############################################################################################
        ################################################################################################################################################
        
        #variavel para armazenar o erro do stream
        erro_stream = 0
        #variavel para armazenar as deteccoes
        deteccoes = []
        #variavel para armazenar os alarmes
        alarmes = []
        #variavel para armazenar o tempo inicial
        start_time = time.time()
        
        #vetor para armazenar a predicoes_vetor
        if(grafico == True):
            predicoes_vetor = [None] * len(stream)
            erro_stream_vetor = [None] * len(stream)
            
        #variavel auxiliar 
        mudanca_ocorreu = False
        
        #entrando no stream de dados
        for i in range(1, len(stream)):
            
            
            #computando o erro
            loss = mean_absolute_error(stream[i:i+1], predicao)
            erro_stream += loss
    
            #adicionando o novo dado a janela de predicao
            janela_predicao.Fila_Add(stream[i])
                
            #realizando a nova predicao com a nova janela de predicao
            predicao = enxame.Predizer(janela_predicao.dados)
            
            if(grafico == True):                
                #salvando o erro 
                erro_stream_vetor[i] = loss
                #salvando a predicao
                predicoes_vetor[i] = predicao
            
            if(mudanca_ocorreu == False):
                
                #verificando os sensores
                mudou = s.monitorar(loss, i, True)
                
                if(mudou == True):
                    if(grafico == True):    
                        print("[%d] Detectou uma mudança" % (i))
                    deteccoes.append(i)
                    
                    #zerando a janela de treinamento
                    janela_caracteristicas.Zerar_Janela()
                
                    #variavel para alterar o fluxo, ir para o periodo de retreinamento
                    mudanca_ocorreu = True
                    
            else:
                
                if(len(janela_caracteristicas.dados) < self.n):
                    
                    #adicionando a nova instancia na janela de caracteristicas
                    janela_caracteristicas.Increment_Add(stream[i])
                    
                else:
                
                    #atualizando o modelo_vigente preditivo
                    enxame = IDPSO_ELM(janela_caracteristicas.dados, [1, 0, 0], self.lags, self.qtd_neuronios)
                    enxame.Parametros_IDPSO(it, self.numero_particulas, inercia_inicial, inercia_final, c1, c2, crit_parada)
                    enxame.Treinar() 
                    
                    janela_predicao = Janela()
                    janela_predicao.Ajustar(enxame.dataset[0][(len(enxame.dataset[0])-1):])
                    predicao = enxame.Predizer(janela_predicao.dados)
                    
                    #ativando os sensores de acordo com a primeira janela de caracteristicas
                    s = S(self.qtd_sensores, self.c)
                    s.armazenar_conceito(janela_caracteristicas.dados, self.lags, enxame)
                    
                    #variavel para voltar para o loop principal
                    mudanca_ocorreu = False
        
        #variavel para armazenar o tempo final
        end_time = time.time()
        
        #computando as metricas de deteccao
        mt = Metricas_deteccao()
        #[falsos_alarmes, atrasos] = mt.resultados_dow_drift(deteccoes, self.n)
        [falsos_alarmes, atrasos] = mt.resultados(deteccoes, self.n)
        
        #computando a acuracia da previsao ao longo do fluxo de dados
        MAE = erro_stream/len(stream)
        
        #computando o tempo de execucao
        tempo_execucao = (end_time-start_time)
        
        if(grafico == True):
            tecnica = "IDPSO_ELM_SV"
            print(tecnica)
            print("Alarmes:")
            print(alarmes)
            print("Deteccoes:")
            print(deteccoes)
            print("Falsos Alarmes: ", falsos_alarmes)
            print("Atrasos: ", atrasos)
            print("MAE: ", MAE)
            print("Tempo de execucao: ", tempo_execucao)
        
        #plotando o grafico de erro
        if(grafico == True):
            g = Grafico()
            #g.Plotar_graficos_dow_drift(stream, predicoes_vetor, deteccoes, alarmes, erro_stream_vetor, self.n, atrasos, falsos_alarmes, tempo_execucao, MAE, nome=tecnica)
            g.Plotar_graficos_cnt(stream, predicoes_vetor, deteccoes, alarmes, erro_stream_vetor, self.n, atrasos, falsos_alarmes, tempo_execucao, MAE, nome=tecnica)
                           
        #retorno do metodo
        return falsos_alarmes, atrasos, MAE, tempo_execucao
    
def main():
    
    #instanciando o dataset
    dtst = Datasets()
    dataset = dtst.Leitura_dados(dtst.bases_lineares(10), csv=True)
    #dataset = dtst.Leitura_dados(dtst.bases_reais(4), csv=True)
    particao = Particionar_series(dataset, [0.0, 0.0, 0.0], 0)
    dataset = particao.Normalizar(dataset)
        
    #instanciando o algoritmo com sensores
    #dataset, qtd_train_inicial, tamanho_janela, passo, lagnd_neuronios, qtd_sensores
    n = 100
    lags = 5
    qtd_neuronios = 10
    numero_particulas = 30
    qtd_sensores = 30
    c = 1
    alg = Algoritmo_sensores(dataset, n, lags, qtd_neuronios, numero_particulas, qtd_sensores, c)
    
    #colhendo os resultados
    alg.Executar(grafico=True)
    
    
if __name__ == "__main__":
    main()      