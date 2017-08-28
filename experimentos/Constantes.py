#-*- coding: utf-8 -*-

'''
Created on 23 de ago de 2017

@author: gusta
'''


class Constantes():
    def __init__(self, alocacao):
        self.qtd_execucoes = 5
        self.variacao_inicio = 1
        self.variacao_final = 31
        self.pasta = "Deteccao1"
        #self.pasta = "preliminares"
        if(alocacao == 'dentro'):
            self.caminho_bases = "../tabelas/Experimentos/"
        elif(alocacao == 'fora'):
            self.caminho_bases = "tabelas/Experimentos/"
        #self.folhas = ["ELM", "ELM_DDM", "ELM_ECDD", "ELM-FEDD", "IDPSO-ELM-B", "IDPSO-ELM-S", "P-IDPSO-ELM", "M-IDPSO-ELM"]
        self.folhas = ["ELM_DDM", "ELM_ECDD", "ELM-FEDD", "IDPSO-ELM-B", "IDPSO-ELM-S", "IDPSO-ELM-SV", "M-IDPSO-ELM-BS"]
        
        
        