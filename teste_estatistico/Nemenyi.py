#-*- coding: utf-8 -*-
'''
Created on 24 de mai de 2017

@author: gusta
'''
from scipy.stats import rankdata, norm
from scipy.special import gammaln
import numpy as np
import Orange.evaluation as ora
import matplotlib.pyplot as plt

class Ler_dados():
    pass

    def obter_dados_arquivo(self, caminho_tabela, linhas, colunas):
        '''
        método para gerar plots do teste estatístico
        :param: caminho_tabela: string, referente ao caminho que a tabela se encontra
        :param: linhas: vetor inteiro, contendo o inicio da linha e o final dos dados para serem usados no teste
        :param: colunas: vetor inteiro, contendo o inicio da coluna e o final dos dados para serem usados no teste
        '''
        # importando lib que abre o arquivo
        import xlrd
        # abrindo um workbook e copiando ele em uma variavel auxiliar
        book = xlrd.open_workbook(caminho_tabela)
        # obtendo a quantidade de folhas 
        i = len(book.sheet_names())
        # abrindo a folha existente
        sh = book.sheet_by_index(i-1)
            
        # obtendo a quantidade linhas dentro da folha
        linha_inicial = linhas[0]
        linha_final = linhas[1]
        
        # obtendo a quantidade colunas dentro da folha
        coluna_inicial = colunas[0]
        coluna_final = colunas[1]
            
        # variavel para salvar a primeira coluna das caminho_tabela
        labels = []
        acuracias = []
        
        # for para a quantidade de colunas
        for j in range(coluna_inicial, coluna_final+1):
            # for para percorrer as linhas de cada coluna
            for k in range(0, 1):
                # copiando o valor referente a linha e coluna passada
                valor = sh.cell_value(rowx=k, colx=j)
                labels.append(valor)
                
                
        # for para a quantidade de colunas
        for j in range(coluna_inicial, coluna_final+1):
            # variavel para salvar os valores de cada coluna
            valores = []
            # for para percorrer as linhas de cada coluna
            for k in range(linha_inicial, linha_final):
                # copiando o valor referente a linha e coluna passada
                valor = sh.cell_value(rowx=k, colx=j)
                valores.append(valor)
            # salvando o conjunto de acuracias    
            acuracias.append(np.asarray(valores))
        # convertendo a lista final em um array
        acuracias = np.asarray(acuracias)
            
        return labels, acuracias

