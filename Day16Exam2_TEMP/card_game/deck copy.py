from card import Card
import random

class Deck:
    def __init__(self):
        self.list_card=self.build()
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''
    # ('A', 2, 3, 4, 5, 6, 7, 8, 9) và suit ('G', 'H', 'J', 'K')

    '''Tạo bộ bài: tạo 1 list, mỗi phần tử của list là 1 lá bài gồm 9*4=36 lá bài'''
    def build(self):
        list_card=[]
        list_rank = ['A', 2, 3, 4, 5, 6, 7, 8, 9]
        list_suit = ['G', 'H', 'J', 'K']         
        for rank in list_rank:
            for suit in list_suit:
              list_card.append(Card(rank, suit))
        return  list_card
      

    def shuffle_card(self):
        '''Trộn bài, random(list)'''
        return random.shuffle(self.list_card)

    # def shuffle_card(self,list_card):
    #     '''Trộn bài, random(list)'''
    #     return random.choice(list_card)      

    #Chia bài, gán 1 con bài cho 1 người nào đó.
    def deal_card(self,card_item):
        return self.remove(card_item)
        '''Rút một lá bài từ bộ bài: lấy random 1 lá bài từ bộ bài, tức là lấy random 1 phần tử trong list ra'''

deck=Deck()
print(deck)
list_card_t=deck.shuffle_card
for i in list_card_t:
    print(i)