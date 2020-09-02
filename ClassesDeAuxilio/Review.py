import random

class Review:
    def __init__(self,text,score):
        self.text = text
        self.score = score
        self.sentiment = self.getSentiment()

    def getSentiment(self):
        if self.score <= 2:
            self.sentiment = 'NEGATIVE'
        elif self.score >=4:
            self.sentiment = 'POSITIVE'
        else:
            self.sentiment = 'NEUTRAL'
        return self.sentiment

    def balancear(reviews):
        #print(reviews[0].sentiment)
        positive = []
        neutral = []
        negative = []
        cargaBalanceada = []
        for entrada in reviews:
            if entrada.sentiment == 'POSITIVE':
                positive.append(entrada)
            elif entrada.sentiment == 'NEUTRAL':
                neutral.append(entrada)
            else:
                negative.append(entrada)
        
        #print("POSITIVOS: %d" % len(positive))
        #print("NEUTROS: %d" % len(neutral))
        #print("NEGATIVOS: %d" % len(negative))

        positive = positive[0:len(negative)]
        neutral = neutral[0:len(negative)]
        #print("POSITIVOS: %d" % len(positive))
        #print("NEUTROS: %d" % len(neutral))
        #print("NEGATIVOS: %d" % len(negative))    
        cargaBalanceada = positive + neutral + negative
        print(cargaBalanceada[0])
        print()
        random.shuffle(cargaBalanceada)
        print(cargaBalanceada[0])
        return cargaBalanceada
        
