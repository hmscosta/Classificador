import json
from ClassesDeAuxilio.Review import Review
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
        print(self.reviews[0].score)


           