import card as ca
class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self,name):  # dễ
        self.name=name
        self.listBai=[]


    @property
    def point(self):  # trung bình
        sum=self.listBai[0].rank+self.listBai[1].rank+self.listBai[2].rank
        if sum <=10:
           sum=sum
        else:
            if sum%10==0:
                sum=10
            else:
                sum=sum%10
        return sum

    '''
            Tìm lá bài lớn nhất
            Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
            '''

    @property
    def biggest_card(self):
        maxValue = self.listBai[0]
        if self.listBai[1].__gt__(maxValue)==self.listBai[1]:
            maxValue=self.listBai[1]
        if self.listBai[2].__gt__(maxValue)==self.listBai[2]:
            maxValue=self.listBai[2]
        return maxValue

    def add_card(self,labai):
        self.listBai.append(labai)


    '''Reset bộ bài khi chơi game mới'''
    def remove_card(self):
        self.listBai=[]

    '''Lật bài, hiển thị các lá bài '♠', '♣', '♦', '♥'''
    def flip_card(self):
        print(f'{self.name}   {self.listBai[0].rank}{self.listBai[0].suit} {self.listBai[1].rank}{self.listBai[1].suit} {self.listBai[2].rank}{self.listBai[2].suit} Điểm:{self.point} Lá bài lớn nhất:',end='')
        self.biggest_card.__str__()


# pl=Player("lan")
# pl.listBai.append(ca.Card(9,"♣"))
# pl.listBai.append(ca.Card(8,"♣"))
# pl.listBai.append(ca.Card(6,"♣"))
# print(pl.point)
#
#