class NemenyiTestPostHoc():
    def __init__(self, labels, data):
        self._noOfGroups = data.shape[0]
        self._noOfSamples = data.shape[1]
        self.labels = labels
        self._data = data

    def do(self):
        dataAsRanks = np.full(self._data.shape, np.nan)
        for i in range(self._noOfSamples):
            dataAsRanks[:, i] = rankdata(self._data[:, i])
        meansOfRanksOfDependentSamples = np.mean(dataAsRanks, 1)
        qValues = self._compareStatisticsOfAllPairs(meansOfRanksOfDependentSamples)
        pValues = self._calculatePValues(qValues)

        return meansOfRanksOfDependentSamples, pValues

    def _compareStatisticsOfAllPairs(self, meansOfRanks):
        noOfMeansOfRanks = len(meansOfRanks)
        compareResults = np.zeros((noOfMeansOfRanks-1, noOfMeansOfRanks))
        for i in range(noOfMeansOfRanks-1):
            for j in range(i+1, noOfMeansOfRanks):
                compareResults[i][j] = self._compareStatisticsOfSinglePair((meansOfRanks[i], meansOfRanks[j]))
        return compareResults

    def _compareStatisticsOfSinglePair(self, meansOfRanksPair):
        diff = abs(meansOfRanksPair[0] - meansOfRanksPair[1])
        qval = diff / np.sqrt(self._noOfGroups * (self._noOfGroups + 1) / (6 * self._noOfSamples))
        return qval * np.sqrt(2)

    def _calculatePValues(self, qValues):
        for qRow in qValues:
            for i in range(len(qRow)):
                qRow[i] = self._ptukey(qRow[i], 1, self._noOfGroups, np.inf)
        return 1 - qValues

    def _wprob(self, w, rr, cc):
        nleg = 12
        ihalf = 6

        C1 = -30
        C2 = -50
        C3 = 60
        M_1_SQRT_2PI = 1 / np.sqrt(2 * np.pi)
        bb = 8
        wlar = 3
        wincr1 = 2
        wincr2 = 3
        xleg = [
            0.981560634246719250690549090149,
            0.904117256370474856678465866119,
            0.769902674194304687036893833213,
            0.587317954286617447296702418941,
            0.367831498998180193752691536644,
            0.125233408511468915472441369464
        ]
        aleg = [
            0.047175336386511827194615961485,
            0.106939325995318430960254718194,
            0.160078328543346226334652529543,
            0.203167426723065921749064455810,
            0.233492536538354808760849898925,
            0.249147045813402785000562436043
        ]

        qsqz = w * 0.5

        if qsqz >= bb:
            return 1.0

        # find (f(w/2) - 1) ^ cc
        # (first term in integral of hartley's form).

        pr_w = 2 * norm.cdf(qsqz) - 1
        if pr_w >= np.exp(C2 / cc):
            pr_w = pr_w ** cc
        else:
            pr_w = 0.0

        # if w is large then the second component of the
        # integral is small, so fewer intervals are needed.

        wincr = wincr1 if w > wlar else wincr2

        # find the integral of second term of hartley's form
        # for the integral of the range for equal-length
        # intervals using legendre quadrature.  limits of
        # integration are from (w/2, 8).  two or three
        # equal-length intervals are used.

        # blb and bub are lower and upper limits of integration.

        blb = qsqz
        binc = (bb - qsqz) / wincr
        bub = blb + binc
        einsum = 0.0

        # integrate over each interval

        cc1 = cc - 1.0
        for wi in range(1, wincr + 1):
            elsum = 0.0
            a = 0.5 * (bub + blb)

            # legendre quadrature with order = nleg

            b = 0.5 * (bub - blb)

            for jj in range(1, nleg + 1):
                if (ihalf < jj):
                    j = (nleg - jj) + 1
                    xx = xleg[j-1]
                else:
                    j = jj
                    xx = -xleg[j-1]
                c = b * xx
                ac = a + c

                # if exp(-qexpo/2) < 9e-14
                # then doesn't contribute to integral

                qexpo = ac * ac
                if qexpo > C3:
                    break

                pplus = 2 * norm.cdf(ac)
                pminus = 2 * norm.cdf(ac, w)

                # if rinsum ^ (cc-1) < 9e-14, */
                # then doesn't contribute to integral */

                rinsum = (pplus * 0.5) - (pminus * 0.5)
                if (rinsum >= np.exp(C1 / cc1)):
                    rinsum = (aleg[j-1] * np.exp(-(0.5 * qexpo))) * (rinsum ** cc1)
                    elsum += rinsum

            elsum *= (((2.0 * b) * cc) * M_1_SQRT_2PI)
            einsum += elsum
            blb = bub
            bub += binc

        # if pr_w ^ rr < 9e-14, then return 0
        pr_w += einsum
        if pr_w <= np.exp(C1 / rr):
            return 0

        pr_w = pr_w ** rr
        if (pr_w >= 1):
            return 1
        return pr_w

    def _ptukey(self, q, rr, cc, df):

        M_LN2 = 0.69314718055994530942

        nlegq = 16
        ihalfq = 8

        eps1 = -30.0
        eps2 = 1.0e-14
        dhaf = 100.0
        dquar = 800.0
        deigh = 5000.0
        dlarg = 25000.0
        ulen1 = 1.0
        ulen2 = 0.5
        ulen3 = 0.25
        ulen4 = 0.125
        xlegq = [
            0.989400934991649932596154173450,
            0.944575023073232576077988415535,
            0.865631202387831743880467897712,
            0.755404408355003033895101194847,
            0.617876244402643748446671764049,
            0.458016777657227386342419442984,
            0.281603550779258913230460501460,
            0.950125098376374401853193354250e-1
        ]
        alegq = [
            0.271524594117540948517805724560e-1,
            0.622535239386478928628438369944e-1,
            0.951585116824927848099251076022e-1,
            0.124628971255533872052476282192,
            0.149595988816576732081501730547,
            0.169156519395002538189312079030,
            0.182603415044923588866763667969,
            0.189450610455068496285396723208
        ]

        if q <= 0:
            return 0

        if (df < 2) or (rr < 1) or (cc < 2):
            return float('nan')

        if np.isfinite(q) is False:
            return 1

        if df > dlarg:
            return self._wprob(q, rr, cc)

        # in fact we don't need the code below and majority of variables:

        # calculate leading constant

        f2 = df * 0.5
        f2lf = ((f2 * np.log(df)) - (df * M_LN2)) - gammaln(f2)
        f21 = f2 - 1.0

        # integral is divided into unit, half-unit, quarter-unit, or
        # eighth-unit length intervals depending on the value of the
        # degrees of freedom.

        ff4 = df * 0.25
        if df <= dhaf:
            ulen = ulen1
        elif df <= dquar:
            ulen = ulen2
        elif df <= deigh:
            ulen = ulen3
        else:
            ulen = ulen4

        f2lf += np.log(ulen)

        ans = 0.0

        for i in range(1, 51):
            otsum = 0.0

            # legendre quadrature with order = nlegq
            # nodes (stored in xlegq) are symmetric around zero.

            twa1 = (2*i - 1) * ulen

            for jj in range(1, nlegq + 1):
                if (ihalfq < jj):
                    j = jj - ihalfq - 1
                    t1 = (f2lf + (f21 * np.log(twa1 + (xlegq[j] * ulen)))) - (((xlegq[j] * ulen) + twa1) * ff4)
                else:
                    j = jj - 1
                    t1 = (f2lf + (f21 * np.log(twa1 - (xlegq[j] * ulen)))) + (((xlegq[j] * ulen) - twa1) * ff4)

                # if exp(t1) < 9e-14, then doesn't contribute to integral
                if t1 >= eps1:
                    if ihalfq < jj:
                        qsqz = q * np.sqrt(((xlegq[j] * ulen) + twa1) * 0.5)
                    else:
                        qsqz = q * np.sqrt(((-(xlegq[j] * ulen)) + twa1) * 0.5)

                    wprb = self._wprob(qsqz, rr, cc)
                    rotsum = (wprb * alegq[j]) * np.exp(t1)
                    otsum += rotsum

            # if integral for interval i < 1e-14, then stop.
            # However, in order to avoid small area under left tail,
            # at least  1 / ulen  intervals are calculated.

            if (i * ulen >= 1.0) and (otsum <= eps2):
                break

            ans += otsum

        return min(1, ans)

