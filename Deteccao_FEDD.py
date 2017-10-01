#-*- coding: utf-8 -*-
'''
Created on 13 de fev de 2017
classe para avaliar todos os metodos de deteccao nas series financeiras
@author: gusta
'''

from geradores_tabela.Tabela_excel import Tabela_excel
from ferramentas.Importar_dataset import Datasets
from ferramentas.Particionar_series import Particionar_series
from algoritmos_online.ELM_DDM import ELM_DDM
from algoritmos_online.ELM_ECDD import ELM_ECDD
from algoritmos_online.ELM_FEDD import ELM_FEDD
from algoritmos_online.IDPSO_ELM_S import IDPSO_ELM_S
from algoritmos_online.IDPSO_ELM_B import IDPSO_ELM_B
from algoritmos_online.IDPSO_ELM_SV import IDPSO_ELM_SV
from algoritmos_online.IDPSO_ELM_BS import IDPSO_ELM_BS
from experimentos.Constantes import Constantes

def printar_metricas(falsos_alarmes, atrasos, MAPE, tempo_execucao):
    print("Falsos alarmes:", falsos_alarmes)
    print("Atrasos:", atrasos)
    print("MAPE:", MAPE)
    print("Tempo:", tempo_execucao)
    print()
    
def caminho_datasets(alocacao, i, k):
    
    ###########################################instanciando o dataset#################################################################################
    dtst = Datasets(alocacao)
    
    if(i == 0):
        dataset = dtst.Leitura_dados(dtst.bases_linear_graduais(k), csv=True)
        nome_arquivo = '/Lineares-Graduais/lin-grad-' + str(k)
        return dataset, nome_arquivo
                                
    elif(i == 1):
        dataset = dtst.Leitura_dados(dtst.bases_linear_abruptas(k), csv=True)
        nome_arquivo = '/Lineares-Abruptas/lin-abt-' + str(k)
        return dataset, nome_arquivo
            
    elif(i == 2):
        dataset = dtst.Leitura_dados(dtst.bases_nlinear_graduais(k), csv=True)
        nome_arquivo = '/LinearesN-Graduais/lin_n-grad-' + str(k)
        return dataset, nome_arquivo
                              
    elif(i == 3):
        dataset = dtst.Leitura_dados(dtst.bases_nlinear_abruptas(k), csv=True)
        nome_arquivo = '/LinearesN-Abruptas/lin_n-abt-' + str(k)
        return dataset, nome_arquivo
                              
    elif(i == 4):
        dataset = dtst.Leitura_dados(dtst.bases_sazonais(k), csv=True)
        nome_arquivo = '/Sazonais/saz-' + str(k)
        return dataset, nome_arquivo
                                
    elif(i == 5):
        dataset = dtst.Leitura_dados(dtst.bases_hibridas(k), csv=True)
        nome_arquivo = '/Hibridas/hib-' + str(k)
        return dataset, nome_arquivo
            
    elif(i == 6):
        dataset = dtst.Leitura_dados(dtst.bases_reais(k), csv=True)
        if(k == 1):
            nome_arquivo = '/Reais/dow'
            return dataset, nome_arquivo
        elif(k == 2):
            nome_arquivo = '/Reais/nasdaq'
            return dataset, nome_arquivo
        elif(k == 3):
            nome_arquivo = '/Reais/SP500'
            return dataset, nome_arquivo         
    ##################################################################################################################################################
    
def main():
    '''
        metodo para rodar o experimento
    '''
    
    subpasta = ['/[1]']
    param_fedd = [0.1]
    
    ###########################################definindo informaceos referentes a pastas #################################################################################
    
    alocacao = 'fora'
    e = Constantes(alocacao)
        
    ###########################################definindo os indices das series que serão experimentadas#################################################################################
                
    vez = [5]
    variacao = range(1, 26)
                
    ####################################################################################################################################################################################
    for z in range(len(subpasta)):           
        for i in vez:
            
            for k in variacao:
                               
                ###########################################instanciando o dataset#################################################################################
                dataset, nome_arquivo = caminho_datasets(alocacao, i, k)
                ##################################################################################################################################################
                                
                ######################################## criando a tabela onde as informacoes serao armazenadas ##################################################
                #normalizando a serie
                particao = Particionar_series(dataset, [0.0, 0.0, 0.0], 0)
                dataset = particao.Normalizar(dataset)
                                    
                tabela = Tabela_excel()
                nome = e.caminho_bases + "FEDD (0.1)" + subpasta[z] + nome_arquivo
                folhas = ["ELM-FEDD"]
                cabecalho = ["falsos alarmes", "atrasos", "MAPE", "tempo execucao"]
                largura_col = 5000
                tabela.Criar_tabela(nome, folhas, cabecalho, largura_col)
                ##################################################################################################################################################
                                
                #####################instanciando as variaveis para o construtor das classes#######################################################################
                grafico = False
                n = 300
                lags = 5
                qtd_neuronios = 10
                ##################################################################################################################################################
                                
                ##############################################definindo quantas vezes cada algoritmo sera executado##############################################
                # quantidade de execucoes
                qtd_execucoes = 5
                            
                # for de execucoes
                for execucao in range(qtd_execucoes):
                    print("Reais Drifts" + subpasta[z] + nome_arquivo + " -  Execucao [%s]"  %(execucao))
    
                    ########################################### instanciando os algoritmo e escrevendo as execucoes ####################################################
                    
                    #"ELM-FEDD"
                    print(folhas[0])
                    alg = ELM_FEDD(dataset, n, lags, qtd_neuronios, 0.2, param_fedd[z], param_fedd[z])
                    [falsos_alarmes, atrasos, MAPE, tempo_execucao] = alg.Executar(grafico=grafico)
                    printar_metricas(falsos_alarmes, atrasos, MAPE, tempo_execucao)
                    tabela.Adicionar_Sheet_Linha(0, execucao, [falsos_alarmes, atrasos, MAPE, tempo_execucao])
                    
                    
                    ##################################################################################################################################################
                                        
                tabela.Calcular_Medias(qtd_execucoes)
                ##################################################################################################################################################
     
if __name__ == "__main__":
    main()

