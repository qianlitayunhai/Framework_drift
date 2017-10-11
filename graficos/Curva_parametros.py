# -*- coding: utf-8 -*-
'''
Created on 24 de abr de 2017

@author: gusta
'''

import matplotlib.pyplot as plt
plt.style.use('seaborn-darkgrid')

fonte = 12
legenda = 15

class Curva():
    def __init__(self):
        pass
    
    def Curvas_artificiais_geral(self):
        
        ##########################################PARAMETROS####################################################################
        cores = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black']
        pontos = ['bo', 'bs', 'g^']
        line = ['-', '--', '-.', ':', 'steps']
        best = 'red'
        tradeoff = 'yellow'
        tamanho_linha = 4
        tamanho_pontos = 8
        tamanho_fonte = 11
        sob_ponto = 300
        sob_triang = 90
        tam_triang = 6
        alfa = 0.7
        ########################################################################################################################
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [1293.422222, 1643.022222, 2519.25, 4727.933333]
        fa_ddm = [56.86111111, 54.81666667, 42.54444444, 19.57222222]
        mae_ddm = [0.052047807, 0.046565159, 0.045854402, 0.042699195]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[3], atrasos_ddm[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ddm)):
            #plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
            plt.text(fa_ddm[i], atrasos_ddm[i]+sob_ponto, param_ddm[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        atrasos_ecdd = [1855.4,    2839.194444,    4085.288889,    6217.377778]
        fa_ecdd = [49.53888889, 30.66666667, 16.63333333, 9.588888889]
        mae_ecdd = [0.092576456, 0.044029671, 0.069903868, 0.049410685]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[2], atrasos_ecdd[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ecdd)):
            #plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
            plt.text(fa_ecdd[i], atrasos_ecdd[i]+sob_ponto, param_ecdd[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        
        ###############################################-ELM-FEDD-#############################################################
        tecnica = 'ELM-FEDD'
        param_fedd = ['0', '0.25', '0.5', '0.75']
        atrasos_fedd = [1308.266667, 4546.622222, 6611.566667, 8080.877778]
        fa_fedd = [56.65, 10.42222222, 5.05, 3.505555556]
        mae_fedd = [0.043551024, 0.065050726, 0.078407112, 0.094179621]
        val_min = min(mae_fedd)
        i = mae_fedd.index(val_min)
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_fedd[1], atrasos_fedd[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_fedd)):
            #plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
            plt.text(fa_fedd[i], atrasos_fedd[i]+sob_ponto, param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [2266.516667,    2585.861111, 2930.522222, 2806.627778]
        fa_c = [48.38333333, 46.32777778, 44.59444444, 44.06111111]
        mae_c = [0.02891793, 0.029314347, 0.029180261, 0.029531332]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[3], atrasos_c[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_c)):
            #plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
            plt.text(fa_c[i], atrasos_c[i]+sob_ponto, param_c[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
    
    
        ########################################IDPSO-ELM-S################################################################################
        tecnica = 'IDPSO-ELM-S'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1955.511111, 2989.1, 4770.411111, 6885.594444]
        fa_s = [47.17777778, 24.78888889, 11.58888889, 5.116666667]
        mae_s = [0.029595375, 0.030660853, 0.032411644, 0.033898074]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
        
        ########################################IDPSO-ELM-SV################################################################################
        tecnica = 'IDPSO-ELM-SV'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1647.455556, 2551.083333, 4341.933333, 6426.961111]
        fa_s = [48.95, 26.51666667, 12.96666667, 6.411111111]
        mae_s = [0.029575598, 0.031889836, 0.032587299, 0.032511621]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        '''
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
        plt.plot(fa_s[1], atrasos_s[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        '''
        
        ########################################IDPSO-ELM-BS################################################################################
        tecnica = 'RPSO-ELM'
        param_s = ['1', '2', '3', '4']
        atrasos_s = [8534.788889,  11521.98333,  13010.01111,  13944.02778]
        fa_s = [7.5,  3.211111111,  1.777777778,  1.305555556]
        mae_s = [0.031876795,  0.042164524,  0.05769702,  0.056671508]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[0], atrasos_s[0]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.title('Curve FPR x DD For All Artificial Time Series',  {'fontsize': legenda})
        plt.tick_params(labelsize= fonte)
        plt.xlabel('FPR', fontsize= fonte)
        plt.ylabel('DD', fontsize= fonte)
        plt.legend(prop={'size':legenda})
        plt.grid(True)
        plt.show()
        ########################################################################################################################

    def Curvas_artificiais_lin_grad(self):
        
        ##########################################PARAMETROS####################################################################
        cores = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black']
        pontos = ['bo', 'bs', 'g^']
        line = ['-', '--', '-.', ':', 'steps']
        best = 'red'
        tradeoff = 'yellow'
        tamanho_linha = 4
        tamanho_pontos = 8
        tamanho_fonte = 11
        sob_ponto = 300
        sob_triang = 90
        tam_triang = 6
        alfa = 0.7
        ########################################################################################################################
        
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [1226.266667,  1401.666667,  1663.133333,  2614.266667]
        fa_ddm = [57,  56.2,  50.06666667,  30.4]
        mae_ddm = [0.026375129,  0.021659845,  0.024224167,  0.025719345]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[3], atrasos_ddm[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ddm)):
            #plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
            plt.text(fa_ddm[i], atrasos_ddm[i]+sob_ponto, param_ddm[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        atrasos_ecdd = [1392.166667,  3191.666667,  4126.333333,  6901]
        fa_ecdd = [51.73333333,  31.56666667,  18.4,  13.16666667]
        mae_ecdd = [0.027959081,  0.030609672,  0.0236632,  0.02406365]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[3], atrasos_ecdd[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ecdd)):
            #plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
            plt.text(fa_ecdd[i], atrasos_ecdd[i]+sob_ponto, param_ecdd[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-FEDD-#############################################################
        tecnica = 'ELM-FEDD'
        param_fedd = ['0', '0.25', '0.5', '0.75']
        atrasos_fedd = [1306.866667,  4002.233333,  6705.1,  7927.133333]
        fa_fedd = [57,  9.9,  3.866666667,  2.033333333]
        mae_fedd = [0.01861672,  0.074115974,  0.071456722,  0.077775442]
        val_min = min(mae_fedd)
        i = mae_fedd.index(val_min)
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_fedd[1], atrasos_fedd[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_fedd)):
            #plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
            plt.text(fa_fedd[i], atrasos_fedd[i]+sob_ponto, param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [2084.633333,  2324.733333,  2789.4,  2760.233333]
        fa_c = [50.8,  48.53333333,  46.06666667,  45.33333333]
        mae_c = [0.014671703,  0.015049552,  0.015307541,  0.014832375]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[3], atrasos_c[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_c)):
            #plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
            plt.text(fa_c[i], atrasos_c[i]+sob_ponto, param_c[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
    
    
        ########################################IDPSO-ELM-S################################################################################
        tecnica = 'IDPSO-ELM-S'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1590.866667,  4036.366667,  5216.5,  7378]
        fa_s = [49.23333333,  22.33333333,  11.56666667,  5.9]
        mae_s = [0.014654705,  0.014928963,  0.015662123,  0.015828906]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
        
        ########################################IDPSO-ELM-SV################################################################################
        tecnica = 'IDPSO-ELM-SV'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1375.333333,  3191.666667,  5407.766667,  6901]
        fa_s = [51.13333333,  22.36666667,  12.1,  7.433333333]
        mae_s = [0.014693417,  0.014486955,  0.015518155,  0.015825129]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        '''
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
        plt.plot(fa_s[1], atrasos_s[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        '''
        
        ########################################IDPSO-ELM-BS################################################################################
        tecnica = 'RPSO-ELM'
        param_s = ['1', '2', '3', '4']
        atrasos_s = [8256.966667,  11478.2,  12545.43333,  13826.9]
        fa_s = [9.466666667,  4.433333333,  2.433333333,  1.633333333]
        mae_s = [0.016740594,  0.020397963,  0.020572842,  0.023069852]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[0], atrasos_s[0]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.title('Curve FPR x DD For Linear Gradual Time Series',  {'fontsize': legenda})
        plt.tick_params(labelsize= fonte)
        plt.xlabel('FPR', fontsize= fonte)
        plt.ylabel('DD', fontsize=fonte)
        plt.legend(prop={'size':legenda})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
    
    def Curvas_artificiais_lin_abt(self):
        
        ##########################################PARAMETROS####################################################################
        cores = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black']
        pontos = ['bo', 'bs', 'g^']
        line = ['-', '--', '-.', ':', 'steps']
        best = 'red'
        tradeoff = 'yellow'
        tamanho_linha = 4
        tamanho_pontos = 8
        tamanho_fonte = 11
        sob_ponto = 300
        sob_triang = 90
        tam_triang = 6
        alfa = 0.7
        ########################################################################################################################
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [1228.066667,  1429.666667,  1473.7,  2023.9]
        fa_ddm = [57,  56.16666667,  50.33333333,  30.56666667]
        mae_ddm = [0.017664435,  0.019432016,  0.017860761,  0.017908498]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[3], atrasos_ddm[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ddm)):
            #plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
            plt.text(fa_ddm[i], atrasos_ddm[i]+sob_ponto, param_ddm[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        atrasos_ecdd = [1464.566667,  1762.566667,  3043.4,  3809.766667]
        fa_ecdd = [47,  24.86666667,  15.13333333,  10.63333333]
        mae_ecdd = [0.017811463,  0.017569207,  0.019760369,  0.021085186]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[3], atrasos_ecdd[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ecdd)):
            #plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
            plt.text(fa_ecdd[i], atrasos_ecdd[i]+sob_ponto, param_ecdd[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        
        ###############################################-ELM-FEDD-#############################################################
        tecnica = 'ELM-FEDD'
        param_fedd = ['0', '0.25', '0.5', '0.75']
        atrasos_fedd = [1315.433333,  1626.633333,  1413.366667,  1893.7]
        fa_fedd = [57,  13.1,  6.233333333,  3.366666667]
        mae_fedd = [0.013523039,  0.030027827,  0.066795104,  0.063871453]
        val_min = min(mae_fedd)
        i = mae_fedd.index(val_min)
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_fedd[3], atrasos_fedd[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_fedd)):
            #plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
            plt.text(fa_fedd[i], atrasos_fedd[i]+sob_ponto, param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [1529.433333,  1602.233333,  1899.266667,  1835.566667]
        fa_c = [50.3,  48.33333333,  46.16666667,  44.7]
        mae_c = [0.012748385,  0.012783434,  0.013681787,  0.013052804]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[3], atrasos_c[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_c)):
            #plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
            plt.text(fa_c[i], atrasos_c[i]+sob_ponto, param_c[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
    
    
        ########################################IDPSO-ELM-S################################################################################
        tecnica = 'IDPSO-ELM-S'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1529.333333,  1969.766667,  3475.166667,  5048.466667]
        fa_s = [43.86666667,  18.13333333,  10.5,  6.066666667]
        mae_s = [0.013168267,  0.013866622,  0.014852327,  0.015385162]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
        
        ########################################IDPSO-ELM-SV################################################################################
        tecnica = 'IDPSO-ELM-SV'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1390.2,  1744.766667,  2673.266667,  3942.366667]
        fa_s = [45.9,  19.6,  10.9,  6.033333333]
        mae_s = [0.012802833,  0.013279847,  0.015107225,  0.014919755]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[3], atrasos_s[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        '''
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
        plt.plot(fa_s[1], atrasos_s[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        '''
        
        ########################################IDPSO-ELM-BS################################################################################
        tecnica = 'RPSO-ELM'
        param_s = ['1', '2', '3', '4']
        atrasos_s = [3085.433333,  6846.533333,  8964.2,  10315.76667]
        fa_s = [15.66666667,  5.8,  3.9,  2.8]
        mae_s = [0.012358074,  0.015267738,  0.017237839,  0.017972077]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[0], atrasos_s[0]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.title('Curve FPR x DD For Linear Abrupt Time Series',  {'fontsize': legenda})
        plt.tick_params(labelsize= fonte)
        plt.xlabel('FPR', fontsize= fonte)
        plt.ylabel('DD', fontsize=fonte)
        plt.legend(prop={'size':legenda})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
    
    def Curvas_artificiais_nlin_grad(self):
        
        ##########################################PARAMETROS####################################################################
        cores = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black']
        pontos = ['bo', 'bs', 'g^']
        line = ['-', '--', '-.', ':', 'steps']
        best = 'red'
        tradeoff = 'yellow'
        tamanho_linha = 4
        tamanho_pontos = 8
        tamanho_fonte = 11
        sob_ponto = 300
        sob_triang = 90
        tam_triang = 6
        alfa = 0.7
        ########################################################################################################################
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [1276.866667,  1384.666667,  1851.066667,  10048.13333]
        fa_ddm = [57,  55.7,  37.7,  4.266666667]
        mae_ddm = [0.034736048,  0.036285867,  0.034455381,  0.035075013]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[3], atrasos_ddm[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ddm)):
            #plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
            plt.text(fa_ddm[i], atrasos_ddm[i]+sob_ponto, param_ddm[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        atrasos_ecdd = [1457.7,  2457.4,  5494.066667,  9515.966667]
        fa_ecdd = [53.6,  33.1,  9.233333333,  3.433333333]
        mae_ecdd = [0.035821564,  0.035285538,  0.034540666,  0.035065079]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[2], atrasos_ecdd[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ecdd)):
            #plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
            plt.text(fa_ecdd[i], atrasos_ecdd[i]+sob_ponto, param_ecdd[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-FEDD-#############################################################
        tecnica = 'ELM-FEDD'
        param_fedd = ['0', '0.25', '0.5', '0.75']
        atrasos_fedd = [1317.9,  8939.533333,  13625.63333,  16034.33333]
        fa_fedd = [57,  8.166666667,  1.866666667,  0.9]
        mae_fedd = [0.033155362,  0.036602977,  0.037082587,  0.044245015]
        val_min = min(mae_fedd)
        i = mae_fedd.index(val_min)
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_fedd[1], atrasos_fedd[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_fedd)):
            #plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
            plt.text(fa_fedd[i], atrasos_fedd[i]+sob_ponto, param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [3343.2,  4136.8,  4843.366667,  4940.966667]
        fa_c = [39.83333333,  36.43333333,  32.36666667,  31.4]
        mae_c = [0.033083548,  0.032829917,  0.032817463,  0.033268274]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[3], atrasos_c[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_c)):
            #plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
            plt.text(fa_c[i], atrasos_c[i]+sob_ponto, param_c[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
    
    
        ########################################IDPSO-ELM-S################################################################################
        tecnica = 'IDPSO-ELM-S'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1433.1,  2818.566667,  6706.566667,  11046.96667]
        fa_s = [53.16666667,  26.86666667,  4.5,  1]
        mae_s = [0.032971889,  0.032799604,  0.033001789,  0.033785918]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
        
        ########################################IDPSO-ELM-SV################################################################################
        tecnica = 'IDPSO-ELM-SV'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1396.5,  2320.533333,  6094.066667,  10652.1]
        fa_s = [53.66666667,  29,  5.433333333,  1.366666667]
        mae_s = [0.032702199,  0.032722155,  0.032785869,  0.033745942]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        '''
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
        plt.plot(fa_s[1], atrasos_s[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        '''
        
        ########################################IDPSO-ELM-BS################################################################################
        tecnica = 'RPSO-ELM'
        param_s = ['1', '2', '3', '4']
        atrasos_s = [14566.7,  17069.43333,  17117.96667,  17500.73333]
        fa_s = [0.533333333,  0,  0.066666667,  0]
        mae_s = [0.036013005,  0.037401111,  0.038564703,  0.038664173]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[0], atrasos_s[0]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.title('Curve FPR x DD For Non-linear Gradual Time Series',  {'fontsize': legenda})
        plt.tick_params(labelsize= fonte)
        plt.xlabel('FPR', fontsize= fonte)
        plt.ylabel('DD', fontsize=fonte)
        plt.legend(prop={'size':legenda})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
    
    def Curvas_artificiais_nlin_abt(self):
        
        ##########################################PARAMETROS####################################################################
        cores = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black']
        pontos = ['bo', 'bs', 'g^']
        line = ['-', '--', '-.', ':', 'steps']
        best = 'red'
        tradeoff = 'yellow'
        tamanho_linha = 4
        tamanho_pontos = 8
        tamanho_fonte = 11
        sob_ponto = 300
        sob_triang = 90
        tam_triang = 6
        alfa = 0.7
        ########################################################################################################################
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [1429.933333,  1567.366667,  1734.433333,  2407.266667]
        fa_ddm = [56.3,  55.03333333,  47.33333333,  25.9]
        mae_ddm = [0.058707731,  0.040188159,  0.063594064,  0.048260816]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[3], atrasos_ddm[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ddm)):
            #plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
            plt.text(fa_ddm[i], atrasos_ddm[i]+sob_ponto, param_ddm[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        atrasos_ecdd = [1679.3,  2909.233333,  4507.766667,  5261.533333]
        fa_ecdd = [46.53333333,  24.13333333,  14.6,  10.4]
        mae_ecdd = [0.036032306,  0.043751417,  0.028705699,  0.049387328]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[3], atrasos_ecdd[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ecdd)):
            #plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
            plt.text(fa_ecdd[i], atrasos_ecdd[i]+sob_ponto, param_ecdd[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-FEDD-#############################################################
        tecnica = 'ELM-FEDD'
        param_fedd = ['0', '0.25', '0.5', '0.75']
        atrasos_fedd = [1349.833333,  4697.9,  5916.5,  6510.1]
        fa_fedd = [57,  9.133333333,  4.566666667,  3.4]
        mae_fedd = [0.046742538,  0.08545889,  0.068362713,  0.121044875]
        val_min = min(mae_fedd)
        i = mae_fedd.index(val_min)
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_fedd[1], atrasos_fedd[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_fedd)):
            #plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
            plt.text(fa_fedd[i], atrasos_fedd[i]+sob_ponto, param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [3343.2,  4136.8,  4843.366667,  4940.966667]
        fa_c = [50.66666667,  48.86666667,  48.8,  46.43333333]
        mae_c = [0.01703281,  0.018117926,  0.017430204,  0.01717139]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[3], atrasos_c[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_c)):
            #plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
            plt.text(fa_c[i], atrasos_c[i]+sob_ponto, param_c[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
    
    
        ########################################IDPSO-ELM-S################################################################################
        tecnica = 'IDPSO-ELM-S'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [2156.3,  3663.466667,  6306.166667,  9186.9]
        fa_s = [43.46666667,  17.86666667,  8.3,  4.2]
        mae_s = [0.017330932,  0.017660505,  0.018218966,  0.018668395]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
        
        ########################################IDPSO-ELM-SV################################################################################
        tecnica = 'IDPSO-ELM-SV'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1817.866667,  3347.966667,  6369.533333,  8988.733333]
        fa_s = [45.53333333,  20.36666667,  9.133333333,  5.466666667]
        mae_s = [0.018730997,  0.017116451,  0.017657997,  0.01831623]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        '''
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
        plt.plot(fa_s[1], atrasos_s[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        '''
        
        ########################################IDPSO-ELM-BS################################################################################
        tecnica = 'RPSO-ELM'
        param_s = ['1', '2', '3', '4']
        atrasos_s = [6277.666667,  10407.86667,  12142.96667,  12757.93333]
        fa_s = [12.2,  5.333333333,  2.533333333,  2.133333333]
        mae_s = [0.018120445,  0.021936548,  0.022783185,  0.023300527]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[0], atrasos_s[0]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.title('Curve FPR x DD For Non-linear Abrupt Time Series',  {'fontsize': legenda})
        plt.tick_params(labelsize= fonte)
        plt.xlabel('FPR', fontsize= fonte)
        plt.ylabel('DD', fontsize=fonte)
        plt.legend(prop={'size':legenda})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
    
    def Curvas_artificiais_saz(self):
        
        ##########################################PARAMETROS####################################################################
        cores = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black']
        pontos = ['bo', 'bs', 'g^']
        line = ['-', '--', '-.', ':', 'steps']
        best = 'red'
        tradeoff = 'yellow'
        tamanho_linha = 4
        tamanho_pontos = 8
        tamanho_fonte = 11
        sob_ponto = 300
        sob_triang = 90
        tam_triang = 6
        alfa = 0.7
        ########################################################################################################################
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [1268.366667,  1435.8,  3210.833333,  6305.933333]
        fa_ddm = [57,  56.06666667,  37.53333333,  8.8]
        mae_ddm = [0.072340348,  0.07010872,  0.071852822,  0.078154009]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[3], atrasos_ddm[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ddm)):
            #plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
            plt.text(fa_ddm[i], atrasos_ddm[i]+sob_ponto, param_ddm[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        atrasos_ecdd = [1449.133333,  1910.5,  3013.966667,  3957.166667]
        fa_ecdd = [55.96666667,  51.63333333,  30.2,  10.8]
        mae_ecdd = [0.070074467,  0.072570456,  0.071438934,  0.07351]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[3], atrasos_ecdd[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ecdd)):
            #plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
            plt.text(fa_ecdd[i], atrasos_ecdd[i]+sob_ponto, param_ecdd[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-FEDD-#############################################################
        tecnica = 'ELM-FEDD'
        param_fedd = ['0', '0.25', '0.5', '0.75']
        atrasos_fedd = [1230.066667,  6025,  8601.5,  11619.03333]
        fa_fedd = [54.93333333,  2.833333333,  0.9,  0.566666667]
        mae_fedd = [0.046742538,  0.08545889,  0.068362713,  0.121044875 ]
        val_min = min(mae_fedd)
        i = mae_fedd.index(val_min)
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_fedd[1], atrasos_fedd[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_fedd)):
            #plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
            plt.text(fa_fedd[i], atrasos_fedd[i]+sob_ponto, param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [2324.333333,  2540.133333,  2525.1,  1818.1]
        fa_c = [53.36666667,  52.63333333,  52.43333333,  54.6]
        mae_c = [0.068070501,  0.068144423,  0.067979817,  0.066847063]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[3], atrasos_c[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_c)):
            #plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
            plt.text(fa_c[i], atrasos_c[i]+sob_ponto, param_c[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
    
    
        ########################################IDPSO-ELM-S################################################################################
        tecnica = 'IDPSO-ELM-S'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1432.733333,  1795.3,  3421.4,  4028.5]
        fa_s = [55.86666667,  48.43333333,  25.16666667,  7.2]
        mae_s = [0.066614379,  0.06734919,  0.068033088,  0.068968655]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[3], atrasos_s[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
        
        ########################################IDPSO-ELM-SV################################################################################
        tecnica = 'IDPSO-ELM-SV'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1427.4,  1421.4,  2362.633333,  3967.833333]
        fa_s = [55.96666667,  51.33333333,  30.1,  10.83333333]
        mae_s = [0.066839345,  0.066617305,  0.067048395,  0.068810921]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[3], atrasos_s[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        '''
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
        plt.plot(fa_s[1], atrasos_s[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        '''
        
        ########################################IDPSO-ELM-BS################################################################################
        tecnica = 'RPSO-ELM'
        param_s = ['1', '2', '3', '4']
        atrasos_s = [10321.96667,  11795.66667,  14805.56667,  15432.9]
        fa_s = [1.033333333,  0.166666667,  0.166666667,  0.066666667]
        mae_s = [0.083382342,  0.104526192,  0.183390587,  0.189710868]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[0], atrasos_s[0]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.title('Curve FPR x DD For Sazonal Time Series',  {'fontsize': legenda})
        plt.tick_params(labelsize= fonte)
        plt.xlabel('FPR', fontsize= fonte)
        plt.ylabel('DD', fontsize=fonte)
        plt.legend(prop={'size':legenda})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
    
    def Curvas_artificiais_hib(self):
        
        ##########################################PARAMETROS####################################################################
        cores = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black']
        pontos = ['bo', 'bs', 'g^']
        line = ['-', '--', '-.', ':', 'steps']
        best = 'red'
        tradeoff = 'yellow'
        tamanho_linha = 4
        tamanho_pontos = 8
        tamanho_fonte = 11
        sob_ponto = 300
        sob_triang = 90
        tam_triang = 6
        alfa = 0.7
        ########################################################################################################################
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [1331.033333,  2638.966667,  5182.333333,  4968.1]
        fa_ddm = [56.86666667,  49.73333333,  32.3,  17.5]
        mae_ddm = [0.102463148,  0.09171635,  0.063139217,  0.051077486]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[3], atrasos_ddm[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ddm)):
            #plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
            plt.text(fa_ddm[i], atrasos_ddm[i]+sob_ponto, param_ddm[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        atrasos_ecdd = [2489.533333,  3478.1,  3905.766667,  4109.733333]
        fa_ecdd = [42.4,  18.7,  12.23333333,  9.1]
        mae_ecdd = [0.367759852,  0.064391734,  0.241314337,  0.093112217]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[3], atrasos_ecdd[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_ecdd)):
            #plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
            plt.text(fa_ecdd[i], atrasos_ecdd[i]+sob_ponto, param_ecdd[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-FEDD-#############################################################
        tecnica = 'ELM-FEDD'
        param_fedd = ['0', '0.25', '0.5', '0.75']
        atrasos_fedd = [1329.5,  1988.433333,  3407.3,  4500.966667]
        fa_fedd = [56.96666667,  19.4,  12.86666667,  10.76666667]
        mae_fedd = [0.083406991,  0.067925495,  0.096041824,  0.09713683]
        val_min = min(mae_fedd)
        i = mae_fedd.index(val_min)
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_fedd[3], atrasos_fedd[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_fedd)):
            #plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
            plt.text(fa_fedd[i], atrasos_fedd[i]+sob_ponto, param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [2944.3,  3323.633333,  3881.366667,  3676.333333]
        fa_c = [45.33333333,  43.16666667,  41.73333333,  41.9]
        mae_c = [0.027900634,  0.02896083,  0.027864754,  0.032016086]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[3], atrasos_c[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_c)):
            #plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
            plt.text(fa_c[i], atrasos_c[i]+sob_ponto, param_c[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
    
    
        ########################################IDPSO-ELM-S################################################################################
        tecnica = 'IDPSO-ELM-S'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [3590.733333,  3651.133333,  3496.666667,  4624.733333]
        fa_s = [37.46666667,  15.1,  9.5,  6.333333333]
        mae_s = [0.032832076,  0.037360233,  0.044701572,  0.05075141]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[3], atrasos_s[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
        
        ########################################IDPSO-ELM-SV################################################################################
        tecnica = 'IDPSO-ELM-SV'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [2477.433333,  3280.166667,  3144.333333,  4109.733333]
        fa_s = [41.5,  16.43333333,  10.13333333,  7.333333333]
        mae_s = [0.031684798,  0.047116304,  0.047406151,  0.043451749]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[3], atrasos_s[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        '''
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
        plt.plot(fa_s[1], atrasos_s[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        '''
        
        ########################################IDPSO-ELM-BS################################################################################
        tecnica = 'RPSO-ELM'
        param_s = ['1', '2', '3', '4']
        atrasos_s = [10321.96667,  11795.66667,  14805.56667,  15432.9]
        fa_s = [6.1,  3.533333333,  1.566666667,  1.2]
        mae_s = [0.024646308,  0.05345759,  0.063632963,  0.047311549]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[0], atrasos_s[0]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tam_triang)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.title('Curve FPR x DD For Hibrid Time Series',  {'fontsize': legenda})
        plt.tick_params(labelsize= fonte)
        plt.xlabel('FPR', fontsize= fonte)
        plt.ylabel('DD', fontsize=fonte)
        plt.legend(prop={'size':legenda})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
    
    def Curvas_reais_retorno(self):
        
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
        cores = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black']
        pontos = ['bo', 'bs', 'g^']
        line = ['-', '--', '-.', ':', 'steps']
        best = 'red'
        tradeoff = 'yellow'
        tamanho_linha = 4
        tamanho_pontos = 8
        tamanho_fonte = 11
        tamanho_tradeoff = 6
        sob_ponto = 7
        sob_triang = 2
        alfa = 0.7
        ########################################################################################################################
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [280, 259.8, 280, 280]
        fa_ddm = [4, 4, 4, 4]
        mae_ddm = [0.125988124, 0.124289217, 0.125488219, 0.126176397]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
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
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
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
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
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
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
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
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
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
        
        plt.plot(fa_s,   atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ########################################IDPSO-ELM-BS################################################################################
        tecnica = 'RPSO-ELM'
        param_s = ['1', '2', '3', '4']
        atrasos_s = [386.8,  372.8,  452.4,  518.6]
        fa_s = [1.6,  0.4,  0.4,  0]
        mae_s = [0.024982148,  0.027982034,  0.034897447,  0.030648013]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[1], atrasos_s[1]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.title('Down Jones With a Concept Drift Known',  {'fontsize': legenda})
        plt.tick_params(labelsize= fonte)
        plt.xlabel('FPR', fontsize= fonte)
        plt.ylabel('DD', fontsize=fonte)
        plt.legend(prop={'size':legenda})
        plt.grid(True)
        plt.show()
        ########################################################################################################################
    
    def Curvas_sp(self):
        
        ##########################################PARAMETROS####################################################################
        cores = ['blue', 'green', 'red', 'cyan', 'purple', 'yellow', 'black']
        pontos = ['bo', 'bs', 'g^']
        line = ['-', '--', '-.', ':', 'steps']
        best = 'red'
        tradeoff = 'yellow'
        tamanho_linha = 4
        tamanho_pontos = 8
        tamanho_fonte = 11
        tamanho_tradeoff = 6
        sob_ponto = 50
        sob_triang = 10
        alfa = 0.7
        ########################################################################################################################
        
        ###############################################-ELM-DDM-######################################################
        tecnica = 'ELM-DDM'  
        param_ddm = ['2', '4', '6', '8']
        atrasos_ddm = [170,  170,  170,  170]
        fa_ddm = [37,  37,  37,  37]
        mae_ddm = [0.013666161,  0.011529026,  0.012130961,  0.010924068]
        val_min = min(mae_ddm)
        i = mae_ddm.index(val_min)
        
        plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ddm[3], atrasos_ddm[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_ddm)):
            #plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
            plt.text(fa_ddm[i], atrasos_ddm[i]+sob_ponto, param_ddm[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-ECDD-#############################################################
        tecnica = 'ELM-ECDD'
        param_ecdd = ['0.25', '0.5', '0.75', '1']
        atrasos_ecdd = [767.6,  1102.2,  882.6,  1245]
        fa_ecdd = [20.2,  12.8,  11,  10]
        mae_ecdd = [0.013154498,  0.013962691,  0.015089595,  0.018075655]
        val_min = min(mae_ecdd)
        i = mae_ecdd.index(val_min)
        
        plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_ecdd[3], atrasos_ecdd[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_ecdd)):
            #plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
            plt.text(fa_ecdd[i], atrasos_ecdd[i]+sob_ponto, param_ecdd[i], fontsize=tamanho_fonte)
        ############################################################################################################
        
        ###############################################-ELM-FEDD-#############################################################
        tecnica = 'ELM-FEDD'
        param_fedd = ['0', '0.25', '0.5', '0.75']
        atrasos_fedd = [305,  484,  350,  609]
        fa_fedd = [27,  27,  17,  14]
        mae_fedd = [0.052969354,  0.018260641,  0.788872002,  0.033532531]
        val_min = min(mae_fedd)
        i = mae_fedd.index(val_min)
        
        plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_fedd[3], atrasos_fedd[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_fedd)):
            #plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
            plt.text(fa_fedd[i], atrasos_fedd[i]+sob_ponto, param_fedd[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        
        ###########################################-IDPSO-ELM-B ################################################################
        tecnica = 'IDPSO-ELM-B'
        param_c = ['0.25', '0.5', '0.75', '1']
        atrasos_c = [406,  364.8,  402.4,  663.2]
        fa_c = [24.6,  20.8,  20,  17.2]
        mae_c = [0.009832959,  0.010959407,  0.010231704,  0.010409677]
        val_min = min(mae_c)
        i = mae_c.index(val_min)
        
        plt.plot(fa_c,  atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_c[3], atrasos_c[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_c)):
            #plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
            plt.text(fa_c[i], atrasos_c[i]+sob_ponto, param_c[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
    
    
        ########################################IDPSO-ELM-S################################################################################
        tecnica = 'IDPSO-ELM-S'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [1310.8,  1274,  1247.6,  2027.4]
        fa_s = [15.2,  9.4,  7.6,  5.4]
        mae_s = [0.015142231,  0.020741042,  0.019845362,  0.025659656]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[2], atrasos_s[2]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ###########################################################################################################################
        
        ########################################IDPSO-ELM-SV################################################################################
        tecnica = 'IDPSO-ELM-SV'
        param_s = ['0.25', '0.5', '0.75', '1']
        atrasos_s = [779,  1143,  1032,  1368.6]
        fa_s = [17.4,  10.4,  8.8,  7.4]
        mae_s = [0.011260627,  0.010893518,  0.015625199,  0.014549436]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s,   atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha, alpha = alfa)
        plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[3], atrasos_s[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+tamanho_tradeoff)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ########################################IDPSO-ELM-BS################################################################################
        tecnica = 'RPSO-ELM'
        param_s = ['1', '2', '3', '4']
        atrasos_s = [949.4,  1807.2,  1287,  1538.2]
        fa_s = [26,  12.8,  10.8,  8.6]
        mae_s = [0.008511887,  0.013256357,  0.011274764,  0.012212321]
        val_min = min(mae_s)
        i = mae_s.index(val_min)
        
        plt.plot(fa_s, atrasos_s, pontos[0], color = cores[1], markersize=tamanho_pontos, alpha = alfa)
        plt.plot(fa_s, atrasos_s, line[1], color = cores[1], label = tecnica, linewidth=tamanho_linha, alpha = alfa)
        #plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
        plt.plot(fa_s[3], atrasos_s[3]+sob_triang, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
        for i in range(len(param_s)):
            #plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
            plt.text(fa_s[i], atrasos_s[i]+sob_ponto, param_s[i], fontsize=tamanho_fonte)
        ########################################################################################################################
        
        ###########################################PLOTANDO E ADICIONANDO LEGENDAS############################################
        plt.title('S&P500 With a Concept Drift Known',  {'fontsize': legenda})
        plt.tick_params(labelsize= fonte)
        plt.xlabel('FPR', fontsize= fonte)
        plt.ylabel('DD', fontsize=fonte)
        plt.legend(prop={'size':legenda})
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
    c.Curvas_artificiais_geral()
    c.Curvas_artificiais_lin_grad()
    c.Curvas_artificiais_lin_abt()
    c.Curvas_artificiais_nlin_grad()
    c.Curvas_artificiais_nlin_abt()
    c.Curvas_artificiais_saz()
    c.Curvas_artificiais_hib()
    c.Curvas_down()
    c.Curvas_sp()
    c.Tempo_execucao()
    
if __name__ == "__main__":
    main()
    
    
    