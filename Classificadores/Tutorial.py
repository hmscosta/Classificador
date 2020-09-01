import json
from ClassesDeAuxilio.Review import Review
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import tree
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score
class Tutorial:

    nome = "classificador_tutorial"
    file_path = "/home/henrique/Documents/Desenvolvimento/Python/Datasets/Books_small.json"
    reviews = []

    def classificador(self):
        print("%s trabalhando" % self.nome)
        arquivo = open(self.file_path,"r")
        for line in arquivo:
            review = json.loads(line)
            self.reviews.append(Review(review['reviewText'], review['overall']))
        arquivo.close()
        
        #Separando os dados em teste e treinamento
        training, test = train_test_split(self.reviews, test_size=0.33, random_state=42)
        print(len(training))
        print(len(test))
        #Separando score e text em duas arrays
        train_x = [x.text for x in training]
        train_y = [x.sentiment for x in training]
        test_x = [x.text for x in test]
        test_y = [x.sentiment for x in test]
        #Vetorizando (bag of words)
        vectorizer = CountVectorizer()
        train_x_vectors = vectorizer.fit_transform(train_x) #Cria os vetores em formato numerico
        test_x_vectors = vectorizer.transform(test_x) #Cria os vetores em formato numerico
        #Usando o algoritimo de decision tree
        clf_tree = tree.DecisionTreeClassifier()
        clf_tree = clf_tree.fit(train_x_vectors, train_y)
        print(clf_tree.predict(test_x_vectors[0:5]))
        #Usando o algoritimo de LogisticRegression
        clf_lre = LogisticRegression()
        clf_lre = clf_lre.fit(train_x_vectors, train_y)
        print(clf_lre.predict(test_x_vectors[0:5]))
        #Usando o algoritimo de Naive Bayes
        clf_gnb = GaussianNB()
        #gnb = gnb.fit(train_x, train_y)
        #print(gnb.predict(test_x_vectors[0:5]))


        #Comparando a eficiencia dos modelos (MEAN ACCURACY)
        print()
        print("-------- Avaliando os modelos --------")
        print("\nMEAN ACCURACY")
        print("\nDecision Tree: %.3f" % clf_tree.score(test_x_vectors,test_y))
        print("LogisticRegression: %.3f" % clf_lre.score(test_x_vectors,test_y))
        #Comparando a eficiencia dos modelos (F1 SCORES)
        print("\nF1 SCORES\n")
        print(f1_score(test_y, clf_tree.predict(test_x_vectors), average = None, labels = ['POSITIVE','NEUTRAL','NEGATIVE']))
        print(f1_score(test_y, clf_lre.predict(test_x_vectors), average = None, labels = ['POSITIVE','NEUTRAL','NEGATIVE']))