from Day16Exam2Date1510.card_game.card import Card


class Deck(Card):
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''

    def build(self):
        '''Tạo bộ bài: tạo 1 list, mỗi phần tử của list là 1 lá bài gồm 9*4=36 lá bài'''
        pass

    def shuffle_card(self):
        '''Trộn bài, random(list)'''
        pass

    def deal_card(self):
        '''Rút một lá bài từ bộ bài: lấy random 1 lá bài từ bộ bài, tức là lấy random 1 phần tử trong list ra'''