# consistent with https://cran.r-project.org/web/packages/PMCMR/vignettes/PMCMR.pdf p. 17

    def gerar_plot(self, nome, caminho):
        
        #emparelhando as acuracias de cada modelo
        #print(friedmanchisquare(self._data[0], self._data[1], self._data[2], self._data[3], self._data[4], self._data[5]))
        
        #obtendo os rankins dos modelos e os pvalues
        meanRanks, pValues = self.do()
        #print("Média dos rankings: ")
        #print(meanRanks)
        
        #print("Pvalues: ")
        #print(pValues)
        
        #computando as estatisticas a partir do rank dos modelos
        cd = ora.compute_CD(meanRanks, len(self._data[0]), alpha="0.05", test="nemenyi")
        
        # criando o plot com os rankings, labels e distancia critica
        ora.graph_ranks(meanRanks, self.labels, cd=cd, width=10, textspace=2)

        # salvando a figura        
        plt.savefig(caminho+nome)
        
        print("Teste gerado!")
        #plt.show()
    
    def Exemplo_executavel(self):
        #acuracias dos modelos, cada coluna é um modelo
        data = np.asarray([(3.88, 5.64, 5.76, 4.25, 5.91, 4.33), 
                           (30.58, 30.14, 16.92, 23.19, 26.74, 10.91),
                           (25.24, 33.52, 25.45, 18.85, 20.45, 26.67), 
                           (4.44, 7.94, 4.04, 4.4, 4.23, 4.36),
                           (29.41, 30.72, 32.92, 28.23, 23.35, 12), 
                           (38.87, 33.12, 39.15, 28.06, 38.23, 26.65)])
        
        #label dos modelos, cada coluna é um modelo
        names_alg = ["alg1", 
                     "alg2", 
                     "alg3", 
                     "alg4", 
                     "alg5", 
                     "alg6"]
        
        #computando o nemenyi posthuc
        nemenyi = NemenyiTestPostHoc(names_alg, data)
        nemenyi.gerar_plot("teste", "../Tabelas/Experimentos/Preliminares/")
        
def main():
    
    tbt = Ler_dados()
    caminho_arquivo = 'E:/Workspace2/Framework_drift/tabelas/Experimentos/Exp Acur - Param Min/tabela_mape_param_min.xls'
    caminho_salvar = 'E:/Workspace2/Framework_drift/tabelas/Experimentos/Exp Acur - Param Min'
    
    #lin grad
    labels, acuracias = tbt.obter_dados_arquivo(caminho_arquivo, [1, 31], [1, 9]) 
    nemenyi = NemenyiTestPostHoc(labels, acuracias)
    nemenyi.gerar_plot("/friedman_lin_grad", caminho_salvar)
    
    #lin abt
    labels, acuracias = tbt.obter_dados_arquivo(caminho_arquivo, [32, 61], [1, 9]) 
    nemenyi = NemenyiTestPostHoc(labels, acuracias)
    nemenyi.gerar_plot("/friedman_lin_abt", caminho_salvar)
    
    #nlin grad
    labels, acuracias = tbt.obter_dados_arquivo(caminho_arquivo, [62, 91], [1, 9]) 
    nemenyi = NemenyiTestPostHoc(labels, acuracias)
    nemenyi.gerar_plot("/friedman_nlin_grad", caminho_salvar)
    
    #nlin abt
    labels, acuracias = tbt.obter_dados_arquivo(caminho_arquivo, [92, 121], [1, 9]) 
    nemenyi = NemenyiTestPostHoc(labels, acuracias)
    nemenyi.gerar_plot("/friedman_nlin_abt", caminho_salvar)
    
    #saz
    labels, acuracias = tbt.obter_dados_arquivo(caminho_arquivo, [122, 151], [1, 9]) 
    nemenyi = NemenyiTestPostHoc(labels, acuracias)
    nemenyi.gerar_plot("/friedman_saz", caminho_salvar)
    
    #hib
    labels, acuracias = tbt.obter_dados_arquivo(caminho_arquivo, [152, 181], [1, 9]) 
    nemenyi = NemenyiTestPostHoc(labels, acuracias)
    nemenyi.gerar_plot("/friedman_hib", caminho_salvar)
    
    #geral
    labels, acuracias = tbt.obter_dados_arquivo(caminho_arquivo, [1, 181], [1, 9]) 
    nemenyi = NemenyiTestPostHoc(labels, acuracias)
    nemenyi.gerar_plot("/friedman_geral", caminho_salvar)
    

if __name__ == '__main__':
    main()
    