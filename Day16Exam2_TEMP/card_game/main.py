import card as c
import game as g
import deck as d
import player as p

def main():
    list_player=[]  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    print("Wellcome!!!\n   chào mừng đến với game đánh bài 3 cây ( vui thôi nha)")
    print("   Có bao nhiêu người muốn chơi:")
    number_player=int(input("Nhập số người chơi:"))    
    try:
        name_1=input("Tên người chơi 1: ")
        name_2=input("Tên người chơi 2: ")
    except ValueError as e:
        print(e)
    c.card_function()
    

if __name__ == '__main__':
    main()
