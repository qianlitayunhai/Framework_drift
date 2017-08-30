# -*- coding: utf-8 -*-
'''
Created on 24 de abr de 2017

@author: gusta
'''

import matplotlib.pyplot as plt

class Curva():
    def __init__(self):
        pass
    
    def Curvas_ICTAI(self):
        
        ##########################################PARAMETROS####################################################################
        cores = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black']
        pontos = ['bo', 'bs', 'g^']
        line = ['-', '--', '-.', ':', 'steps']
        best = 'red'
        tradeoff = 'yellow'
        tamanho_linha = 3
        tamanho_pontos = 9
        tamanho_fonte = 18
        af_dd = 100
        af_fa = 0
        ########################################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        atrasos_ecdd = [2237.661667,    2798.418333,    4169.381667,   5375.136667]
        fa_ecdd = [43.69833333,   26.98166667,    17.61333333,    9.651666667]
        mae_ecdd = [0.055793487,    0.056384367,    0.057980822,    0.068061947,    0.067606176]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[2], atrasos_ecdd[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        ############################################################################################################
        
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['3', '5', '6', '8']
        atrasos_ddm = [1911.4,    3469.6,    4526.4,    6400.7]
        fa_ddm = [52.1,    35.3,    20.7,    7.8]
        mae_ddm = [0.0468,    0.0483,    0.0504,    0.0780]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[2], atrasos_ddm[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_ddm)):
            plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        
        ###############################################-ELM-FEDD-#############################################################
        tecnica = 'ELM-FEDD'
        param_fedd = ['0', '0.25', '0.5', '0.75']
        atrasos_fedd = [1347.108333,    4675.316667,    6790.475,    8354.65]
        fa_fedd = [56.19166667,    14.94166667,    9.541666667,    7.6]
        mae_fedd = [0.058427404,    0.083492844,    0.088153567,    0.123736945]
        val_min = min(mae_fedd)
        i = mae_fedd.index(val_min)
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_fedd[1], atrasos_fedd[1]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_fedd)):
            plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [2389.11875,    2459.185,    2640.418333,    5671.061667]
        fa_c = [46.85916667,    46.40833333,    45.59666667,    31.24]
        mae_c = [0.039836941,   0.040017313,    0.04009332,  0.043023703]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c, atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[2], atrasos_c[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_c)):
            plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
    
    
        ########################################IDPSO-ELM-S################################################################################
        tecnica = 'IDPSO-ELM-S'
        param_s = ['0.25', '0.5', '0.75', '1']
        
        ################################-1-#################################
        atrasos_s = [1939.895,    2716.105,   4011.056667,    5119.00]
        fa_s = [43.595,    26.58666667,    17.48166667,    9.10]
        mae_s = [0.041482178,    0.04362065,    0.044493041,    0.0424]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (1)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        
        ################################-30-####################################
        atrasos_s = [2037.661667,    2694.44,    4098.958333,    5106.23]
        fa_s = [43.15833333,   26.25166667,    16.605,    8.28]
        mae_s = [0.041458538,  0.044224473,  0.045264889,   0.042510248]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_s)):
            plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.tick_params(labelsize= 18)
        plt.xlabel('FPR', fontsize= 18)
        plt.ylabel('DD', fontsize=18)
        plt.legend(prop={'size':25})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
         
def main():
    
    c = Curva()
    c.Curvas_ICTAI()
    
    
if __name__ == "__main__":
    main()
    
    
    