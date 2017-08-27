# -*- coding: utf-8 -*-
'''
Created on 24 de abr de 2017

@author: gusta
'''

import matplotlib.pyplot as plt

class ROC_curve():
    def __init__(self):
        pass
    
    def PlotarCurva(self, x, y, labels, tecnica):
        
        plt.plot(x, y, 'bo', label = "Parametros")
        plt.plot(x, y)
        
        plt.legend()
        
        plt.xlabel('Atrasos')
        plt.ylabel('Falsos Alarmes')
        
        for i in range(len(labels)):
            plt.text(x[i], y[i], labels[i])
            
        plt.title('%s ' % (tecnica))
        plt.grid(True)
        
        plt.show()

def main():
    '''
    tecnica1 = 'S'
    param1 = ['1', '5', '10', '20', '30']
    mae1 = [0.0424, 0.0416, 0.0424, 0.0421, 0.0425]
    fa1 = [10.10, 10.13, 9.40, 9.075, 9.28]
    
    tecnica2 = 'CPT'
    param2 = ['1', '5', '10', '25', '50']
    mae2 = [0.0375, 0.0416, 0.0422, 0.0484, 0.0583]
    fa2 = [53.90, 36.55, 20.45, 8.35, 3.50]
    
    
    
    
    ############################################GRAFICO 1 ######################################################
    figura = plt.figure()
    
    N = len(fa1)
    x = range(N)
    width = 0.6
    
    lim_mae = 0.02
    lim_mae_min = 0.01
    lim_fa = 5
    
    
    grafico1 = figura.add_subplot(2, 2, 1)
    grafico1.grid(True)
    grafico1.bar(x, fa1, width, align='center', color = 'Blue', label = tecnica1)
    grafico1.legend()
    plt.ylabel('Falsos Alarmes')
    plt.xlabel('Parâmetros')
    grafico1.axis([-1, 5, min(fa1)-lim_fa, max(fa1)+lim_fa])
    grafico1.set_xticks(x)
    grafico1.set_xticklabels(param1)
    
    
    grafico2 = figura.add_subplot(2, 2, 2)
    grafico2.grid(True)
    grafico2.bar(x, mae1, width, align='center', color = 'Blue', label = tecnica1)
    grafico2.legend()
    plt.ylabel('MAE')
    plt.xlabel('Parâmetros')
    grafico2.axis([-1, 5, min(mae1)-lim_mae_min, max(mae1)+lim_mae])
    grafico2.set_xticks(x)
    grafico2.set_xticklabels(param1)
    
    
    grafico3 = figura.add_subplot(2, 2, 3)
    grafico3.grid(True)
    grafico3.bar(x, fa2, width, align='center', color = 'Red', label = tecnica2)
    grafico3.legend()
    plt.ylabel('Falsos Alarmes')
    plt.xlabel('Parâmetros')
    grafico3.axis([-1, 5, 0, max(fa2)+lim_fa])
    grafico3.set_xticks(x)
    grafico3.set_xticklabels(param2)
    
    
    grafico4 = figura.add_subplot(2, 2, 4)
    grafico4.grid(True)
    grafico4.bar(x, mae2, width, align='center', color = 'Red', label = tecnica2)
    grafico4.legend()
    plt.ylabel('MAE')
    plt.xlabel('Parâmetros')
    grafico4.axis([-1, 5, 0, max(mae2)+lim_mae])
    grafico4.set_xticks(x)
    grafico4.set_xticklabels(param2)
    
    
    
    plt.show()
    ############################################################################################################
    
    
    ############################################GRAFICO 2 ######################################################
    figura = plt.figure()
    
    grafico1 = figura.add_subplot(1, 2, 1)
    grafico1.plot(fa1, mae1, 'bo', color = 'Blue')
    grafico1.plot(fa1, mae1, label = tecnica1)
    grafico1.legend()
    plt.xlabel('Falsos Alarmes')
    plt.ylabel('MAE')
    for i in range(len(param1)):
        grafico1.text(fa1[i], mae1[i], param1[i])
    grafico1.grid(True)
    
    grafico2 = figura.add_subplot(1, 2, 2)
    grafico2.plot(fa2, mae2, 'bo', color = 'Red')
    grafico2.plot(fa2, mae2, color = 'Red', label = tecnica2)
    grafico2.legend()
    plt.xlabel('Falsos Alarmes')
    plt.ylabel('MAE')
    for i in range(len(param1)):
        grafico2.text(fa2[i], mae2[i], param2[i])
    grafico2.grid(True)
    
    plt.show()
    ############################################################################################################
    '''
    
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
    
    ###############################################-ELM-ECDD-#############################################################
    tecnica = 'ELM-ECDD'
    #param_ecdd = ['0.5', '0.75', '1', '1.5', '2']
    #atrasos_ecdd = [2798.418333,    4169.381667,   5375.136667,    7004.57,    8465.543333]
    #fa_ecdd = [26.98166667,    17.61333333,    9.651666667,    3.631666667,    1.918333333]
    param_ecdd = ['0.25', '0.5', '0.75', '1']
    atrasos_ecdd = [2237.661667,    2798.418333,    4169.381667,   5375.136667]
    fa_ecdd = [43.69833333,   26.98166667,    17.61333333,    9.651666667]
    mae_ecdd = [0.055793487,    0.056384367,    0.057980822,    0.068061947,    0.067606176]
    val_min = min(mae_ecdd)
    i = mae_ecdd.index(val_min)
    
    #cr.PlotarCurva(atrasos_ecdd, fa_ecdd, param_ecdd, tecnica)
    plt.plot(fa_ecdd, atrasos_ecdd, pontos[0], color = cores[0], markersize=tamanho_pontos)
    plt.plot(fa_ecdd, atrasos_ecdd, line[0], color = cores[0],label = tecnica, linewidth=tamanho_linha)
    plt.plot(fa_ecdd[i], atrasos_ecdd[i], pontos[1], color = best, markersize=tamanho_pontos)
    plt.plot(fa_ecdd[2], atrasos_ecdd[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
    #plt.plot(fa_ecdd, atrasos_ecdd, 'bo', color = 'Blue')
    #plt.plot(fa_ecdd, atrasos_ecdd, label = tecnica)
    #for i in range(len(param_ecdd)):
    #    plt.text(fa_ecdd[i] + af_fa, atrasos_ecdd[i] + af_dd, param_ecdd[i], fontsize=tamanho_fonte)
    #plt.grid(True)
    #plt.show()
    
    
    ############################################################################################################
    ###############################################-ELM-DDM-ELM_pcg_ELM_DDM######################################################
    tecnica = 'ELM-DDM'   #param_ddm = ['3', '5', '6', '8', '10']
    #atrasos_ddm = [1911.4,    3469.6,    4526.4,    6400.7,    7754.9]
    #fa_ddm = [52.1,    35.3,    20.7,    7.8,    4.4]
    param_ddm = ['3', '5', '6', '8']
    atrasos_ddm = [1911.4,    3469.6,    4526.4,    6400.7]
    fa_ddm = [52.1,    35.3,    20.7,    7.8]
    mae_ddm = [0.0468,    0.0483,    0.0504,    0.0780]
    val_min = min(mae_ddm)
    i = mae_ddm.index(val_min)
    
    #cr.PlotarCurva(atrasos_ddm, fa_ddm, param_ddm, tecnica)
    plt.plot(fa_ddm, atrasos_ddm, pontos[0], color = cores[1], markersize=tamanho_pontos)
    plt.plot(fa_ddm, atrasos_ddm, line[0], color = cores[1], label = tecnica, linewidth=tamanho_linha)
    plt.plot(fa_ddm[i], atrasos_ddm[i], pontos[1], color = best, markersize=tamanho_pontos)
    plt.plot(fa_ddm[2], atrasos_ddm[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
    #plt.plot(fa_ddm, atrasos_ddm, 'bo', color = 'Green')
    #plt.plot(fa_ddm, atrasos_ddm, label = tecnica)
    #plt.xlabel('Falsos Alarmes')
    #plt.ylabel('Atrasos')
    for i in range(len(param_ddm)):
        plt.text(fa_ddm[i] + af_fa, atrasos_ddm[i] + af_dd, param_ddm[i], fontsize=tamanho_fonte)
    #plt.grid(True)
    #plt.show()
    ############################################################################################################
    
    ###############################################-ELM-FEDD-#############################################################
    tecnica = 'ELM-FEDD'
    #param_fedd = ['0', '0.25', '0.5', '0.75', '1']
    #atrasos_fedd = [1347.108333,    4675.316667,    6790.475,    8354.65,    9809.425]
    #fa_fedd = [56.19166667,    14.94166667,    9.541666667,    7.6,    5.741666667]
    #mae_fedd = [0.058427404,    0.083492844,    0.088153567,    0.123736945,    0.104093741]
    param_fedd = ['0', '0.25', '0.5', '0.75']
    atrasos_fedd = [1347.108333,    4675.316667,    6790.475,    8354.65]
    fa_fedd = [56.19166667,    14.94166667,    9.541666667,    7.6]
    mae_fedd = [0.058427404,    0.083492844,    0.088153567,    0.123736945]
    val_min = min(mae_fedd)
    i = mae_fedd.index(val_min)
    
    #cr.PlotarCurva(atrasos_fedd, fa_fedd, param_fedd, tecnica)
    plt.plot(fa_fedd, atrasos_fedd, pontos[0], color = cores[4], markersize=tamanho_pontos)
    plt.plot(fa_fedd, atrasos_fedd, line[0], color = cores[4],label = tecnica, linewidth=tamanho_linha)
    plt.plot(fa_fedd[i], atrasos_fedd[i], pontos[1], color = best, markersize=tamanho_pontos)
    plt.plot(fa_fedd[1], atrasos_fedd[1]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
    #plt.plot(fa_fedd, atrasos_fedd, 'bo', color = 'Blue')
    #plt.plot(fa_fedd, atrasos_fedd, label = tecnica)
    #plt.xlabel('Falsos Alarmes')
    #plt.ylabel('Atrasos')
    for i in range(len(param_fedd)):
        plt.text(fa_fedd[i] + af_fa, atrasos_fedd[i] + af_dd, param_fedd[i], fontsize=tamanho_fonte)
    #plt.grid(True)
    #plt.show()
    
    ###########################################-IDPSO-ELM-B DDM-ELM_pcg_ELM_DDM#########################################################
    '''
    tecnica = 'IDPSO-ELM-B (DDM)ELM_pcg_ELM_DDMparam_c = ['3', '5', '8', '10']
    
    ################################-w = 3-#################################
    atrasos_c = [1489.692083,    1468.081667,    1469.633333,   1487.083333]
    fa_c = [54.335,    54.36833333,    54.40333333,    54.24166667]
    #cr.PlotarCurva(fa_c, atrasos_c, param_c, tecnica)
    plt.plot(fa_c, atrasos_c, pontos[2], color = cores[2])
    plt.plot(fa_c, atrasos_c, line[2], color = cores[2], label = tecnica + ": limite = 1")
    
    plt.legend()
    for i in range(len(param_c)):
        plt.text(fa_c[i], atrasos_c[i], param_c[i])
    #plt.grid(True)
    #plt.show()
    #######################################################################
    '''
         
    '''
    ###########################################-IDPSO-ELM-B DDM-ELM_pcg_ELM_DDM#########################################################
    tecnica = 'IDPSO-ELM-B (DDM)ELM_pcg_ELM_DDMparam_c = ['1', '5', '10', '25', '50']
    
    ################################-w = 3-#################################
    atrasos_c = [1489.692083,    3769.291667,    7191.123333,   10976.18,    12967.58333]
    fa_c = [54.335,    37.1,    22.12,    8.403333333,    3.481666667]
    #cr.PlotarCurva(fa_c, atrasos_c, param_c, tecnica)
    plt.plot(fa_c, atrasos_c, pontos[2], color = cores[2])
    plt.plot(fa_c, atrasos_c, line[2], color = cores[2], label = tecnica + ": w = 3")
    plt.legend()
    for i in range(len(param_c)):
        plt.text(fa_c[i], atrasos_c[i], param_c[i])
    #plt.grid(True)
    #plt.show()
    #######################################################################
    
    ##############################-w = 5-####################################
    atrasos_c = [1468.081667,    3757.788333,    7419.523333,    10745.21917,    13056.07167]
    fa_c = [54.36833333,    37.04,    21.66833333,    8.613333333,    3.48]
    #cr.PlotarCurva(fa_c, atrasos_c, param_c, tecnica)
    plt.plot(fa_c, atrasos_c, pontos[2], color = cores[3])
    plt.plot(fa_c, atrasos_c, line[2], color = cores[3], label = tecnica + ": w = 5")
    plt.legend()
    for i in range(len(param_c)):
        plt.text(fa_c[i], atrasos_c[i], param_c[i])
    #plt.grid(True)
    #plt.show()
    #######################################################################
    
    ##############################-w = 8-###################################
    atrasos_c = [1469.633333,    3938.168333,    7438.128333,    10788.21333,    13028.00167]
    fa_c = [54.40333333,    36.635,    21.505,    8.451666667,    3.468333333]
    #cr.PlotarCurva(fa_c, atrasos_c, param_c, tecnica)
    plt.plot(fa_c, atrasos_c, pontos[2], color = cores[4])
    plt.plot(fa_c, atrasos_c, line[2], color = cores[4], label = tecnica + ": w = 8")
    plt.legend()
    for i in range(len(param_c)):
        plt.text(fa_c[i], atrasos_c[i], param_c[i])
    #plt.grid(True)
    #plt.show()
    #######################################################################

    ################################-w = 10-####################################
    atrasos_c = [1487.083333,    3825.583333,    7349.59,    10831.55,    13069.04167]
    fa_c = [54.24166667,    36.82666667,    21.63444444,    8.5,    3.431666667]
    #cr.PlotarCurva(fa_c, atrasos_c, param_c, tecnica)
    plt.plot(fa_c, atrasos_c, pontos[2], color = cores[5])
    plt.plot(fa_c, atrasos_c, line[2], color = cores[5], label = tecnica + ": w = 10")
    plt.legend()
    for i in range(len(param_c)):
        plt.text(fa_c[i], atrasos_c[i], param_c[i])
    #plt.grid(True)
    #plt.show()
    #######################################################################
    '''
    ############################################################################################################
    
    ###########################################-IDPSO-ELM-B ECDD-################################################################
    #tecnica = 'IDPSO-ELM-B (ECDD)'
    
    tecnica = 'IDPSO-ELM-B'
    param_c = ['0.25', '0.5', '0.75', '1']
    
    ################################-c = 0.25-#################################
    atrasos_c = [2389.11875,    2459.185,    2640.418333,    5671.061667]
    fa_c = [46.85916667,    46.40833333,    45.59666667,    31.24]
    mae_c = [0.039836941,   0.040017313,    0.04009332,  0.043023703]
    val_min = min(mae_c)
    i = mae_c.index(val_min)
    
    #cr.PlotarCurva(fa_c, atrasos_c, param_c, tecnica)
    plt.plot(fa_c, atrasos_c, pontos[0], color = cores[6], markersize=tamanho_pontos)
    #plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica + ": limite = 1")
    plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica, linewidth=tamanho_linha)
    plt.plot(fa_c[i], atrasos_c[i], pontos[1], color = best, markersize=tamanho_pontos)
    plt.plot(fa_c[2], atrasos_c[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
    for i in range(len(param_c)):
        plt.text(fa_c[i] + af_fa, atrasos_c[i] + af_dd, param_c[i], fontsize=tamanho_fonte)
    #plt.grid(True)
    
    '''
    ###########################################-IDPSO-ELM-B ECDD-################################################################
    tecnica = 'IDPSO-ELM-B (ECDD)'
    param_c = ['1', '5', '10', '25', '50']
    
    ################################-c = 0.25-#################################
    atrasos_c = [2389.11875,    5798.526667,    8728.986667,    11483.235,    13604.10833]
    fa_c = [46.85916667,    30.49333333,    17.5,    7.491666667,    2.963333333]
    #cr.PlotarCurva(fa_c, atrasos_c, param_c, tecnica)
    plt.plot(fa_c, atrasos_c, pontos[0], color = cores[6])
    plt.plot(fa_c, atrasos_c, line[3], color = cores[6], label = tecnica + ": c = 0.25")
    plt.legend()
    for i in range(len(param_c)):
        plt.text(fa_c[i], atrasos_c[i], param_c[i])
    #plt.grid(True)
    #plt.show()
    #######################################################################
    
    ##############################-c = 0.5-####################################
    atrasos_c = [2459.185,    6415.573333,    9116.848333,    11990.5675,    13818.565]
    fa_c = [46.40833333,    28.38666667,    15.755,    6.8175,    2.808333333]
    #cr.PlotarCurva(fa_c, atrasos_c, param_c, tecnica)
    plt.plot(fa_c, atrasos_c, pontos[0], color = cores[0])
    plt.plot(fa_c, atrasos_c, line[3], color = cores[0], label = tecnica + ": c = 0.5")
    plt.legend()
    for i in range(len(param_c)):
        plt.text(fa_c[i], atrasos_c[i], param_c[i])
    #plt.grid(True)
    #plt.show()
    #######################################################################
    
    ################################-c = 0.75-####################################
    atrasos_c = [2640.418333,    6803.251667,    9459.205,    12339.03333,    14000.14]
    fa_c = [45.59666667,    26.38166667,    14.04916667,    6.496666667,    2.613333333]
    #cr.PlotarCurva(fa_c, atrasos_c, param_c, tecnica)
    plt.plot(fa_c, atrasos_c, pontos[0], color = cores[1])
    plt.plot(fa_c, atrasos_c, line[3], color = cores[1], label = tecnica + ": c = 0.75")
    plt.legend()
    for i in range(len(param_c)):
        plt.text(fa_c[i], atrasos_c[i], param_c[i])
    #plt.grid(True)
    #plt.show()
    
    ##############################-c = 1-###################################
    atrasos_c = [5671.061667,    13497.52833,    14430.69833,   15241.085,    15824.56167]
    fa_c = [31.24,    5.54,    3.511666667,    1.708333333,    0.756666667]
    #cr.PlotarCurva(fa_c, atrasos_c, param_c, tecnica)
    plt.plot(fa_c, atrasos_c, pontos[0], color = cores[2])
    plt.plot(fa_c, atrasos_c, line[3], color = cores[2], label = tecnica + ": c = 1")
    plt.legend()
    for i in range(len(param_c)):
        plt.text(fa_c[i], atrasos_c[i], param_c[i])
    #plt.grid(True)
    #plt.show()
    #######################################################################
    '''
    ############################################################################################################
    
    '''
    ##################################################-IDPSO-ELM-S-##########################################################
    tecnica = 'IDPSO-ELM-S (ECDD)'
    param_s = ['1', '5', '10', '20', '30']
    
    N = len(param_s)
    x = range(N)
    width = 0.6
    lim_fa = 1
    lim_atrasos = 50
    
    ################################-0.25-#################################
    atrasos_s = [1939.895,    1930.839167,    1965.871667,    1994.05,    2037.661667]
    fa_s = [44.595,    44.4275,    44.335,    44.26833333,    44.15833333]
    #cr.PlotarCurva(fa_s, atrasos_s, param_s, tecnica)
    plt.plot(fa_s, atrasos_s, 'bo', color = 'Blue')
    plt.plot(fa_s, atrasos_s, label = tecnica + ": c = 0.25")
    plt.legend()
    for i in range(len(param_s)):
        plt.text(fa_s[i], atrasos_s[i], param_s[i])
    #######################################################################
    
    ##############################-0.5-####################################
    atrasos_s = [2716.105,    2734.136667,    2737.878333,    2708.108333,    2694.44]
    fa_s = [27.58666667,    27.30666667,    27.29,    27.255,    27.25166667]
    #cr.PlotarCurva(fa_s, atrasos_s, param_s, tecnica)
    plt.plot(fa_s, atrasos_s, 'bo', color = 'Green')
    plt.plot(fa_s, atrasos_s, label = tecnica + ": c = 0.5")
    plt.legend()
    for i in range(len(param_s)):
        plt.text(fa_s[i], atrasos_s[i], param_s[i])
    #######################################################################
    
    ##############################-0.75-###################################
    atrasos_s = [4011.056667,    3905.813333,    4044.356667,    4050.228333,    4098.958333]
    fa_s = [18.48166667,   18.14,    17.85333333,    17.64166667,    17.605]
    #cr.PlotarCurva(fa_s, atrasos_s, param_s, tecnica)
    plt.plot(fa_s, atrasos_s, 'bo', color = 'Red')
    plt.plot(fa_s, atrasos_s, label = tecnica  + ": c = 0.75")
    plt.legend()
    for i in range(len(param_s)):
        plt.text(fa_s[i], atrasos_s[i], param_s[i])
    #######################################################################
    
    ################################-1-####################################
    atrasos_s = [5119.00,    5149.35,    5346.00,    5150.80,    5106.23]
    fa_s = [10.10, 10.13, 9.40, 9.075, 9.28]
    #cr.PlotarCurva(fa_s, atrasos_s, param_s, tecnica)
    plt.plot(fa_s, atrasos_s, 'bo', color = 'Cyan')
    plt.plot(fa_s, atrasos_s, label = tecnica + ": c = 1")
    plt.legend()
    for i in range(len(param_s)):
        plt.text(fa_s[i], atrasos_s[i], param_s[i])
    plt.grid(True)
    plt.show()
    '''
    #######################################################################
    
    
    ###########################visulização por qtds#######################
    
    #tecnica = 'IDPSO-ELM-S (ECDD)'
    
    tecnica = 'IDPSO-ELM-S'
    param_s = ['0.25', '0.5', '0.75', '1']
    
    N = len(param_s)
    x = range(N)
    width = 0.6
    lim_fa = 1
    lim_atrasos = 50
    
    ################################-1-#################################
    atrasos_s = [1939.895,    2716.105,   4011.056667,    5119.00]
    fa_s = [43.595,    26.58666667,    17.48166667,    9.10]
    mae_s = [0.041482178,    0.04362065,    0.044493041,    0.0424]
    val_min = min(mae_s)
    i = mae_s.index(val_min)
    
    #cr.PlotarCurva(fa_s, atrasos_s, param_s, tecnica)
    plt.plot(fa_s, atrasos_s, pontos[0], color = cores[3], markersize=tamanho_pontos)
    plt.plot(fa_s, atrasos_s, line[1], color = cores[3], label = tecnica + " (1)", linewidth=tamanho_linha)
    plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
    plt.plot(fa_s[2], atrasos_s[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
    #for i in range(len(param_s)):
    #    plt.text(fa_s[i] + af_fa, atrasos_s[i] + af_dd, param_s[i], fontsize=tamanho_fonte)
    #plt.grid(True)
    #plt.show()
    
    #######################################################################
    
    '''
    ##############################-5-####################################
    atrasos_s = [1930.839167,    2734.136667,    3905.813333,   5149.35]
    fa_s = [44.4275,    27.30666667,    18.14,    10.13]
    #cr.PlotarCurva(fa_s, atrasos_s, param_s, tecnica)
    plt.plot(fa_s, atrasos_s, pontos[1], color = cores[2])
    plt.plot(fa_s, atrasos_s, line[1], color = cores[2], label = tecnica + ": qtds = 5")
    plt.legend()
    for i in range(len(param_s)):
        plt.text(fa_s[i], atrasos_s[i], param_s[i])
    #plt.grid(True)
    #plt.show()
    #######################################################################
    
    ##############################-10-###################################
    atrasos_s = [1965.871667,    2737.878333,    4044.356667,    5346.00]
    fa_s = [44.335,    27.29,    17.85333333,    9.40]
    #cr.PlotarCurva(fa_s, atrasos_s, param_s, tecnica)
    plt.plot(fa_s, atrasos_s, pontos[1], color = cores[4])
    plt.plot(fa_s, atrasos_s, line[1], color = cores[4], label = tecnica  + ": qtds = 10")
    plt.legend()
    for i in range(len(param_s)):
        plt.text(fa_s[i], atrasos_s[i], param_s[i])
    #plt.grid(True)
    #plt.show()
    #######################################################################
    
    ################################-20-####################################
    atrasos_s = [1994.05,    2708.108333,    4050.228333,    5150.80]
    fa_s = [44.26833333,    27.255,    17.64166667,    9.075]
    #cr.PlotarCurva(fa_s, atrasos_s, param_s, tecnica)
    plt.plot(fa_s, atrasos_s, pontos[1], color = cores[5])
    plt.plot(fa_s, atrasos_s, line[1], color = cores[5], label = tecnica + ": qtds = 20")
    plt.legend()
    for i in range(len(param_s)):
        plt.text(fa_s[i], atrasos_s[i], param_s[i])
    #plt.grid(True)
    #plt.show()
    #######################################################################
    '''
    
    ################################-30-####################################
    atrasos_s = [2037.661667,    2694.44,    4098.958333,    5106.23]
    fa_s = [43.15833333,   26.25166667,    16.605,    8.28]
    mae_s = [0.041458538,  0.044224473,  0.045264889,   0.042510248]
    val_min = min(mae_s)
    i = mae_s.index(val_min)
    
    #cr.PlotarCurva(fa_s, atrasos_s, param_s, tecnica)
    plt.plot(fa_s, atrasos_s, pontos[0], color = cores[6], markersize=tamanho_pontos)
    plt.plot(fa_s, atrasos_s, line[1], color = cores[6], label = tecnica + " (30)", linewidth=tamanho_linha)
    plt.plot(fa_s[i], atrasos_s[i], pontos[1], color = best, markersize=tamanho_pontos)
    plt.plot(fa_s[2], atrasos_s[2]+50, pontos[2], color = tradeoff, markersize=tamanho_pontos+5)
    for i in range(len(param_s)):
        plt.text(fa_s[i] - 1.5, atrasos_s[i] - 5*af_dd, param_s[i], fontsize=tamanho_fonte)
    #######################################################################
    
    plt.tick_params(labelsize= 18)
    plt.xlabel('FPR', fontsize= 18)
    plt.ylabel('DD', fontsize=18)
    plt.legend(prop={'size':25})
    plt.grid(True)
    plt.show()


    ################################-0.25-#################################
    param_s = ['1', '5', '10', '20', '30']
    atrasos_s = [1939.895,    1930.839167,    1965.871667,    1994.05,    2037.661667]
    fa_s = [44.595,    44.4275,    44.335,    44.26833333,    44.15833333]
    
    N = len(atrasos_s)
    x = range(N)
    
    figura = plt.figure()
    figura.suptitle("IDPSO-ELM-S: c = 0.25", fontsize=11, fontweight='bold')
    grafico1 = figura.add_subplot(1, 2, 1)
    grafico1.grid(True)
    grafico1.bar(x, fa_s, width, align='center', color = 'Blue', label = 'qtds')
    grafico1.legend()
    plt.ylabel('False Alarms')
    plt.xlabel('Number of Sensors')
    grafico1.axis([-1, 5, min(fa_s)-lim_fa, max(fa_s)+lim_fa])
    grafico1.set_xticks(x)
    grafico1.set_xticklabels(param_s)
    plt.show(True)
    
    grafico2 = figura.add_subplot(1, 2, 2)
    grafico2.grid(True)
    grafico2.bar(x, atrasos_s, width, align='center', color = 'Blue',  label = 'qtds')
    grafico2.legend()
    plt.ylabel('Atrasos')
    plt.xlabel('Parâmetros')
    grafico2.axis([-1, 5, min(atrasos_s)-lim_atrasos, max(atrasos_s)+lim_atrasos])
    grafico2.set_xticks(x)
    grafico2.set_xticklabels(param_s)
    ############################################################################################################
    
    ################################-0.5-#################################
    atrasos_s = [2716.105,    2734.136667,    2737.878333,    2708.108333,    2694.44]
    fa_s = [27.58666667,    27.30666667,    27.29,    27.255,    27.25166667]
    
    figura = plt.figure()
    figura.suptitle("IDPSO-ELM-S: c = 0.5", fontsize=11, fontweight='bold')
    grafico1 = figura.add_subplot(1, 2, 1)
    grafico1.grid(True)
    grafico1.bar(x, fa_s, width, align='center', color = 'Blue', label = 'qtds')
    grafico1.legend()
    plt.ylabel('False Alarms')
    plt.xlabel('Number of Sensors')
    grafico1.axis([-1, 5, min(fa_s)-lim_fa, max(fa_s)+lim_fa])
    grafico1.set_xticks(x)
    grafico1.set_xticklabels(param_s)
    plt.show(True)
    
    grafico2 = figura.add_subplot(1, 2, 2)
    grafico2.grid(True)
    grafico2.bar(x, atrasos_s, width, align='center', color = 'Blue',  label = 'qtds')
    grafico2.legend()
    plt.ylabel('Atrasos')
    plt.xlabel('Parâmetros')
    grafico2.axis([-1, 5, min(atrasos_s)-lim_atrasos, max(atrasos_s)+lim_atrasos])
    grafico2.set_xticks(x)
    grafico2.set_xticklabels(param_s)
    plt.show(True)
    ############################################################################################################
    
    ################################-0.75-#################################
    atrasos_s = [4011.056667,    3905.813333,    4044.356667,    4050.228333,    4098.958333]
    fa_s = [18.48166667,   18.14,    17.85333333,    17.64166667,    17.605]
    
    figura = plt.figure()
    figura.suptitle("IDPSO-ELM-S: c = 0.75", fontsize=11, fontweight='bold')
    grafico1 = figura.add_subplot(1, 1, 1)
    grafico1.grid(True)
    grafico1.bar(x, fa_s, width, align='center', color = 'Blue')
    grafico1.legend()
    grafico1.axis([-1, 5, min(fa_s)-lim_fa, max(fa_s)+lim_fa])
    grafico1.set_xticks(x)
    grafico1.set_xticklabels(param_s)
    plt.tick_params(labelsize= 18)
    plt.ylabel('False Alarms', fontsize= 18)
    plt.xlabel('Number of Sensors', fontsize=18)
    plt.grid(True)
    plt.show()
    
    '''
    grafico2 = figura.add_subplot(1, 2, 2)
    grafico2.grid(True)
    grafico2.bar(x, atrasos_s, width, align='center', color = 'Blue',  label = 'qtds')
    grafico2.legend()
    plt.ylabel('Atrasos')
    plt.xlabel('Parâmetros')
    grafico2.axis([-1, 5, min(atrasos_s)-lim_atrasos, max(atrasos_s)+lim_atrasos])
    grafico2.set_xticks(x)
    grafico2.set_xticklabels(param_s)
    plt.show(True)
    '''
    ############################################################################################################
    
    ################################-1-#################################
    atrasos_s = [5119.00,    5149.35,    5346.00,    5150.80,    5106.23]
    fa_s = [10.10, 10.13, 9.40, 9.075, 9.28]
    
    figura = plt.figure()
    figura.suptitle("IDPSO-ELM-S: c = 1", fontsize=11, fontweight='bold')
    grafico1 = figura.add_subplot(1, 2, 1)
    grafico1.grid(True)
    grafico1.bar(x, fa_s, width, align='center', color = 'Blue', label = 'qtds')
    grafico1.legend()
    plt.ylabel('Falsos Alarmes')
    plt.xlabel('Parâmetros')
    grafico1.axis([-1, 5, min(fa_s)-lim_fa, max(fa_s)+lim_fa])
    grafico1.set_xticks(x)
    grafico1.set_xticklabels(param_s)
    
    '''
    grafico2 = figura.add_subplot(1, 2, 2)
    grafico2.grid(True)
    grafico2.bar(x, atrasos_s, width, align='center', color = 'Blue',  label = 'qtds')
    grafico2.legend()
    plt.ylabel('Atrasos')
    plt.xlabel('Parâmetros')
    grafico2.axis([-1, 5, min(atrasos_s)-lim_atrasos, max(atrasos_s)+lim_atrasos])
    grafico2.set_xticks(x)
    grafico2.set_xticklabels(param_s)
    '''
    plt.show(True)
    ############################################################################################################

    '''
    ############################################################################################################
    tecnica = 'IDPSO-ELM-S - qtd 4; w = 1'
    param_ecdd = ['qtd 4; w = 1']
    atrasos_ecdd = [5400.15]
    fa_ecdd = [5.775]
    #cr.PlotarCurva(atrasos_ecdd, fa_ecdd, param_ecdd, tecnica)
    plt.plot(atrasos_ecdd, fa_ecdd, 'bo', color = 'Red')
    plt.plot(atrasos_ecdd, fa_ecdd, label = tecnica)
    plt.legend()
    for i in range(len(param_ecdd)):
        plt.text(atrasos_ecdd[i], fa_ecdd[i], param_ecdd[i])
    ############################################################################################################
    
    ############################################################################################################
    tecnica = 'Cpt+Sensor'
    param_ecdd = ['0', '0.25', '0.5', '0.75', '1']
    atrasos_ecdd = [1013.1, 1536.225, 2522.45, 4088.025, 5173.35]
    fa_ecdd = [37.05, 28.825, 18.25, 11.925, 6.175]
    #cr.PlotarCurva(atrasos_ecdd, fa_ecdd, param_ecdd, tecnica)
    plt.plot(atrasos_ecdd, fa_ecdd, 'bo', color = 'Gray')
    plt.plot(atrasos_ecdd, fa_ecdd, label = tecnica, color = 'Gray')
    plt.legend()
    for i in range(len(param_ecdd)):
        plt.text(atrasos_ecdd[i], fa_ecdd[i], param_ecdd[i])
    ############################################################################################################
    
    
    
    ############################################################################################################
    tecnica = 'IDPSO-ELM-B'
    param_ecdd = ['1', '2', '3', '4', '5']
    atrasos_ecdd = [915.425, 1262.875, 1836.575, 2607.8, 3541.325]
    fa_ecdd = [37.625, 34.15, 30.65, 27.15, 23.4]
    #cr.PlotarCurva(atrasos_ecdd, fa_ecdd, param_ecdd, tecnica)
    plt.plot(atrasos_ecdd, fa_ecdd, 'bo', color = 'Purple')
    plt.plot(atrasos_ecdd, fa_ecdd, label = tecnica, color = 'Purple')
    plt.legend()
    for i in range(len(param_ecdd)):
        plt.text(atrasos_ecdd[i], fa_ecdd[i], param_ecdd[i])
    ############################################################################################################
    
    
    plt.show()
    '''
    
if __name__ == "__main__":
    main()
    
    
    