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


#load da serie
dtst = Datasets('dentro')
serie = dtst.Leitura_dados(dtst.bases_reais(1), csv=True)
particao = Particionar_series(serie, [0.0, 0.0, 0.0], 0)
serie = particao.Normalizar(serie)
serie = serie[0:300]

# configuracoes basicas para treinamento
divisao_dataset = [0.6, 0.2, 0.2]
qtd_neuronis = 5
janela_tempo = 5

# instanciando o método IDPSO-ELM
idpso_elm = IDPSO_ELM(serie, divisao_dataset, janela_tempo, qtd_neuronis)
idpso_elm.Parametros_IDPSO(100, 30, 1, 0.8, 1.7, 2.3, 20)
idpso_elm.Treinar()  

# instanciando o método ELM
elm = ELMRegressor(qtd_neuronis)
elm.Tratamento_dados(serie, divisao_dataset, janela_tempo)
elm.Treinar(elm.train_entradas, elm.train_saidas)

# instanciando o método PSO_SLFN
pso_slfn = PSO_SLFN(serie, divisao_dataset, janela_tempo, 3)
pso_slfn.Parametros_PSO(100, 30, 0.8, 2, 2, 20, 0.25)
pso_slfn.Treinar()

# instanciando o método PSO_ELM
pso_elm = PSO_ELM(serie, divisao_dataset, janela_tempo, qtd_neuronis)
pso_elm.Parametros_PSO(100, 30, 0.8, 2, 2, 20, 0.25)
pso_elm.Treinar()

# organizando os dados para comparacao #
train_x, train_y = idpso_elm.dataset[0], idpso_elm.dataset[1] 
val_x, val_y = idpso_elm.dataset[2], idpso_elm.dataset[3]
test_x, test_y = idpso_elm.dataset[4], idpso_elm.dataset[5]



################################## computando a previsao para o conjunto de treinamento ################################

plt.plot(train_y, label = "Real")

print("\n------------------------------------------")

previsao = idpso_elm.Predizer(train_x)
MAE = mean_absolute_error(train_y, previsao)
plt.plot(previsao, label = "Previsao IDPSO-ELM: " + str(MAE))
print('IDPSO_ELM - Train MAE: ', MAE)


previsao = elm.Predizer(train_x)
MAE = mean_absolute_error(train_y, previsao)
plt.plot(previsao, label = "Previsao ELM: " + str(MAE))
print('ELM - Train MAE: ', MAE)


previsao = pso_slfn.Predizer(train_x)
MAE = mean_absolute_error(train_y, previsao)
plt.plot(previsao, label = "Previsao PSO_SLFN: " + str(MAE))
print('PSO_SLFN - Train MAE: ', MAE)


previsao = pso_elm.Predizer(train_x)
MAE = mean_absolute_error(train_y, previsao)
plt.plot(previsao, label = "Previsao PSO_ELM: " + str(MAE))
print('PSO_ELM - Train MAE: ', MAE)

print("------------------------------------------")

plt.legend()
plt.show()

###################################################################################


################################## computando a previsao para o conjunto de validacao ################################

plt.plot(val_y, label = "Real")

print("\n------------------------------------------")

previsao = idpso_elm.Predizer(val_x)
MAE = mean_absolute_error(val_y, previsao)
plt.plot(previsao, label = "Previsao IDPSO-ELM: " + str(MAE))
print('IDPSO_ELM - val MAE: ', MAE)


previsao = elm.Predizer(val_x)
MAE = mean_absolute_error(val_y, previsao)
plt.plot(previsao, label = "Previsao ELM: " + str(MAE))
print('ELM - val MAE: ', MAE)


previsao = pso_slfn.Predizer(val_x)
MAE = mean_absolute_error(val_y, previsao)
plt.plot(previsao, label = "Previsao PSO_SLFN: " + str(MAE))
print('PSO_SLFN - val MAE: ', MAE)


previsao = pso_elm.Predizer(val_x)
MAE = mean_absolute_error(val_y, previsao)
plt.plot(previsao, label = "Previsao PSO_ELM: " + str(MAE))
print('PSO_ELM - val MAE: ', MAE)

print("------------------------------------------")

plt.legend()
plt.show()

###################################################################################


################################## computando a previsao para o conjunto de teste ################################

plt.plot(test_y, label = "Real")

print("\n------------------------------------------")

previsao = idpso_elm.Predizer(test_x)
MAE = mean_absolute_error(test_y, previsao)
plt.plot(previsao, label = "Previsao IDPSO-ELM: " + str(MAE))
print('IDPSO_ELM - test MAE: ', MAE)


previsao = elm.Predizer(test_x)
MAE = mean_absolute_error(test_y, previsao)
plt.plot(previsao, label = "Previsao ELM: " + str(MAE))
print('ELM - test MAE: ', MAE)


previsao = pso_slfn.Predizer(test_x)
MAE = mean_absolute_error(test_y, previsao)
plt.plot(previsao, label = "Previsao PSO_SLFN: " + str(MAE))
print('PSO_SLFN - test MAE: ', MAE)


previsao = pso_elm.Predizer(test_x)
MAE = mean_absolute_error(test_y, previsao)
plt.plot(previsao, label = "Previsao PSO_ELM: " + str(MAE))
print('PSO_ELM - test MAE: ', MAE)

print("------------------------------------------")

plt.legend()
plt.show()

###################################################################################



