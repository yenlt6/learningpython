'''Kết nối CSDL'''
# Kết nối đến MySQL
# from pymysql import connect, cursors
# config = {
#     'host': 'remotemysql.com',
#     'user': 'UyMDXcxEoz',
#     'password': 'lFJmWnNbEC',
#     'database': 'UyMDXcxEoz'
# }
# conn = connect(**config)
# conn.close()
# import the time module
import time
from datetime import date

from datetime import datetime

from pymysql import connect, cursors

config = {
    "host": "10.124.60.67",
    "user": "omd_qc",
    "password": "omd_qc",
    "database": "game_log",
}

conn = connect(**config)
conn.close()

today  = datetime.now()


def log():
    '''
    Ghi thông tin về game vào CSDL và 2 bảng games và logs

    Bảng games gồm tên người chiến thắng

    Bảng logs gồm danh sách người chơi, bộ bài, điểm và lá bài lớn nhất tương ứng với game

    Chú ý, sau khi INSERT vào games, có thể lấy id của game vừa tạo với cursor.lastrowid
    '''
    pass


def get_last_game():
    '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
    pass


def history():
    '''
    Lấy thông tin về lịch sử chơi

    Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi (sử dụng GROUP BY và các hàm tổng hợp)
    '''
