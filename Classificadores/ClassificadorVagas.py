import json
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from ClassesDeAuxilio.Vaga import Vaga
from sklearn import tree
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score
from sklearn.model_selection import GridSearchCV

class ClassificadorVagas:

    nome = "classificador_de_vagas"
    vagas = []
    teste = []
    
    def classificador(self):
        print("%s trabalhando" % self.nome)
        file_path = "/home/henrique/Documents/Desenvolvimento/Python/Datasets/vagas.json"
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
        ##print(len(test))
        #Separando descricao e tagVaga em duas arrays
        train_x = [x.descricao for x in training]
        train_y = [x.tagVaga for x in training]
        test_x = [x.descricao for x in test]
        test_y = [x.tagVaga for x in test]
       

        #Rodando o algoritimo de bag of words
        vectorizer = TfidfVectorizer()
        train_x_vectors = vectorizer.fit_transform(train_x) #Cria os vetores em formato numerico
        test_x_vectors = vectorizer.transform(test_x) #Cria os vetores em formato numerico
        #Tunando os algoritimos
        parameters = {'kernel':('linear', 'poly', 'rbf'),
                     'C': (1, 2, 4, 8, 10, 16, 32, 64)}
        #svc = svm.SVC()
        #clf_svm_tunned = GridSearchCV(svc, parameters, cv=5, verbose=10)
        #clf_svm_tunned.fit(train_x_vectors, train_y)
        print()
        print()
        #Usando o algoritimo de svm
        clf_svm = svm.SVC(kernel = 'linear')
        clf_svm = clf_svm.fit(train_x_vectors, train_y)
        
        print(test_x[0])
        print(test_y[0])
        print("--------------------------")
        print(clf_svm.predict(test_x_vectors[0]))