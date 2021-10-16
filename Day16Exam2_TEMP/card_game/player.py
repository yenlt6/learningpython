import card
class Player(card):
    '''
    Class đại diện cho mỗi người chơi
    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self,name,card):
        self.name=name
        self.card=card # mỗi người chơi được 3 quân bài, có nghĩa là nó phải chứa kiểu list Card?
        
    def __str__(self) -> str:
        return f'Player: {self.name}, {self.card}'
         
    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài của người chơi, 
           Y mỗi người chơi có 3 lá bài'''
        var_1=0        
        self.Car
    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài của người chơi, 
           Y mỗi người chơi có 3 lá bài'''
        var_1=0      
        switcher={
                'A': 1,
                1:1,
                2:2,
                3:3,
                4:4,
                5:5,
                6:6,
                7:7,
                8:8,
                9:9,
             }
        switcher.get(self.Card.rank)

    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        switcher={
                'G': 4,
                'H':3,
                'J':2,
                'k':1
        }
        pass

    def add_card(self):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        pass

    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''

    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
