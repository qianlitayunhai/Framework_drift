#-*- coding: utf-8 -*-

'''
Created on 23 de ago de 2017

@author: gusta
'''


class Constantes():
    def __init__(self, alocacao):
        self.qtd_execucoes = 5
        self.variacao_inicio = 1
        self.variacao_final = 3
        #self.pasta = "Teste"
        #self.pasta = "Deteccao"
        #self.pasta = "Deteccao (B e BS)"
        #self.pasta = "preliminares"
        #self.pasta = "Acuracia_adpt"
        #self.pasta = "Desempenho Series Financeiras"
        #self.pasta = "Reais Drifts"
        #self.pasta = "FEDD (0.1)"
        self.pasta = "Reais Drifts- sem retorno"
        #self.pasta = "Deteccao art RPSO"
        
        if(alocacao == 'dentro'):
            self.caminho_bases = "../tabelas/Experimentos/"
        elif(alocacao == 'fora'):
            self.caminho_bases = "tabelas/Experimentos/"
        
        #self.folhas = ["ELM", "ELM-DDM", "ELM-ECDD", "ELM-FEDD", "IDPSO-ELM-B", "IDPSO-ELM-S", "IDPSO-ELM-SV", "P-IDPSO-ELM-SV", "M-IDPSO-ELM-SV", "RPSO", "RPSO-ELM"]
        #self.folhas = ["ELM-DDM", "ELM-ECDD", "ELM-FEDD", "IDPSO-ELM-B", "IDPSO-ELM-S", "IDPSO-ELM-SV", "P-IDPSO-ELM-SV", "M-IDPSO-ELM-SV"]
        #self.folhas = ["ELM_DDM", "ELM_ECDD", "ELM-FEDD", "IDPSO-ELM-B", "IDPSO-ELM-S", "IDPSO-ELM-SV", "IDPSO-ELM-BS"]
        #self.folhas = ["P-IDPSO-ELM-SV", "M-IDPSO-ELM-SV"]
        #self.folhas = ["ELM-FEDD"]
        #self.folhas = ["ELM_DDM", "ELM_ECDD", "ELM-FEDD", "IDPSO-ELM-B", "IDPSO-ELM-S", "IDPSO-ELM-SV", "P-IDPSO-ELM-SV", "M-IDPSO-ELM-SV" ]
        self.folhas = ["RPSO-ELM"]
        
        