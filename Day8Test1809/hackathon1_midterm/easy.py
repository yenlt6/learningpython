# 1
from datetime import datetime
import re
def day_diff(release_date, code_complete_day):
    release_date = datetime.strptime(release_date, "%d/%m/%Y")
    code_complete_day = datetime.strptime(code_complete_day, "%Y-%d-%m")
    return abs((release_date - code_complete_day).days)


# 2
def alpha_num(sentence):
    return re.findall(r'(?:\d+[a-zA-Z]+|[a-zA-Z]+\d+)', sentence)
    