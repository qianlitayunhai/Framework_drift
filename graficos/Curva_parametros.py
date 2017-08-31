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
        tamanho_fonte = 14
        af_dd = 100
        af_fa = 0
        ########################################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        #atrasos_ecdd = [1955.511111, 2989.1, 4770.411111, 6885.594444]
        atrasos_ecdd = [1855.4,    2839.194444,    4085.288889,    6217.377778]
        fa_ecdd = [49.53888889, 30.66666667, 16.63333333, 9.588888889]
        mae_ecdd = [0.092576456, 0.044029671, 0.069903868, 0.049410685]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[2], atrasos_ecdd[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_ecdd)):
            plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [1293.422222, 1643.022222, 2519.25, 4727.933333]
        fa_ddm = [56.86111111, 54.81666667, 42.54444444, 19.57222222]
        mae_ddm = [0.052047807, 0.046565159, 0.045854402, 0.042699195]
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
        atrasos_fedd = [1308.266667, 4546.622222, 6611.566667, 8080.877778]
        fa_fedd = [56.65, 10.42222222, 5.05, 3.505555556]
        mae_fedd = [0.043551024, 0.065050726, 0.078407112, 0.094179621]
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
        atrasos_c = [1195, 1195, 1195, 1195]
        fa_c = [57, 57, 57, 57]
        mae_c = [0.031068499, 0.032032684, 0.030175617, 0.031561158]
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
        atrasos_s = [1955.511111, 2989.1, 4770.411111, 6885.594444]
        fa_s = [47.17777778, 24.78888889, 11.58888889, 5.116666667]
        mae_s = [0.029595375, 0.030660853, 0.032411644, 0.033898074]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        #for i in range(len(param_s)):
        #    plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
        
        ########################################IDPSO-ELM-SV################################################################################
        tecnica = 'IDPSO-ELM-SV'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1647.455556, 2551.083333, 4341.933333, 6426.961111]
        fa_s = [48.95, 26.51666667, 12.96666667, 6.411111111]
        mae_s = [0.029575598, 0.031889836, 0.032587299, 0.032511621]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        #for i in range(len(param_s)):
        #    plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ########################################IDPSO-ELM-BS################################################################################
        tecnica = 'IDPSO-ELM-BS'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1857.072222, 2689.566667, 4866.527778, 6948.788889]
        fa_s = [47.42777778, 25.02777778, 11.64444444, 5.238888889]
        mae_s = [0.030215641, 0.031272762, 0.03195898, 0.03176229]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[1], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[1], label = tecnica + " (30)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_s)):
            plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.tick_params(labelsize= 12)
        plt.xlabel('FPR', fontsize= 18)
        plt.ylabel('DD', fontsize=18)
        plt.legend(prop={'size':20})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
         
def main():
    
    c = Curva()
    c.Curvas_ICTAI()
    
    
if __name__ == "__main__":
    main()
    
    
    