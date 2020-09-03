import json
from ClassesDeAuxilio.Review import Review
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn import tree
from sklearn import svm
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import f1_score
class Tutorial:

    nome = "classificador_tutorial"
    file_path = "/home/henrique/Documents/Desenvolvimento/Python/Datasets/Books_small_10000.json"
    reviews = []
    #objetoReview = Review() 
    def classificador(self):
        print("%s trabalhando" % self.nome)
        arquivo = open(self.file_path,"r")
        for line in arquivo:
            review = json.loads(line)
            self.reviews.append(Review(review['reviewText'], review['overall']))
        arquivo.close()
        #Balanceando as entradas
        self.reviews = Review.balancear(self.reviews)
                
        #Separando os dados em teste e treinamento
        training, test = train_test_split(self.reviews, test_size=0.33, random_state=42)
        
        #Separando score e text em duas arrays
        train_x = [x.text for x in training]
        train_y = [x.sentiment for x in training]
        test_x = [x.text for x in test]
        test_y = [x.sentiment for x in test]
        
        #Vetorizando (bag of words)
        vectorizer = TfidfVectorizer()
        train_x_vectors = vectorizer.fit_transform(train_x) #Cria os vetores em formato numerico
        test_x_vectors = vectorizer.transform(test_x) #Cria os vetores em formato numerico
        
        #Usando o algoritimo de svm
        clf_svm = svm.SVC(kernel = 'linear')
        clf_svm = clf_svm.fit(train_x_vectors, train_y)
                
        #Usando o algoritimo de decision tree
        clf_tree = tree.DecisionTreeClassifier()
        clf_tree = clf_tree.fit(train_x_vectors, train_y)
        #print(clf_tree.predict(test_x_vectors[0:5]))
        
        #Usando o algoritimo de LogisticRegression
        clf_lre = LogisticRegression()
        clf_lre = clf_lre.fit(train_x_vectors, train_y)
        print(train_y.count('POSITIVE'))
        print(train_y.count('NEUTRAL'))
        print(train_y.count('NEGATIVE'))
        
        #Usando o algoritimo de Naive Bayes
        clf_gnb = GaussianNB()
        #gnb = gnb.fit(train_x, train_y)
        #print(gnb.predict(test_x_vectors[0:5]))

        #Comparando a eficiencia dos modelos (MEAN ACCURACY)
        print()
        print("-------- Avaliando os modelos --------")
        print("\nMEAN ACCURACY")
        print("\nSVM: %.3f" % clf_svm.score(test_x_vectors,test_y))
        print("Decision Tree: %.3f" % clf_tree.score(test_x_vectors,test_y))
        print("LogisticRegression: %.3f" % clf_lre.score(test_x_vectors,test_y))
        
        #Comparando a eficiencia dos modelos (F1 SCORES)
        print("\nF1 SCORES\n")
        scores_svm = f1_score(test_y, clf_svm.predict(test_x_vectors), average = None, labels = ['POSITIVE','NEUTRAL','NEGATIVE'])
        scores_tree = f1_score(test_y, clf_tree.predict(test_x_vectors), average = None, labels = ['POSITIVE','NEUTRAL','NEGATIVE'])
        scores_lre = f1_score(test_y, clf_lre.predict(test_x_vectors), average = None, labels = ['POSITIVE','NEUTRAL','NEGATIVE'])
        print("SVM")
        print("\n Positive: %.3f \n Neutral: %.3f \n Negative: %.3f \n" % (scores_svm[0], scores_svm[1], scores_svm[2] ) )
        print()
        print("Decision Tree")
        print("\n Positive: %.3f \n Neutral: %.3f \n Negative: %.3f \n" % (scores_tree[0], scores_tree[1], scores_tree[2] ) )
        print()
        print("Logistic Regression")
        print("\n Positive: %.3f \n Neutral: %.3f \n Negative: %.3f \n" % (scores_lre[0], scores_lre[1], scores_lre[2] ) )