import pandas as pd
from sklearn import datasets

class Tutorial:

    nome = "classificador_tutorial"


    def classificador(self):
        print("%s trabalhando" % self.nome)
        iris = datasets.load_iris()
        digits = datasets.load_digits()
        print(digits.data)
           