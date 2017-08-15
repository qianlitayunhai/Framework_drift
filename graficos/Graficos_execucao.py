#-*- coding: utf-8 -*-
'''
Created on 19 de abr de 2017

@author: gusta
'''
import matplotlib.pyplot as plt

class Grafico():
    pass    

    def Plotar_graficos_dow_drift(self, stream, predicoes_vetor, deteccoes, alarmes, erro_stream_vetor, n, atrasos, falsos_alarmes, tempo_execucao, MAE=None, nome=None):
        '''
        Metodo para plotar tanto o grafico de previsao, erro no data stream e as deteccoes para a serie real Down Jones Industrial Average
        :param grafico: variavel booleana
        :param stream: data stream
        :param predicoes_vetor: vetor de previsoes
        :param deteccoes: deteccoes encontradas
        :param erro_stream_vetor: erro do data stream
        :return: plot de previsao, erro do data stream e deteccoes
        '''
        
        #estilo de algumas funcoes do grafico
        largura_deteccoes_verdadeiras = 2
        largura_deteccoes = 2
        estilo = 'dashed'
        cor_dados_reais = 'Blue'
        cor_previsao = 'Red'
        cor_erro = 'Blue'
        cor_deteccao_verdadeira = 'Green'
        cor_deteccao_encontrada = '#00BFFF'
        cor_falsos_alarmes = 'Magenta'
        cor_alarmes = '#FF7F27'
        cor_retreinamento = 'Gray'
        cor_online = 'Yellow'
        cor_alpha_retreinamento = 0.15
        alpha_avisos = 0.2
        
        localizacao_legenda = [1.13, 0.85]
        
        
        eixox = [0] * 2
        eixox[0] = 0
        eixox[1] = 650
        eixoy = [0] * 2
        eixoy[0] = -0.3
        eixoy[1] = 1.3
        erro_eixoy = [0] * 2
        erro_eixoy[0] = 0
        erro_eixoy[1] = 1
        x_intervalos = range(eixox[0], eixox[1]+100, 50)
        
        label_deteccao_verdadeira = 'Real Change'
        label_deteccao_encontrada = 'Change Found'
        label_alarme_falso = 'False Alarms'
        label_aviso = 'Nível de Aviso'
        label_retreinamento = 'Retreining'
        label_online = 'Online'

        #deteccoes verdadeiras
        deteccoes_reais = [24, 307, 510]
        
            
        #criando uma figura
        figura = plt.figure()
        if(nome != None):
            figura.suptitle(nome, fontsize=11, fontweight='bold')
    
        #definindo a figura 1 com a previsao e os dados reais
        grafico1 = figura.add_subplot(2, 10, (1, 9))
        grafico1.plot(stream, label = 'Original Serie', color = cor_dados_reais)
        grafico1.plot(predicoes_vetor, label = 'Forecast', color = cor_previsao)
        
        if(MAE == None):
            grafico1.set_title("Previsão e dados reais")
        else:
            grafico1.set_title("Previsão e dados reais - MAE: " + str(MAE))
            
        #plotando as deteccoes verdadeiras
        for i in range(len(deteccoes_reais)):
            contador2 = deteccoes_reais[i]
            if(i == 0):
                grafico1.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, label = label_deteccao_verdadeira, color=cor_deteccao_verdadeira)
            else:
                grafico1.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, color=cor_deteccao_verdadeira)
        
        
        auxiliar = [False] * 9
        primeiro_false = False
        
        #inserindo os labels
        grafico1.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_alarme_falso, color=cor_falsos_alarmes, alpha = alpha_avisos)
        #grafico1.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_aviso, color=cor_alarmes)
        grafico1.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_deteccao_encontrada, color=cor_deteccao_encontrada)
        grafico1.axvspan(-1000, -1000+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, label = label_retreinamento, zorder=10)
        grafico1.axvspan(-1100, -1000, facecolor=cor_online, alpha=cor_alpha_retreinamento, label = label_online)
        
        
        #plotando as deteccoes encontradas
        if(len(deteccoes) > 0):
            
            for i in range(len(alarmes)):
                grafico1.axvline(alarmes[i], linewidth=largura_deteccoes, linestyle=estilo, color=cor_alarmes, alpha = alpha_avisos)
            
            
            for i in range(len(deteccoes)):
                contador = deteccoes[i]
                    
                if(deteccoes[i] < deteccoes_reais[0]):
                    
                    if(primeiro_false == False):
                        primeiro_false = True
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                    else:
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
    
                # x >= 5000 e x < 10000     
                if(deteccoes[i] >= deteccoes_reais[0] and deteccoes[i] < deteccoes_reais[1]):      
                    
                    if(auxiliar[0] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        
                    if(auxiliar[0] == False):
                        
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        
                        if(primeiro_false == False):
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        auxiliar[0] = True
                       
                    
                # x >= 10000 e x < 15000
                if(deteccoes[i] >= deteccoes_reais[1] and deteccoes[i] < deteccoes_reais[2]):      
                    
                    if(auxiliar[1] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        
                    if(auxiliar[1] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        auxiliar[1] = True
                       
                #x >= 45000
                if(deteccoes[i] >= deteccoes_reais[2]):      
                    
                    if(auxiliar[2] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        
                    if(auxiliar[2] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        auxiliar[2] = True
                
                if(i == 0):
                    grafico1.axvspan(0, deteccoes[i], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                    
                    if(len(deteccoes) > 1):
                        grafico1.axvspan(contador+n, deteccoes[i+1], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                    else:
                        grafico1.axvspan(contador+n, eixox[1], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                        
                elif(i != len(deteccoes)-1):
                    grafico1.axvspan(contador+n, deteccoes[i+1], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                else:    
                    grafico1.axvspan(contador+n, eixox[1], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                
                
        
        
                        
        #colocando legenda e definindo os eixos do grafico                        
        plt.ylabel('Observations')
        plt.xlabel('Time')
        grafico1.axis([eixox[0], eixox[1], 0, 1])
        grafico1.legend(loc='upper center', bbox_to_anchor=(localizacao_legenda[0], localizacao_legenda[1]), ncol=1, fancybox=True, shadow=True)
        plt.xticks(x_intervalos, rotation = 45)
        
        texto = (" Alarmes Falsos: %.2f | Atrasos:  %.2f | Tempo de execução: %.2f " %(falsos_alarmes, atrasos, tempo_execucao))
        
        grafico1.annotate(texto,
                    xy=(0.5, 0.4), xytext=(0, 0),
                    xycoords=('axes fraction', 'figure fraction'),
                    textcoords='offset points',
                    size=14, ha='center', va='bottom', bbox=dict(boxstyle="round", fc="w", ec="0", alpha=1))
        
        #definindo a figura 2 com o erro de previsao
        grafico2 = figura.add_subplot(3, 10, (21, 29))
        grafico2.plot(erro_stream_vetor, label = 'Erro de Previsão', color = cor_erro)
        grafico2.set_title("Erro de Previsão")
        
        #Definindo os labels
        grafico2.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_alarme_falso, color=cor_falsos_alarmes)
        grafico2.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_deteccao_encontrada, color=cor_deteccao_encontrada)
        grafico2.axvspan(-1000, -1000+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, label = label_retreinamento)
            
        #plotando as deteccoes verdadeiras
        for i in range(len(deteccoes_reais)):
            contador2 = deteccoes_reais[i]
                
            if(i == 0):
                grafico2.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, label = label_deteccao_verdadeira, color=cor_deteccao_verdadeira)
            else:
                grafico2.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, color=cor_deteccao_verdadeira)
            
        
        auxiliar = [False] * 9
        primeiro_false = False
        
        #plotando as deteccoes encontradas
        if(len(deteccoes) > 0):
            for i in range(len(deteccoes)):
                contador = deteccoes[i]
                    
                if(deteccoes[i] < deteccoes_reais[0]):
                    
                    if(primeiro_false == False):
                        primeiro_false = True
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                    else:
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
    
                # x >= 5000 e x < 10000     
                if(deteccoes[i] >= deteccoes_reais[0] and deteccoes[i] < deteccoes_reais[1]):      
                    
                    if(auxiliar[0] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[0] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[0] = True
                       
                    
                # x >= 10000 e x < 15000
                if(deteccoes[i] >= deteccoes_reais[1] and deteccoes[i] < deteccoes_reais[2]):      
                    
                    if(auxiliar[1] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[1] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[1] = True
                       
                #x >= 45000
                if(deteccoes[i] >= deteccoes_reais[2]):      
                    
                    if(auxiliar[2] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[2] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[2] = True

        #colocando legenda e definindo os eixos do grafico
        plt.ylabel('MAE')
        plt.xlabel('Tempo')
        grafico2.legend(loc='upper center', bbox_to_anchor=(localizacao_legenda[0], localizacao_legenda[1]), ncol=1, fancybox=True, shadow=True)
        grafico2.axis([eixox[0], eixox[1], erro_eixoy[0], erro_eixoy[1]])
        plt.xticks(x_intervalos, rotation = 45)
        
        #mostrando o grafico                                        
        plt.show()
    
    def Plotar_graficos_cnt(self, stream, predicoes_vetor, deteccoes, alarmes, erro_stream_vetor, n, atrasos, falsos_alarmes, tempo_execucao, MAE=None, nome=None):
        '''
        Metodo para plotar tanto o grafico de previsao, erro no data stream e as deteccoes das series do artigo ICTAI
        :param grafico: variavel booleana
        :param stream: data stream
        :param predicoes_vetor: vetor de previsoes
        :param deteccoes: deteccoes encontradas
        :param erro_stream_vetor: erro do data stream
        :return: plot de previsao, erro do data stream e deteccoes
        '''
        
        #estilo de algumas funcoes do grafico
        largura_deteccoes_verdadeiras = 2
        largura_deteccoes = 2
        estilo = 'dashed'
        cor_dados_reais = 'Blue'
        cor_previsao = 'Red'
        cor_erro = 'Blue'
        cor_deteccao_verdadeira = 'Green'
        cor_deteccao_encontrada = '#00BFFF'
        cor_falsos_alarmes = 'Magenta'
        cor_alarmes = '#FF7F27'
        cor_retreinamento = 'Gray'
        cor_online = 'Yellow'
        cor_alpha_retreinamento = 0.15
        alpha_avisos = 0.2
        
        localizacao_legenda = [1.13, 0.85]
        
        
        eixox = [0] * 2
        eixox[0] = 0
        eixox[1] = 20000
        eixoy = [0] * 2
        eixoy[0] = -0.3
        eixoy[1] = 1.3
        erro_eixoy = [0] * 2
        erro_eixoy[0] = 0
        erro_eixoy[1] = 0.2
        x_intervalos = range(eixox[0], eixox[1]+500, 500)
        
        label_deteccao_verdadeira = 'Real Change'
        label_deteccao_encontrada = 'Change Found'
        label_alarme_falso = 'False Alarms'
        label_aviso = 'Nível de Aviso'
        label_retreinamento = 'Retreining'
        label_online = 'Online'

        #deteccoes verdadeiras
        deteccoes_reais = [2000-n, 4000-n, 6000-n, 8000-n, 10000-n, 12000-n, 14000-n, 16000-n, 18000-n]
        
            
        #criando uma figura
        figura = plt.figure()
        if(nome != None):
            figura.suptitle(nome, fontsize=11, fontweight='bold')
    
        #definindo a figura 1 com a previsao e os dados reais
        grafico1 = figura.add_subplot(2, 10, (1, 9))
        grafico1.plot(stream, label = 'Original Serie', color = cor_dados_reais)
        grafico1.plot(predicoes_vetor, label = 'Forecast', color = cor_previsao)
        
        if(MAE == None):
            grafico1.set_title("Previsão e dados reais")
        else:
            grafico1.set_title("Previsão e dados reais - MAE: " + str(MAE))
            
        #plotando as deteccoes verdadeiras
        for i in range(len(deteccoes_reais)):
            contador2 = deteccoes_reais[i]
            if(i == 0):
                grafico1.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, label = label_deteccao_verdadeira, color=cor_deteccao_verdadeira)
            else:
                grafico1.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, color=cor_deteccao_verdadeira)
        
        
        auxiliar = [False] * 9
        primeiro_false = False
        
        #inserindo os labels
        grafico1.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_alarme_falso, color=cor_falsos_alarmes, alpha = alpha_avisos)
        #grafico1.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_aviso, color=cor_alarmes)
        grafico1.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_deteccao_encontrada, color=cor_deteccao_encontrada)
        grafico1.axvspan(-1000, -1000+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, label = label_retreinamento, zorder=10)
        grafico1.axvspan(-1100, -1000, facecolor=cor_online, alpha=cor_alpha_retreinamento, label = label_online)
        
        
        #plotando as deteccoes encontradas
        if(len(deteccoes) > 0):
            
            for i in range(len(alarmes)):
                grafico1.axvline(alarmes[i], linewidth=largura_deteccoes, linestyle=estilo, color=cor_alarmes, alpha = alpha_avisos)
            
            
            for i in range(len(deteccoes)):
                contador = deteccoes[i]
                    
                if(deteccoes[i] < deteccoes_reais[0]):
                    
                    if(primeiro_false == False):
                        primeiro_false = True
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                    else:
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
    
                # x >= 5000 e x < 10000     
                if(deteccoes[i] >= deteccoes_reais[0] and deteccoes[i] < deteccoes_reais[1]):      
                    
                    if(auxiliar[0] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        
                    if(auxiliar[0] == False):
                        
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        
                        if(primeiro_false == False):
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        auxiliar[0] = True
                       
                    
                # x >= 10000 e x < 15000
                if(deteccoes[i] >= deteccoes_reais[1] and deteccoes[i] < deteccoes_reais[2]):      
                    
                    if(auxiliar[1] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        
                    if(auxiliar[1] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        auxiliar[1] = True
                       
                # x >= 15000 e x < 20000
                if(deteccoes[i] >= deteccoes_reais[2] and deteccoes[i] < deteccoes_reais[3]):      
                    
                    if(auxiliar[2] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        
                    if(auxiliar[2] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        auxiliar[2] = True
                        
                # x >= 20000 e x < 25000
                if(deteccoes[i] >= deteccoes_reais[3] and deteccoes[i] < deteccoes_reais[4]):      
                    
                    if(auxiliar[3] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        
                    if(auxiliar[3] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        auxiliar[3] = True
                       
                # x >= 25000 e x < 30000
                if(deteccoes[i] >= deteccoes_reais[4] and deteccoes[i] < deteccoes_reais[5]):      
                    
                    if(auxiliar[4] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        
                    if(auxiliar[4] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        auxiliar[4] = True
                       
                # x >= 30000 e x < 35000
                if(deteccoes[i] >= deteccoes_reais[5] and deteccoes[i] < deteccoes_reais[6]):      
                    
                    if(auxiliar[5] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        
                    if(auxiliar[5] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        auxiliar[5] = True
                       
                # x >= 35000 e x < 40000
                if(deteccoes[i] >= deteccoes_reais[6] and deteccoes[i] < deteccoes_reais[7]):      
                    
                    if(auxiliar[6] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        
                    if(auxiliar[6] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        auxiliar[6] = True
                       
                # x >= 40000 e x < 45000
                if(deteccoes[i] >= deteccoes_reais[7] and deteccoes[i] < deteccoes_reais[8]):      
                    
                    if(auxiliar[7] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        
                    if(auxiliar[7] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        auxiliar[7] = True
                       
                #x >= 45000
                if(deteccoes[i] >= deteccoes_reais[8]):      
                    
                    if(auxiliar[8] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        
                    if(auxiliar[8] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, zorder=10)
                        auxiliar[8] = True
                
                if(i == 0):
                    grafico1.axvspan(0, deteccoes[i], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                    
                    if(len(deteccoes) > 1):
                        grafico1.axvspan(contador+n, deteccoes[i+1], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                    else:
                        grafico1.axvspan(contador+n, eixox[1], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                        
                elif(i != len(deteccoes)-1):
                    grafico1.axvspan(contador+n, deteccoes[i+1], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                else:    
                    grafico1.axvspan(contador+n, eixox[1], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                
                
        
        
                        
        #colocando legenda e definindo os eixos do grafico                        
        plt.ylabel('Observations')
        plt.xlabel('Time')
        grafico1.axis([eixox[0], eixox[1], 0, 1])
        grafico1.legend(loc='upper center', bbox_to_anchor=(localizacao_legenda[0], localizacao_legenda[1]), ncol=1, fancybox=True, shadow=True)
        plt.xticks(x_intervalos, rotation = 45)
        
        texto = (" Alarmes Falsos: %.2f | Atrasos:  %.2f | Tempo de execução: %.2f " %(falsos_alarmes, atrasos, tempo_execucao))
        
        grafico1.annotate(texto,
                    xy=(0.5, 0.4), xytext=(0, 0),
                    xycoords=('axes fraction', 'figure fraction'),
                    textcoords='offset points',
                    size=14, ha='center', va='bottom', bbox=dict(boxstyle="round", fc="w", ec="0", alpha=1))
        
        #definindo a figura 2 com o erro de previsao
        grafico2 = figura.add_subplot(3, 10, (21, 29))
        grafico2.plot(erro_stream_vetor, label = 'Erro de Previsão', color = cor_erro)
        grafico2.set_title("Erro de Previsão")
        
        #Definindo os labels
        grafico2.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_alarme_falso, color=cor_falsos_alarmes)
        grafico2.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_deteccao_encontrada, color=cor_deteccao_encontrada)
        grafico2.axvspan(-1000, -1000+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, label = label_retreinamento)
            
        #plotando as deteccoes verdadeiras
        for i in range(len(deteccoes_reais)):
            contador2 = deteccoes_reais[i]
                
            if(i == 0):
                grafico2.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, label = label_deteccao_verdadeira, color=cor_deteccao_verdadeira)
            else:
                grafico2.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, color=cor_deteccao_verdadeira)
            
        
        auxiliar = [False] * 9
        primeiro_false = False
        
        #plotando as deteccoes encontradas
        if(len(deteccoes) > 0):
            for i in range(len(deteccoes)):
                contador = deteccoes[i]
                    
                if(deteccoes[i] < deteccoes_reais[0]):
                    
                    if(primeiro_false == False):
                        primeiro_false = True
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                    else:
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
    
                # x >= 5000 e x < 10000     
                if(deteccoes[i] >= deteccoes_reais[0] and deteccoes[i] < deteccoes_reais[1]):      
                    
                    if(auxiliar[0] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[0] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[0] = True
                       
                    
                # x >= 10000 e x < 15000
                if(deteccoes[i] >= deteccoes_reais[1] and deteccoes[i] < deteccoes_reais[2]):      
                    
                    if(auxiliar[1] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[1] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[1] = True
                       
                # x >= 15000 e x < 20000
                if(deteccoes[i] >= deteccoes_reais[2] and deteccoes[i] < deteccoes_reais[3]):      
                    
                    if(auxiliar[2] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[2] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[2] = True
                        
                # x >= 20000 e x < 25000
                if(deteccoes[i] >= deteccoes_reais[3] and deteccoes[i] < deteccoes_reais[4]):      
                    
                    if(auxiliar[3] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[3] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[3] = True
                       
                # x >= 25000 e x < 30000
                if(deteccoes[i] >= deteccoes_reais[4] and deteccoes[i] < deteccoes_reais[5]):      
                    
                    if(auxiliar[4] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[4] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[4] = True
                       
                # x >= 30000 e x < 35000
                if(deteccoes[i] >= deteccoes_reais[5] and deteccoes[i] < deteccoes_reais[6]):      
                    
                    if(auxiliar[5] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[5] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[5] = True
                       
                # x >= 35000 e x < 40000
                if(deteccoes[i] >= deteccoes_reais[6] and deteccoes[i] < deteccoes_reais[7]):      
                    
                    if(auxiliar[6] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[6] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[6] = True
                       
                # x >= 40000 e x < 45000
                if(deteccoes[i] >= deteccoes_reais[7] and deteccoes[i] < deteccoes_reais[8]):      
                    
                    if(auxiliar[7] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[7] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[7] = True
                       
                #x >= 45000
                if(deteccoes[i] >= deteccoes_reais[8]):      
                    
                    if(auxiliar[8] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[8] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[8] = True

        #colocando legenda e definindo os eixos do grafico
        plt.ylabel('MAE')
        plt.xlabel('Tempo')
        grafico2.legend(loc='upper center', bbox_to_anchor=(localizacao_legenda[0], localizacao_legenda[1]), ncol=1, fancybox=True, shadow=True)
        grafico2.axis([eixox[0], eixox[1], erro_eixoy[0], erro_eixoy[1]])
        plt.xticks(x_intervalos, rotation = 45)
        
        #mostrando o grafico                                        
        plt.show()
    
    def Plotar_graficos_gerador(self, stream, predicoes_vetor, deteccoes, alarmes, erro_stream_vetor, n, atrasos, falsos_alarmes, conceitos_pulados, tempo_execucao, MAE=None, nome=None):
        '''
        Metodo para plotar tanto o grafico de previsao, erro no data stream e as deteccoes
        :param grafico: variavel booleana
        :param stream: data stream
        :param predicoes_vetor: vetor de previsoes
        :param deteccoes: deteccoes encontradas
        :param erro_stream_vetor: erro do data stream
        :return: plot de previsao, erro do data stream e deteccoes
        '''
        
        #estilo de algumas funcoes do grafico
        largura_deteccoes_verdadeiras = 3
        largura_deteccoes = 3
        largura_avisos = 1
        estilo = 'dashed'
        cor_dados_reais = 'Blue'
        cor_previsao = 'Red'
        cor_erro = 'Blue'
        cor_deteccao_verdadeira = 'Green'
        cor_deteccao_encontrada = '#00BFFF'
        cor_falsos_alarmes = 'Magenta'
        cor_alarmes = '#FF7F27'
        cor_retreinamento = 'Gray'
        cor_online = 'Yellow'
        alpha_retreinamento = 0.15
        alpha_avisos = 0.2
        
        localizacao_legenda = [1.13, 1]
        
        
        eixox = [0] * 2
        eixox[0] = 0
        eixox[1] = 19800
        eixoy = [0] * 2
        eixoy[0] = -0.3
        eixoy[1] = 1.3
        erro_eixoy = [0] * 2
        erro_eixoy[0] = 0
        erro_eixoy[1] = 0.2
        x_intervalos = range(eixox[0], eixox[1], 500)
        
        label_deteccao_verdadeira = 'Mudança Real'
        label_deteccao_encontrada = 'Detecção Encontrada'
        label_alarme_falso = 'Alarmes Falsos'
        label_aviso = 'Nível de Aviso'
        label_retreinamento = 'Retreinamento'
        label_online = 'Online'

        #deteccoes verdadeiras
        deteccoes_reais = [2000-n, 4000-n, 6000-n, 8000-n, 10000-n, 12000-n, 14000-n, 16000-n, 18000-n]
        
            
        #criando uma figura
        figura = plt.figure()
        if(nome != None):
            figura.suptitle(nome, fontsize=11, fontweight='bold')
    
        #definindo a figura 1 com a previsao e os dados reais
        grafico1 = figura.add_subplot(2, 10, (1, 9))
        grafico1.plot(stream, label = 'Série original', color = cor_dados_reais)
        grafico1.plot(predicoes_vetor, label = 'Previsão', color = cor_previsao)
        
        if(MAE == None):
            grafico1.set_title("Previsão e dados reais")
        else:
            grafico1.set_title("Previsão e dados reais - MAE: " + str(MAE))
            
        #plotando as deteccoes verdadeiras
        for i in range(len(deteccoes_reais)):
            contador2 = deteccoes_reais[i]
            if(i == 0):
                grafico1.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, label = label_deteccao_verdadeira, color=cor_deteccao_verdadeira)
            else:
                grafico1.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, color=cor_deteccao_verdadeira)
        
        
        auxiliar = [False] * 9
        primeiro_false = False
        
        #inserindo os labels
        grafico1.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_alarme_falso, color=cor_falsos_alarmes)
        grafico1.axvline(-1000, linewidth=largura_avisos, linestyle=estilo, label = label_aviso, color=cor_alarmes, alpha = alpha_avisos)
        grafico1.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_deteccao_encontrada, color=cor_deteccao_encontrada)
        grafico1.axvspan(-1000, -1000+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento, label = label_retreinamento)
        grafico1.axvspan(-1100, -1000, facecolor=cor_online, alpha=alpha_retreinamento, label = label_online)
        
        
        #printando quando retreina depois de pular um conceito
        for i in range(len(conceitos_pulados)):
            grafico1.axvspan(conceitos_pulados[i], conceitos_pulados[i]+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
        
        #printando no grafico o periodo em que o modelo ficou online
        aux_min = False
        aux_max = False
        
        for i in range(1, len(erro_stream_vetor)):
            
            if(erro_stream_vetor[i] != None and aux_min == False):
                min = i
                aux_min = True
                
            if(erro_stream_vetor[i] == None or i == len(erro_stream_vetor)-1):
                max = i
                aux_max = True
                
            if(aux_min == True and aux_max == True):
                grafico1.axvspan(min, max, facecolor=cor_online, alpha=alpha_retreinamento)
                aux_min = False
                aux_max = False
        
        #plotando as deteccoes encontradas
        if(len(deteccoes) > 0):
            
            for i in range(len(alarmes)):
                grafico1.axvline(alarmes[i], linewidth=largura_avisos, linestyle=estilo, color=cor_alarmes, alpha = alpha_avisos)
            
            
            for i in range(len(deteccoes)):
                contador = deteccoes[i]
                    
                if(deteccoes[i] < deteccoes_reais[0]):
                    
                    if(primeiro_false == False):
                        primeiro_false = True
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                    else:
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
    
                # x >= 5000 e x < 10000     
                if(deteccoes[i] >= deteccoes_reais[0] and deteccoes[i] < deteccoes_reais[1]):      
                    
                    if(auxiliar[0] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[0] == False):
                        
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        
                        if(primeiro_false == False):
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[0] = True
                       
                    
                # x >= 10000 e x < 15000
                if(deteccoes[i] >= deteccoes_reais[1] and deteccoes[i] < deteccoes_reais[2]):      
                    
                    if(auxiliar[1] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[1] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[1] = True
                       
                # x >= 15000 e x < 20000
                if(deteccoes[i] >= deteccoes_reais[2] and deteccoes[i] < deteccoes_reais[3]):      
                    
                    if(auxiliar[2] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[2] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[2] = True
                        
                # x >= 20000 e x < 25000
                if(deteccoes[i] >= deteccoes_reais[3] and deteccoes[i] < deteccoes_reais[4]):      
                    
                    if(auxiliar[3] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[3] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[3] = True
                       
                # x >= 25000 e x < 30000
                if(deteccoes[i] >= deteccoes_reais[4] and deteccoes[i] < deteccoes_reais[5]):      
                    
                    if(auxiliar[4] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[4] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[4] = True
                       
                # x >= 30000 e x < 35000
                if(deteccoes[i] >= deteccoes_reais[5] and deteccoes[i] < deteccoes_reais[6]):      
                    
                    if(auxiliar[5] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[5] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[5] = True
                       
                # x >= 35000 e x < 40000
                if(deteccoes[i] >= deteccoes_reais[6] and deteccoes[i] < deteccoes_reais[7]):      
                    
                    if(auxiliar[6] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[6] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[6] = True
                       
                # x >= 40000 e x < 45000
                if(deteccoes[i] >= deteccoes_reais[7] and deteccoes[i] < deteccoes_reais[8]):      
                    
                    if(auxiliar[7] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[7] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[7] = True
                       
                #x >= 45000
                if(deteccoes[i] >= deteccoes_reais[8]):      
                    
                    if(auxiliar[8] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[8] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[8] = True
                
                        
        #colocando legenda e definindo os eixos do grafico                        
        plt.ylabel('Valor das observações')
        plt.xlabel('Tempo')
        grafico1.axis([eixox[0], eixox[1], 0, 1])
        grafico1.legend(loc='upper center', bbox_to_anchor=(localizacao_legenda[0], localizacao_legenda[1]), ncol=1, fancybox=True, shadow=True)
        plt.xticks(x_intervalos, rotation = 45)
        
        texto = (" Alarmes Falsos: %.2f | Atrasos:  %.2f | Tempo de execução: %.2f " %(falsos_alarmes, atrasos, tempo_execucao))
        
        grafico1.annotate(texto,
                    xy=(0.5, 0.4), xytext=(0, 0),
                    xycoords=('axes fraction', 'figure fraction'),
                    textcoords='offset points',
                    size=14, ha='center', va='bottom', bbox=dict(boxstyle="round", fc="w", ec="0", alpha=1))
        
        #definindo a figura 2 com o erro de previsao
        grafico2 = figura.add_subplot(3, 10, (21, 29))
        grafico2.plot(erro_stream_vetor, label = 'Erro de Previsão', color = cor_erro)
        grafico2.set_title("Erro de Previsão")
        
        #Definindo os labels
        grafico2.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_alarme_falso, color=cor_falsos_alarmes)
        grafico2.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_deteccao_encontrada, color=cor_deteccao_encontrada)
        grafico2.axvspan(-1000, -1000+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento, label = label_retreinamento)
            
        
        #printando quando retreina depois de pular um conceito
        for i in range(len(conceitos_pulados)):
            grafico2.axvspan(conceitos_pulados[i], conceitos_pulados[i]+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
        
        #plotando as deteccoes verdadeiras
        for i in range(len(deteccoes_reais)):
            contador2 = deteccoes_reais[i]
                
            if(i == 0):
                grafico2.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, label = label_deteccao_verdadeira, color=cor_deteccao_verdadeira)
            else:
                grafico2.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, color=cor_deteccao_verdadeira)
            
        
        auxiliar = [False] * 9
        primeiro_false = False
        
        #plotando as deteccoes encontradas
        if(len(deteccoes) > 0):
            for i in range(len(deteccoes)):
                contador = deteccoes[i]
                    
                if(deteccoes[i] < deteccoes_reais[0]):
                    
                    if(primeiro_false == False):
                        primeiro_false = True
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                    else:
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
    
                # x >= 5000 e x < 10000     
                if(deteccoes[i] >= deteccoes_reais[0] and deteccoes[i] < deteccoes_reais[1]):      
                    
                    if(auxiliar[0] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[0] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[0] = True
                       
                    
                # x >= 10000 e x < 15000
                if(deteccoes[i] >= deteccoes_reais[1] and deteccoes[i] < deteccoes_reais[2]):      
                    
                    if(auxiliar[1] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[1] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[1] = True
                       
                # x >= 15000 e x < 20000
                if(deteccoes[i] >= deteccoes_reais[2] and deteccoes[i] < deteccoes_reais[3]):      
                    
                    if(auxiliar[2] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[2] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[2] = True
                        
                # x >= 20000 e x < 25000
                if(deteccoes[i] >= deteccoes_reais[3] and deteccoes[i] < deteccoes_reais[4]):      
                    
                    if(auxiliar[3] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[3] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[3] = True
                       
                # x >= 25000 e x < 30000
                if(deteccoes[i] >= deteccoes_reais[4] and deteccoes[i] < deteccoes_reais[5]):      
                    
                    if(auxiliar[4] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[4] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[4] = True
                       
                # x >= 30000 e x < 35000
                if(deteccoes[i] >= deteccoes_reais[5] and deteccoes[i] < deteccoes_reais[6]):      
                    
                    if(auxiliar[5] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[5] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[5] = True
                       
                # x >= 35000 e x < 40000
                if(deteccoes[i] >= deteccoes_reais[6] and deteccoes[i] < deteccoes_reais[7]):      
                    
                    if(auxiliar[6] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[6] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[6] = True
                       
                # x >= 40000 e x < 45000
                if(deteccoes[i] >= deteccoes_reais[7] and deteccoes[i] < deteccoes_reais[8]):      
                    
                    if(auxiliar[7] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[7] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[7] = True
                       
                #x >= 45000
                if(deteccoes[i] >= deteccoes_reais[8]):      
                    
                    if(auxiliar[8] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        
                    if(auxiliar[8] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=alpha_retreinamento)
                        auxiliar[8] = True

        #colocando legenda e definindo os eixos do grafico
        plt.ylabel('MAE')
        plt.xlabel('Tempo')
        grafico2.legend(loc='upper center', bbox_to_anchor=(localizacao_legenda[0], localizacao_legenda[1]), ncol=1, fancybox=True, shadow=True)
        grafico2.axis([eixox[0], eixox[1], erro_eixoy[0], erro_eixoy[1]])
        plt.xticks(x_intervalos, rotation = 45)
        
        #mostrando o grafico                                        
        plt.show()
       
    def Plotar_graficos_fedd(self, stream, predicoes_vetor, deteccoes, alarmes, erro_stream_vetor, n, ft_det, atrasos, fa, tempo, MAE=None, nome=None):
        '''
        Metodo para plotar tanto o grafico de previsao, erro no data stream e as deteccoes do artigo FEDD
        :param grafico: variavel booleana
        :param stream: data stream
        :param predicoes_vetor: vetor de previsoes
        :param deteccoes: deteccoes encontradas
        :param erro_stream_vetor: erro do data stream
        :return: plot de previsao, erro do data stream e deteccoes
        '''
        
        #estilo de algumas funcoes do grafico
        largura_deteccoes_verdadeiras = 2
        largura_deteccoes = 2
        estilo = 'dashed'
        cor_dados_reais = 'Blue'
        cor_previsao = 'Red'
        cor_erro = 'Blue'
        cor_deteccao_verdadeira = 'Green'
        cor_deteccao_encontrada = '#00BFFF'
        cor_falsos_alarmes = 'Magenta'
        cor_alarmes = '#FF7F27'
        cor_retreinamento = 'Gray'
        cor_online = 'Yellow'
        cor_alpha_retreinamento = 0.1
        
        localizacao_legenda = [1.13, 0.95]
        
        
        eixox = [0] * 2
        eixox[0] = 0
        eixox[1] = 11500
        eixoy_previsao = [0] * 2
        eixoy_previsao[0] = 2 * min(stream)
        eixoy_previsao[1] = max(stream) + min(stream)
        erro_eixoy = [0] * 2
        erro_eixoy[0] = 0
        erro_eixoy[1] = 0.05
        x_intervalos = range(eixox[0], eixox[1]+500, 500)
        
        label_deteccao_verdadeira = 'Mudança Real'
        label_deteccao_encontrada = 'Detecção Encontrada'
        label_alarme_falso = 'Alarme Falso'
        label_aviso = 'Nível de Aviso'
        label_retreinamento = 'Retreinamento'
        label_online = 'Online'

        #deteccoes verdadeiras
        deteccoes_reais = [2000, 5000, 8000]
        
            
        #criando uma figura
        figura = plt.figure()
        if(nome != None):
            figura.suptitle(nome, fontsize=11, fontweight='bold')
    
        #definindo a figura 1 com a previsao e os dados reais
        grafico1 = figura.add_subplot(2, 10, (1, 9))
        grafico1.plot(stream, label = 'Série original', color = cor_dados_reais)
        grafico1.plot(predicoes_vetor, label = 'Previsão', color = cor_previsao)
        
        if(MAE == None):
            grafico1.set_title("Previsão e dados reais")
        else:
            grafico1.set_title("Previsão e dados reais - MAE: " + str(MAE))
            
        #plotando as deteccoes verdadeiras
        for i in range(len(deteccoes_reais)):
            contador2 = deteccoes_reais[i]
            if(i == 0):
                grafico1.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, label = label_deteccao_verdadeira, color=cor_deteccao_verdadeira)
            else:
                grafico1.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, color=cor_deteccao_verdadeira)
        
        
        auxiliar = [False] * len(deteccoes_reais)
        primeiro_false = False
        
        #inserindo os labels
        grafico1.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_alarme_falso, color=cor_falsos_alarmes)
        grafico1.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_aviso, color=cor_alarmes)
        grafico1.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_deteccao_encontrada, color=cor_deteccao_encontrada)
        grafico1.axvspan(-1000, -1000+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, label = label_retreinamento)
        grafico1.axvspan(-1100, -1000, facecolor=cor_online, alpha=cor_alpha_retreinamento, label = label_online)
        
        
        #plotando as deteccoes encontradas
        if(len(deteccoes) > 0):
            
            for i in range(len(alarmes)):
                grafico1.axvline(alarmes[i], linewidth=largura_deteccoes, linestyle=estilo, color=cor_alarmes)
            
            
            for i in range(len(deteccoes)):
                contador = deteccoes[i]
                    
                #x >= 2000
                if(deteccoes[i] < deteccoes_reais[0]):
                    
                    if(primeiro_false == False):
                        primeiro_false = True
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                    else:
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
    
                # x >= 2000 e x < 5000     
                if(deteccoes[i] >= deteccoes_reais[0] and deteccoes[i] < deteccoes_reais[1]):      
                    
                    if(auxiliar[0] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[0] == False):
                        
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        
                        if(primeiro_false == False):
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[0] = True
                       
                    
                # x >= 5000 e x < 8000
                if(deteccoes[i] >= deteccoes_reais[1] and deteccoes[i] < deteccoes_reais[2]):      
                    
                    if(auxiliar[1] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[1] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[1] = True
                       
                       
                #x >= 8000
                if(deteccoes[i] >= deteccoes_reais[2]):      
                    
                    if(auxiliar[2] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[2] == False):
                        grafico1.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico1.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[2] = True
                
                if(i == 0):
                    grafico1.axvspan(0, deteccoes[i], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                    
                    if(len(deteccoes) > 1):
                        grafico1.axvspan(contador+n, deteccoes[i+1], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                    else:
                        grafico1.axvspan(contador+n, eixox[1], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                        
                elif(i != len(deteccoes)-1):
                    grafico1.axvspan(contador+n, deteccoes[i+1], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                else:    
                    grafico1.axvspan(contador+n, eixox[1], facecolor=cor_online, alpha=cor_alpha_retreinamento)
                
                
        
        
                        
        #colocando legenda e definindo os eixos do grafico                        
        plt.ylabel('Valor das observações')
        plt.xlabel('Tempo')
        grafico1.axis([eixox[0], eixox[1], eixoy_previsao[0], eixoy_previsao[1]])
        grafico1.legend(loc='upper center', bbox_to_anchor=(localizacao_legenda[0], localizacao_legenda[1]), ncol=1, fancybox=True, shadow=True)
        plt.xticks(x_intervalos, rotation = 45)
        
        texto = (" Falta de detecção:  %.2f | Falsos Alarmes: %.2f | Atrasos:  %.2f | Tempo de execução: %.2f " %(ft_det, fa, atrasos, tempo))
        
        grafico1.annotate(texto,
                    xy=(0.5, 0.4), xytext=(0, 0),
                    xycoords=('axes fraction', 'figure fraction'),
                    textcoords='offset points',
                    size=14, ha='center', va='bottom', bbox=dict(boxstyle="round", fc="w", ec="0", alpha=1))
        
        #definindo a figura 2 com o erro de previsao
        grafico2 = figura.add_subplot(3, 10, (21, 29))
        grafico2.plot(erro_stream_vetor, label = 'Erro de Previsão', color = cor_erro)
        grafico2.set_title("Erro de Previsão")
        
        #Definindo os labels
        grafico2.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_alarme_falso, color=cor_falsos_alarmes)
        grafico2.axvline(-1000, linewidth=largura_deteccoes, linestyle=estilo, label = label_deteccao_encontrada, color=cor_deteccao_encontrada)
        grafico2.axvspan(-1000, -1000+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento, label = label_retreinamento)
            
        #plotando as deteccoes verdadeiras
        for i in range(len(deteccoes_reais)):
            contador2 = deteccoes_reais[i]
                
            if(i == 0):
                grafico2.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, label = label_deteccao_verdadeira, color=cor_deteccao_verdadeira)
            else:
                grafico2.axvline(contador2, linewidth=largura_deteccoes_verdadeiras, color=cor_deteccao_verdadeira)
            
        
        auxiliar = [False] * len(deteccoes_reais)
        primeiro_false = False
        
        #plotando as deteccoes encontradas
        if(len(deteccoes) > 0):
            for i in range(len(deteccoes)):
                contador = deteccoes[i]
                    
                
                # x < 2000
                if(deteccoes[i] < deteccoes_reais[0]):
                    
                    if(primeiro_false == False):
                        primeiro_false = True
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                    else:
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
    
                # x >= 2000 e x < 5000     
                if(deteccoes[i] >= deteccoes_reais[0] and deteccoes[i] < deteccoes_reais[1]):      
                    
                    if(auxiliar[0] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                            
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[0] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[0] = True
                       
                    
                # x >= 5000 e x < 8000
                if(deteccoes[i] >= deteccoes_reais[1] and deteccoes[i] < deteccoes_reais[2]):      
                    
                    if(auxiliar[1] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                            
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[1] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[1] = True
                       
                # x >= 8000
                if(deteccoes[i] >= deteccoes_reais[2]):      
                    
                    if(auxiliar[2] == True):
                        
                        if(primeiro_false == False):
                            primeiro_false = True
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        else:
                            grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_falsos_alarmes)
                            grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        
                    if(auxiliar[2] == False):
                        grafico2.axvline(contador, linewidth=largura_deteccoes, linestyle=estilo, color=cor_deteccao_encontrada)
                        grafico2.axvspan(contador, contador+n, facecolor=cor_retreinamento, alpha=cor_alpha_retreinamento)
                        auxiliar[2] = True

        #colocando legenda e definindo os eixos do grafico
        plt.ylabel('MAE')
        plt.xlabel('Tempo')
        grafico2.legend(loc='upper center', bbox_to_anchor=(localizacao_legenda[0], localizacao_legenda[1]), ncol=1, fancybox=True, shadow=True)
        grafico2.axis([eixox[0], eixox[1], erro_eixoy[0], erro_eixoy[1]])
        plt.xticks(x_intervalos, rotation = 45)
        
        #mostrando o grafico                                        
        plt.show()
        
        
def main():
    print()
    
if __name__ == "__main__":
    main() 