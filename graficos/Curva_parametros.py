# -*- coding: utf-8 -*-
'''
Created on 24 de abr de 2017

@author: gusta
'''

import matplotlib.pyplot as plt

class Curva():
    def __init__(self):
        pass
    
    def Curvas_artificiais(self):
        
        ##########################################PARAMETROS####################################################################
        plt.style.use('seaborn-colorblind')
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
            #plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
            plt.text(fa_ecdd[i], atrasos_ecdd[i], param_ecdd[i], fontsize=tamanho_fonte)
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
        #plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[3], atrasos_ddm[3]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_ddm)):
            #plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
            plt.text(fa_ddm[i], atrasos_ddm[i], param_ddm[i], fontsize=tamanho_fonte)
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
            #plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
            plt.text(fa_fedd[i], atrasos_fedd[i], param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [2266.516667,    2585.861111, 2930.522222, 2806.627778]
        fa_c = [48.38333333, 46.32777778, 44.59444444, 44.06111111]
        mae_c = [0.02891793, 0.029314347, 0.029180261, 0.029531332]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[3], atrasos_c[3]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_c)):
            #plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
            plt.text(fa_c[i], atrasos_c[i], param_c[i], fontsize=tamanho_fonte)
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
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i], param_s[i], fontsize=tamanho_fonte)
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
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i], param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ########################################IDPSO-ELM-BS################################################################################
        tecnica = 'IDPSO-ELM-BS'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [3300.983333, 4558.144444, 6336.527778, 7589.072222]
        fa_s = [36.7, 18.67777778, 7.894444444, 4.133333333]
        mae_s = [0.02920959, 0.030868713, 0.033275474, 0.033354695]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[1], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[1], label = tecnica + " (30)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[1], atrasos_s[1]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i], param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.tick_params(labelsize= 12)
        plt.xlabel('FPR', fontsize= 18)
        plt.ylabel('DD', fontsize=18)
        plt.legend(prop={'size':20})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
     
    def Curvas_reais_retorno(self):
        
        ##########################################PARAMETROS####################################################################
        plt.style.use('seaborn-colorblind')
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
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [1427, 1427.2, 1427, 1427.4]
        fa_ddm = [20.5, 20.5, 20.5, 20.5]
        mae_ddm = [0.077636648, 0.078354139, 0.077585075, 0.078413828]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha)
        #plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[3], atrasos_ddm[3]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_ddm)):
            #plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
            plt.text(fa_ddm[i], atrasos_ddm[i], param_ddm[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        atrasos_ecdd = [2554.1, 2409, 2878, 2738.3]
        fa_ecdd = [6.3, 3.2, 2.2, 1.3]
        mae_ecdd = [0.079852352, 0.080202888, 0.078717792, 0.079262183]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[2], atrasos_ecdd[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_ecdd)):
            #plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
            plt.text(fa_ecdd[i], atrasos_ecdd[i], param_ecdd[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-FEDD-#############################################################
        tecnica = 'ELM-FEDD'
        param_fedd = ['0', '0.25', '0.5', '0.75']
        atrasos_fedd = [1526, 1539.5, 1434, 1354]
        fa_fedd = [14.5, 12.5, 10, 10]
        mae_fedd = [0.080918646, 0.075270519, 0.075328739, 0.079564221]
        val_min = min(mae_fedd)
        i = mae_fedd.index(val_min)
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_fedd[1], atrasos_fedd[1]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_fedd)):
            #plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
            plt.text(fa_fedd[i], atrasos_fedd[i], param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [1383.9, 1619.7, 1391, 1988.8]
        fa_c = [18.4, 16, 17.2, 12.1]
        mae_c = [0.077049082, 0.076900506, 0.076874745, 0.077074913]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[3], atrasos_c[3]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_c)):
            #plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
            plt.text(fa_c[i], atrasos_c[i], param_c[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
    
    
        ########################################IDPSO-ELM-S################################################################################
        tecnica = 'IDPSO-ELM-S'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [2598.3, 2633.1, 2685.1, 2501]
        fa_s = [6.3, 3.9, 2.3, 1.3]
        mae_s = [0.078745753, 0.079117638, 0.079713358, 0.079243647]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i], param_s[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
        
        ########################################IDPSO-ELM-SV################################################################################
        tecnica = 'IDPSO-ELM-SV'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [2554.7, 2550.2, 2523.6, 2771.2]
        fa_s = [6.4, 3.7, 2.5, 1.4]
        mae_s = [0.078424746, 0.079857477, 0.078821922, 0.077905909]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s,  atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i], param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.tick_params(labelsize= 12)
        plt.xlabel('FPR', fontsize= 18)
        plt.ylabel('DD', fontsize=18)
        plt.legend(prop={'size':20})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
     
    def Curvas_reais_sem_retorno(self):
        
        ##########################################PARAMETROS####################################################################
        plt.style.use('seaborn-colorblind')
        cores = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black']
        pontos = ['bo', 'bs', 'g^']
        line = ['-', '--', '-.', ':', 'steps']
        best = 'red'
        tradeoff = 'yellow'
        tamanho_linha = 3
        tamanho_pontos = 9
        tamanho_fonte = 14
        ########################################################################################################################
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [1427, 1417.3, 1427.3, 1427.3]
        fa_ddm = [20.5,	20.5,	20.5,	20.5]
        mae_ddm = [0.076821801,    0.076198098,    0.077317944,    0.077175539]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha)
        #plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[3], atrasos_ddm[3]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_ddm)):
            #plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
            plt.text(fa_ddm[i], atrasos_ddm[i], param_ddm[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        atrasos_ecdd = [2581.8,    2396,    2939.5,    2600.6]
        fa_ecdd = [6.1,    4.1 ,   2.3,    1.1]
        mae_ecdd = [0.078027526 ,   0.079514301 ,   0.077742793 ,   0.077883681]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[2], atrasos_ecdd[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_ecdd)):
            #plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
            plt.text(fa_ecdd[i], atrasos_ecdd[i], param_ecdd[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-FEDD-#############################################################
        tecnica = 'ELM-FEDD'
        param_fedd = ['0', '0.25', '0.5', '0.75']
        atrasos_fedd = [1406,    1522  ,  1555.5  ,  1547]
        fa_fedd = [20.5 ,   12.5 ,   10  ,  10]
        mae_fedd = [0.077603901   , 0.07706868    ,0.080130241   , 0.079110156]
        val_min = min(mae_fedd)
        i = mae_fedd.index(val_min)
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_fedd[1], atrasos_fedd[1]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_fedd)):
            #plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
            plt.text(fa_fedd[i], atrasos_fedd[i], param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [1424.4 ,   1650.9   , 1662.2  ,  1896.5]
        fa_c = [18.6  ,  15.6 ,   15.2   , 12.3]
        mae_c = [0.076878304   , 0.07670269 ,   0.076194194 ,   0.076027264]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[3], atrasos_c[3]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_c)):
            #plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
            plt.text(fa_c[i], atrasos_c[i], param_c[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
    
    
        ########################################IDPSO-ELM-S################################################################################
        tecnica = 'IDPSO-ELM-S'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [2531.2,    2594.6 ,   2258.1 ,   2415.8]
        fa_s = [5.9  ,  4.7    ,2.9  ,  1.4]
        mae_s = [0.076838734  ,  0.07857794 ,   0.078153695,    0.077629799]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i], param_s[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
        
        ########################################IDPSO-ELM-SV################################################################################
        tecnica = 'IDPSO-ELM-SV'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [2541.4,    2517.2,    2557,    2417.8]
        fa_s = [6.6 ,   4.4 ,   2.7,    1.1]
        mae_s = [0.077361133,    0.079265926 ,   0.077058479   , 0.077610601]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s,  atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i], param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.tick_params(labelsize= 12)
        plt.xlabel('FPR', fontsize= 18)
        plt.ylabel('DD', fontsize=18)
        plt.legend(prop={'size':20})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
    
    def Curvas_down(self):
        
        ##########################################PARAMETROS####################################################################
        plt.style.use('seaborn-colorblind')
        cores = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black']
        pontos = ['bo', 'bs', 'g^']
        line = ['-', '--', '-.', ':', 'steps']
        best = 'red'
        tradeoff = 'yellow'
        tamanho_linha = 3
        tamanho_pontos = 7
        tamanho_tradeoff = 6
        tamanho_fonte = 11
        sob_ponto = 7
        sob_triang = 2
        ########################################################################################################################
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [280, 259.8, 280, 280]
        fa_ddm = [4, 4, 4, 4]
        mae_ddm = [0.125988124, 0.124289217, 0.125488219, 0.126176397]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha)
        #plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[3], atrasos_ddm[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_ddm)):
            #plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
            plt.text(fa_ddm[i], atrasos_ddm[i]+sob_ponto, param_ddm[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        atrasos_ecdd = [160, 159.6, 182.2, 206]
        fa_ecdd = [3, 2.4, 1.4, 0.4]
        mae_ecdd = [0.126833656, 0.129458812, 0.128195155, 0.128505665]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[3], atrasos_ecdd[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_ecdd)):
            #plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
            plt.text(fa_ecdd[i], atrasos_ecdd[i]+sob_ponto, param_ecdd[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-FEDD-#############################################################
        tecnica = 'ELM-FEDD'
        param_fedd = ['0', '0.25', '0.5', '0.75']
        atrasos_fedd = [277, 266, 297, 442]
        fa_fedd = [4, 2, 1, 0]
        mae_fedd = [0.126266926, 0.126961018, 0.130510675, 0.131338004]
        val_min = min(mae_fedd)
        i = mae_fedd.index(val_min)
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_fedd[2], atrasos_fedd[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_fedd)):
            #plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
            plt.text(fa_fedd[i], atrasos_fedd[i]+sob_ponto, param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [207.6, 220.4, 226.2, 131.6]
        fa_c = [2.8, 2.6, 2.8, 2.8]
        mae_c = [0.126591861, 0.126933389, 0.125852652, 0.125665292]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[1], atrasos_c[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_c)):
            #plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
            plt.text(fa_c[i], atrasos_c[i]+sob_ponto, param_c[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
    
    
        ########################################IDPSO-ELM-S################################################################################
        tecnica = 'IDPSO-ELM-S'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [101.4, 139, 170.2, 238]
        fa_s = [3, 2.4, 1, 0.8]
        mae_s = [0.126490403, 0.129522167, 0.129437949, 0.128949631]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
        
        ########################################IDPSO-ELM-SV################################################################################
        tecnica = 'IDPSO-ELM-SV'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [121, 139, 109.2, 243]
        fa_s = [3, 2.4, 0.8, 0.6]
        mae_s = [0.127251584, 0.130200142, 0.127329709, 0.129419864]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s,   atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.tick_params(labelsize= 12)
        plt.xlabel('FPR', fontsize= 18)
        plt.ylabel('DD', fontsize=18)
        plt.legend(prop={'size':15})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
    
    def Curvas_sp(self):
        
        ##########################################PARAMETROS####################################################################
        plt.style.use('seaborn-colorblind')
        cores = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black']
        pontos = ['bo', 'bs', 'g^']
        line = ['-', '--', '-.', ':', 'steps']
        best = 'red'
        tradeoff = 'yellow'
        tamanho_linha = 3
        tamanho_pontos = 7
        tamanho_tradeoff = 6
        tamanho_fonte = 11
        sob_ponto = 50
        sob_triang = 25
        ########################################################################################################################
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [2574, 2574.8, 2574.6, 2574.6]
        fa_ddm = [37, 37, 37, 37]
        mae_ddm = [0.027655478, 0.028106978, 0.029147668, 0.028174681]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha)
        #plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[3], atrasos_ddm[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_ddm)):
            #plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
            plt.text(fa_ddm[i], atrasos_ddm[i]+sob_ponto, param_ddm[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        atrasos_ecdd = [5003.6, 4632.4, 5696.8, 4995.2]
        fa_ecdd = [9.2, 5.8, 3.2, 1.8]
        mae_ecdd = [0.029221395, 0.029569791, 0.027290432, 0.027261696]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[3], atrasos_ecdd[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_ecdd)):
            #plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
            plt.text(fa_ecdd[i], atrasos_ecdd[i]+sob_ponto, param_ecdd[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-FEDD-#############################################################
        tecnica = 'ELM-FEDD'
        param_fedd = ['0', '0.25', '0.5', '0.75']
        atrasos_fedd = [2535, 2778, 2814, 2652]
        fa_fedd = [37, 23, 19, 20]
        mae_fedd = [0.028940876, 0.027176342, 0.029749807, 0.026882308]
        val_min = min(mae_fedd)
        i = mae_fedd.index(val_min)
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_fedd[2], atrasos_fedd[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_fedd)):
            #plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
            plt.text(fa_fedd[i], atrasos_fedd[i]+sob_ponto, param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [2641.2, 3081.4, 3098.2, 3661.4]
        fa_c = [34.4, 28.6, 27.6, 21.8]
        mae_c = [0.027164746, 0.026471992, 0.026535736, 0.026389236]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[3], atrasos_c[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_c)):
            #plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
            plt.text(fa_c[i], atrasos_c[i]+sob_ponto, param_c[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
    
    
        ########################################IDPSO-ELM-S################################################################################
        tecnica = 'IDPSO-ELM-S'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [4961, 5050.2, 4346, 4593.6]
        fa_s = [8.8, 7, 4.8, 2]
        mae_s = [0.027187065, 0.027633713, 0.026869441, 0.026309967]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
        
        ########################################IDPSO-ELM-SV################################################################################
        tecnica = 'IDPSO-ELM-SV'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [4961.8, 4895.4, 5004.8, 4592.6]
        fa_s = [10.2, 6.4, 4.6, 1.6]
        mae_s = [0.027470683, 0.02833171, 0.026787249, 0.025801338]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s,   atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[3], atrasos_s[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.tick_params(labelsize= 12)
        plt.xlabel('FPR', fontsize= 18)
        plt.ylabel('DD', fontsize=18)
        plt.legend(prop={'size':15})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
     
    def Tempo_execucao(self):
        '''
        método para plotar o tempo de execução dos algoritmos para as series reais financeiras
        '''
        
        plt.style.use('seaborn-darkgrid')
        
        algoritmos = ["ELM",  "ELM-DDM",  "ELM-ECDD",  "ELM-FEDD",  "IDPSO-ELM-B",  "IDPSO-ELM-S",  "IDPSO-ELM-SV",  "P-IDPSO-ELM-SV",  "M-IDPSO-ELM-SV", "RPSO-ELM", "RPSO"]
        tempo = [1.258838492,  3.344348126,  1.670341359,  17.08783947,  12.66821589,  13.56126097,  13.76836696,  20.26134007,  23.8165871, 17.42857175,  167.1866382]
        
        colors = ['blue'] * len(tempo)
        
        sequencia = range(0, len(tempo))
        barras = plt.bar(sequencia, tempo, 0.6, align='center', color = colors)
        plt.title('Time of run')
        plt.ylabel('Seconds')
        plt.xlabel('Algorithms')
        plt.xticks(range(len(tempo)))

        limiar = min(tempo) * 15
        plt.axis([-1, len(tempo), min(tempo) - (limiar/20), max(tempo) + (2*limiar)])
        
        rects = barras.patches
        
        # Now make some labels
        for i in range(len(algoritmos)):
            height = rects[i].get_height()
            plt.text(rects[i].get_x() + rects[i].get_width()/2, height+(limiar/2), algoritmos[i], ha='center', va='bottom', rotation='vertical')
                  
        plt.legend()
        plt.show()
        
def main():
    
    c = Curva()
    #c.Curvas_artificiais()
    #c.Curvas_reais_retorno()
    #c.Curvas_reais_retorno()
    #c.Curvas_reais_sem_retorno()
    #c.Curvas_down()
    #c.Curvas_sp()
    
    c.Tempo_execucao()
    
if __name__ == "__main__":
    main()
    
    
    