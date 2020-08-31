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
        ##print(self.vagas[0].descricao)
        ##print(self.vagas[0].tagVaga)
        #Separando os dados em teste e treinamento
        training, test = train_test_split(self.vagas, test_size=0.33, random_state=42)
        print(len(training))
        print(len(test))
        #Separando descricao e tagVaga em duas arrays
        train_x = [x.descricao for x in training]
        train_y = [x.tagVaga for x in training]
        test_x = [x.descricao for x in test]
        test_y = [x.tagVaga for x in test]
       

        #Rodando o algoritimo de bag of words
        vectorizer = CountVectorizer()
        train_x_vectors = vectorizer.fit_transform(train_x) #Cria os vetores em formato numerico
        ##print(train_x[0])    #Primeira linha de texto
        ##rint(train_x_vectors[0].toarray()) #Vetor numerico que representa a primeira linha de texto
        ##print(vectorizer.get_feature_names())
        #print(train_y)