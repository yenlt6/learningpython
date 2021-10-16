class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    Mỗi lá bài bao gồm rank ('A', 2, 3, 4, 5, 6, 7, 8, 9) và suit ('G', 'H', 'J', 'K')
    '''

    def __init__(self,rank,suit):
        self.rank=rank
        self.suit=suit
      

    def __str__(self):
        '''Hiển thị lá bài'''
        return f'Card({self.rank},{self.suit})'
       

    def __gt__(self, other):
        '''So sánh 2 lá bài'''
    def __gt__(self, other):        
        val1 = 0
        val2 = 0        
        if self.rank>other.rank:
            return True
        elif self.rank==other.rank and self.suit>other.suit:
            return True
        else:
            return False
    
    def card_function(self):
        print("Yeeennn")
        pass
           