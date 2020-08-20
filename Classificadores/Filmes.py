from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn import decomposition, ensemble
import warnings
with warnings.catch_warnings():  
    warnings.filterwarnings("ignore",category=FutureWarning)
    import pandas, xgboost, numpy, textblob, string
    from keras.preprocessing import text, sequence
    from keras import layers, models, optimizers



class Filmes:

    nome = "classificador_de_filmes"


    def classificador(self):
            print("%s trabalhando" % self.nome)