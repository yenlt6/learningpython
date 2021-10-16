class Card:
    '''
    Class đại diện cho mỗi lá bài

    Mỗi lá bài bao gồm rank ('A', 2, 3, 4, 5, 6, 7, 8, 9) và suit ('♠', '♣', '♦', '♥')
    '''

    def __init__(self,rank,suit):
        self.setRank=rank
        self.suit=suit
        self.setsuitNumber=suit
        self.setRankA=rank

    @property
    def getRank(self):
        return self.rank

    @getRank.setter
    def setRank(self, rank):
        if rank == 'A':
            self.rank = 1
        elif rank <= 2 and rank >= 9:
            print("Rank khong hop le")
        else:
            self.rank = rank

    @property
    def getRankA(self):
        return self.rankA

    @getRank.setter
    def setRankA(self, rank):
        if rank == 'A':
            self.rankA = 'A'
        else:
            self.rankA=None
    @property
    def getSuitNumber(self):
        return self.suitNumber

    @getSuitNumber.setter
    def setsuitNumber(self,suit):
        if  suit=='♠':
            self.suitNumber=1
        elif suit=='♣':
            self.suitNumber=2
        elif suit=='♦':
            self.suitNumber=4
        elif suit=='♥':
            self.suitNumber=3

    def __str__(self):
        if self.rankA=='A':
            print(f'{self.rankA}{self.suit}')
        else:
            print(f'{self.rank}{self.suit}')

    def __gt__(self, Card):
       if self.rank>Card.rank:
           return self
       elif self.rank==Card.rank:
           if self.suitNumber>Card.suitNumber:
               return self
           elif self.suitNumber==Card.suitNumber:
               return 0;
           else:
               return Card
       else:
           return Card

