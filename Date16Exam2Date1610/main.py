import deck as dec
import player as pla
import card as ca
import subprocess as sp



import game as ga
def main():  # khó
    game = ga.Game()
    game.setup()
    memu=[]
    memu.append('1.Xem danh sách người chơi')
    memu.append ('2.Thêm mới người chơi ')
    memu.append ('4.Chia bài ')
    memu.append('5.Lật bài: ')
    memu.append('6.Xem lịch sử chơi')
    memu.append("7.Tổng số lượt chơi trong ngày")
    memu.append('8. Thoát game')
    while True:
        for i in memu:
            print(i)
        luachon=int(input("lựa chọn của bạn:"))
        if luachon== 1:
                    game.list_players()
        elif luachon==2:
                    game.add_player()
        elif luachon==3:
                    id=int(input("Nhập id người dùng muốn xóa:"))
                    game.remove_player(id)
        elif luachon==4:
                   game.deal_card()
        elif luachon==5:
                    game.flip_card()
        elif luachon==8:
                    break
        else:
                 print("Unknown Option Selected!")



main()

