'''
Created on 13 de fev de 2017

@author: gusta
'''
import numpy as np

class Metricas_previsao():
    '''
    Classe para instanciar as metricas de previsao  
    '''
    pass

    def mean_absolute_percentage_error(self, y_true, y_pred): 
        '''
        Metodo para computar a metrica MAPE
        :param y_true: lista com os dados reais
        :param y_pred: lista com as previsoes
        :return: retorna a metrica para o conjunto apresentado 
        '''
        
        if(type(y_true) == np.ndarray):
            
            erros = []
            for i in range(len(y_true)):
                
                if(y_pred[i:i+1] == 0):
                    y_pred[i:i+1] = 0.01
                    
                if(y_true[i:i+1] == 0):
                    y_true[i:i+1] = 0.01
            
                erro = np.abs((y_true[i:i+1] - y_pred[i:i+1]) / y_true[i:i+1]) * 100
                erros.append(erro)
                
            return np.mean(erros)
        
        else:
            y_true = np.asarray(y_true)
            y_pred = np.asarray(y_pred)
            
            if(y_pred == 0):
                y_pred = 0.01
            
            if(y_true == 0):
                y_true = 0.01
        
            mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
            
            return mape

def main():
    y_true = [3, -0.5, 2, 7] 
    y_pred = [2.5, -0.3, 2, 8]
    
    mp = Metricas_previsao()
    mape = mp.mean_absolute_percentage_error(y_true, y_pred)
    
    print("MAPE:", mape)

if __name__ == "__main__":
    main()  