import json
from ClassesDeAuxilio.Review import Review
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
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
        #Separando score e text em duas arrays
        train_x = [x.text for x in training]
        train_y = [x.sentiment for x in training]
        test_x = [x.text for x in test]
        test_y = [x.sentiment for x in test]
        

        
        #Rodando o algoritimo de bag of words
        vectorizer = CountVectorizer()
        train_x_vectors = vectorizer.fit_transform(train_x) #Cria os vetores em formato numerico
        print(train_x[0])    #Primeira linha de texto
        print(train_x_vectors[0].toarray()) #Vetor numerico que representa a primeira linha de texto

        #print(vectorizer.get_feature_names())  #Printa todas as features(o dicionario das palavras)
        
           