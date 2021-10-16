import deck as dec
import player as pla
import card as ca

class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self,lisNguoi=[]):
        self.lisNguoi=lisNguoi
        self.boBai= dec.Deck()
    def setup(self):
        print("chào mưng bạn đến với game bài 3 cây")
        print("Nhập số lượng người chơi:")
        n= int(input())
        while(n>5):
            print("chỉ cho tối đa 5 người chơi")
            n = int(input("nhập lại số lượng người chơi:"))
        i = 1
        self.lisNguoi = []
        while(n!=0):
            name=input(f"Tên người chơi thứ {i}: ")
            i=i+1
            pla.Player(name)
            self.lisNguoi.append(pla.Player(name))
            n=n-1

    def list_players(self):
        print(f"| {'ID':9} | {'Name':15}")
        for i in range (0,len(self.lisNguoi)):
            print(f"| {i:9} | {self.lisNguoi[i].name:15}")
#thêm mới nhười chơi
    def add_player(self):
        name = input(f"Tên người chơi tiếp theo:")
        if len(self.lisNguoi)<=5:
            self.lisNguoi.append(pla.Player(name))
        else:
            print("số người chơi đã đủ")
#xóa 1 người chơi
    def remove_player(self,id):
       del self.lisNguoi[id]
#chia bài cho người chơi
    def deal_card(self):
        self.boBai.shuffle_card()
        for i in range(0,len(self.lisNguoi)):
            self.lisNguoi[i].add_card(self.boBai.deal_card())
            self.lisNguoi[i].add_card(self.boBai.deal_card())
            self.lisNguoi[i].add_card(self.boBai.deal_card())
        for i in self.boBai.liscard:
                i.__str__()
#lật bái cho tất cả người chơi, thông báo người chiến t:hắng
    def flip_card(self):
        diem=[]
        for i in range(0,len(self.lisNguoi)):
          self.lisNguoi[i].flip_card()
          diem.append(self.lisNguoi[i].point)
        lismax=[]
        #print(max(diem))
        for i in range(0,len(self.lisNguoi)):
            if self.lisNguoi[i].point==max(diem):
                lismax.append(self.lisNguoi[i])
        one=lismax[0]
        if len(lismax)==1:
           print(f'người chơi chiến thắng:',end='')
           lismax[0].flip_card()
        else:
            for i in lismax:
                car= ca.Card(i.biggest_card.rank,i.biggest_card.suit)
                car1=ca.Card(one.biggest_card.rank,one.biggest_card.suit)
                if car.__gt__(car1) == car:
                    one = i
            print(f'người chơi chiến thắng:', end='')
            one.flip_card()

# ga=Game()
# ga.setup()
# ga.deal_card()
# ga.flip_card()