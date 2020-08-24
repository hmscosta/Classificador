import pandas as pd
from sklearn.datasets import fetch_20newsgroups
class Filmes:

    nome = "classificador_de_filmes"


    def classificador(self):
        print("%s trabalhando" % self.nome)
        categories = ['alt.atheism', 'soc.religion.christian','comp.graphics', 'sci.med']
        twenty_train = fetch_20newsgroups(subset='train',categories=categories, shuffle=True, random_state=42)
        print(twenty_train.target_names)
        
           