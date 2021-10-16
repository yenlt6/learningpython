import card as ca
import random
class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''
    def __init__(self):
       self.liscard=self.build()

    def build(self):
        listRank=["A",2,3,4,5,6,7,8,9]
        listSuit={'♠','♣','♦','♥'}
        listCard=[]
        for i in range (0, len(listRank)):
            for j in listSuit:
                card= ca.Card(listRank[i],j)
                listCard.append(card)
        return listCard
#trộn bài
    def shuffle_card(self):
        random.shuffle(self.liscard)
#Rút một lá bài từ bộ bài
    def deal_card(self):
       labai=self.liscard.pop()
       return labai



