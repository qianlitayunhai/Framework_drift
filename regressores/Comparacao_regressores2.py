#-*- coding: utf-8 -*-

'''
Created on 27 de set de 2017

@author: gusta
'''

import matplotlib.pyplot as plt
from ferramentas.Particionar_series import Particionar_series
from regressores.ELM import ELMRegressor
from regressores.IDPSO_ELM import IDPSO_ELM
from regressores.PSO_SLFN import PSO_SLFN
from regressores.PSO_ELM import PSO_ELM
from sklearn.metrics.regression import mean_absolute_error
from ferramentas.Importar_dataset import Datasets
import numpy as np


#load da serie
dtst = Datasets('dentro')
serie = dtst.Leitura_dados(dtst.bases_reais(2), csv=True)
particao = Particionar_series(serie, [0.0, 0.0, 0.0], 0)
serie = particao.Normalizar(serie)
serie = serie[5000:6500]

# configuracoes basicas para treinamento
divisao_dataset = [0.6, 0.2, 0.2]
qtd_neuronis = 10
janela_tempo = 5
particulas = 30
it = 100
c1 = 2
c2 = 2
crit = 2

# otimizacao de parametros
xmax = [0.3, 0.6, 0.8, 1, 2]
inercia_inicial = [1.2, 1, 0.8, 0.6]
inercia_final = [1.2, 1, 0.8, 0.6, 0.5, 0.4, 0.3, 0.2]


# salvar os melhores parametros
erro_best = 999999
xmax_best = 0
inercia_inicial_best = 0
inercia_final_best = 0
cont = 0

for i in range(len(xmax)):
    for j in range(len(inercia_inicial)):
        for k in range(len(inercia_final)):

            MAE_list = []
            
            for z in range(10):
                # instanciando o método IDPSO-ELM
                idpso_elm = IDPSO_ELM(serie, divisao_dataset, janela_tempo, qtd_neuronis)
                idpso_elm.Parametros_IDPSO(it, particulas, inercia_inicial[j], inercia_final[k], c1, c2, xmax[i], crit)
                idpso_elm.Treinar()  
                
                # organizando os dados para comparacao #
                train_x, train_y = idpso_elm.dataset[0], idpso_elm.dataset[1] 
                val_x, val_y = idpso_elm.dataset[2], idpso_elm.dataset[3]
                test_x, test_y = idpso_elm.dataset[4], idpso_elm.dataset[5]
                
                ################################## computando a previsao para o conjunto de validacao ################################
                previsao = idpso_elm.Predizer(val_x)
                MAE = mean_absolute_error(val_y, previsao)
                MAE_list.append(MAE)
            
            cont += 1
            media = np.mean(MAE_list)
            print(cont, 'Media MAE: ', MAE)
            
            if(erro_best > media):
                erro_best = MAE
                xmax_best = i
                inercia_inicial_best = j
                inercia_final_best = k
            ###################################################################################


print("Erro best: ", erro_best)
print("Xmax: ", xmax[xmax_best])
print("Inercia inicial: ", inercia_inicial[inercia_inicial_best])
print("Inercia final: ", inercia_final[inercia_final_best])


