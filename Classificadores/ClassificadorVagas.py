import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from ClassesDeAuxilio.Vaga import Vaga

class ClassificadorVagas:

    nome = "classificador_de_vagas"
    vagas = []
    def classificador(self):
        print("%s trabalhando" % self.nome)
        file_path = "/home/henrique/Documents/Desenvolvimento/Python/Aprendizado/PythonScrap/texto/vagas.json"
        arquivo = open(file_path,"r")
        for line in arquivo:
            review = json.loads(line)
            for cont in range(len(review)):
                self.vagas.append(Vaga(review[cont]['descricaoVaga'], review[cont]['tagVaga']))
        arquivo.close()

        print(self.vagas[0].descricao)
        print(self.vagas[0].tagVaga)