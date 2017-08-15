#-*- coding: utf-8 -*-
'''
Created on 13 de fev de 2017

@author: gusta
'''

from geradores_tabela.Tabela_testes import Tabela_testes
from geradores_tabela.Tabela_excel import Tabela_excel
from ferramentas.Importar_dataset import Datasets
from ferramentas.Particionar_series import Particionar_series
from algoritmos_online.ELM_SD import ELM_SD
from algoritmos_online.ELM_DDM import ELM_DDM
from algoritmos_online.ELM_ECDD import ELM_ECDD
from algoritmos_online.ELM_FEDD import ELM_FEDD
from algoritmos_online.IDPSO_ELM_S import IDPSO_ELM_S
from algoritmos_online.IDPSO_ELM_B import IDPSO_ELM_B

def main():
    '''
        metodo para rodar o experimento
        
    '''
    
    pasta = 'Previsoes - PARAM(min)'
        
    ###########################################definindo os indices das series que serão experimentadas#################################################################################
                
    vez = [1, 2, 3, 4]
    variacao = range(1, 30)
                
    ####################################################################################################################################################################################
    dtst = Datasets()
                
    for i in vez:
        for k in variacao:
                           
            ###########################################instanciando o dataset#################################################################################
            if(i == 0):
                dataset = dtst.Leitura_dados(dtst.bases_lineares(k), csv=True)
                nome_arquivo = '/Lineares/lin-' + str(k)
                                
            elif(i == 1):
                dataset = dtst.Leitura_dados(dtst.bases_nlineares(k), csv=True)
                nome_arquivo = '/LinearesN/lin_n-' + str(k)
                                
            elif(i == 2):
                dataset = dtst.Leitura_dados(dtst.bases_sazonais(k), csv=True)
                nome_arquivo = '/Sazonais/saz-' + str(k)
                                
            elif(i == 3):
                dataset = dtst.Leitura_dados(dtst.bases_hibridas(k), csv=True)
                nome_arquivo = '/Hibridas/hib-' + str(k)
            
            elif(i == 4):
                dataset = dtst.Leitura_dados(dtst.bases_reais(k), csv=True)
                if(k == 1):
                    nome_arquivo = '/Reais/dow'
                if(k == 2):
                    nome_arquivo = '/Reais/nasdaq'
                if(k == 3):
                    nome_arquivo = '/Reais/SP500'         
            ##################################################################################################################################################
                            
            ######################################## criando a tabela onde as informacoes serao armazenadas ##################################################
                            
            #normalizando a serie
            particao = Particionar_series(dataset, [0.0, 0.0, 0.0], 0)
            dataset = particao.Normalizar(dataset)
                                
            tabela = Tabela_excel()
            nome = "../Tabelas/ZExperimentos/"+ pasta + nome_arquivo +".xls"
            folhas = ["ELM-FEDD", "ELM_DDM", "IDPSO-ELM-B", "ELM_ECDD", "IDPSO-ELM-S (1)", "IDPSO-ELM-S (30)", "ELM"]
            cabecalho = ["falsos alarmes", "atrasos", "MAPE", "tempo_execucao"]
            largura_col = 5000
            tabela.Criar_tabela(nome, folhas, cabecalho, largura_col)
            ##################################################################################################################################################
                            
            #####################instanciando as variaveis para o construtor das classes#######################################################################
            
            grafico = False
            n = 300
            lags = 5
            qtd_neuronios = 10
            numero_particulas = 30
            
            ##################################################################################################################################################
                            
            ##############################################definindo quantas vezes cada algoritmo sera executado##############################################
            
            
            qtd_execucoes = 30
                        
            for execucao in range(qtd_execucoes):
                print(nome_arquivo + " -  Execucao [%s]"  %(execucao))
                                
                ########################################### instanciando os algoritmo e escrevendo as execucoes ####################################################
                #correto:
                print("ELM_FEDD: ")
                
                w = 0.5
                c = 0.75
                alg = ELM_FEDD(dataset, n, lags, qtd_neuronios, 0.2, w, c)
                [falsos_alarmes, atrasos, MAPE, tempo_execucao] = alg.Executar(grafico=grafico)
                tabela.Adicionar_Sheet_Linha(0, execucao, [falsos_alarmes, atrasos, MAPE, tempo_execucao])
                
                print("ELM_DDM: ")
                
                w = 3
                c = 5
                
                alg = ELM_DDM(dataset, n, lags, qtd_neuronios, w, c)
                [falsos_alarmes, atrasos, MAPE, tempo_execucao] = alg.Executar(grafico=grafico)
                tabela.Adicionar_Sheet_Linha(1, execucao, [falsos_alarmes, atrasos, MAPE, tempo_execucao])
                
                print("Comportamento: ")
                
                limite = 1
                w = 0.25
                
                alg = IDPSO_ELM_B(dataset, n, lags, qtd_neuronios, numero_particulas, limite, w)
                [falsos_alarmes, atrasos, MAPE, tempo_execucao] = alg.Executar(grafico=grafico)
                tabela.Adicionar_Sheet_Linha(2, execucao, [falsos_alarmes, atrasos, MAPE, tempo_execucao])
                
                print("ELM_ECDD: ")
                
                w = 0.25
                c = 0.5
                
                alg = ELM_ECDD(dataset, n, lags, qtd_neuronios, 0.2, w, c)
                [falsos_alarmes, atrasos, MAPE, tempo_execucao] = alg.Executar(grafico=grafico)
                tabela.Adicionar_Sheet_Linha(3, execucao, [falsos_alarmes, atrasos, MAPE, tempo_execucao])
                
                print("Sensores (1): ")
                
                qtd_sensores = 1
                c = 0.25
                
                alg = IDPSO_ELM_S(dataset, n, lags, qtd_neuronios, numero_particulas, qtd_sensores, c)
                [falsos_alarmes, atrasos, MAPE, tempo_execucao] = alg.Executar(grafico=grafico)
                tabela.Adicionar_Sheet_Linha(4, execucao, [falsos_alarmes, atrasos, MAPE, tempo_execucao])
                
                print("Sensores (30): ")
                
                qtd_sensores = 30
                c = 0.25
                
                alg = IDPSO_ELM_S(dataset, n, lags, qtd_neuronios, numero_particulas, qtd_sensores, c)
                [falsos_alarmes, atrasos, MAPE, tempo_execucao] = alg.Executar(grafico=grafico)
                tabela.Adicionar_Sheet_Linha(5, execucao, [falsos_alarmes, atrasos, MAPE, tempo_execucao])
                
                print("ELM: ")
                
                limite = 1
                w = 0
                c = 0
            
                alg = ELM_SD(dataset, n, lags, qtd_neuronios)
                [falsos_alarmes, atrasos, MAPE, tempo_execucao] = alg.Executar(grafico=grafico)
                tabela.Adicionar_Sheet_Linha(6, execucao, [falsos_alarmes, atrasos, MAPE, tempo_execucao])
                
                ##################################################################################################################################################
                                    
            tabela.Calcular_Medias(qtd_execucoes)
            ##################################################################################################################################################
    
    tbt = Tabela_testes()
    tbt.Criar_tabelas()
    tbt.Calcular_estatisticas_bases()
    tbt.Gerar_tabela_final()                
       
    
if __name__ == "__main__":
    main()

