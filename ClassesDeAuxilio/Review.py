

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