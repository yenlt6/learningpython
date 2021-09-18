import sys
import re

def extract_names(filename):
    f =  open(filename, encoding='utf-8-sig')
    content = f.read()
    year=re.findall("Popularity in \d+",content)
    year=year[0]
    year=year[14:]    
    name=re.findall('tr align="right"><td>(\d+)<\/td><td>(\w+)<\/td><td>(\w+)<',content)
    rank_1=[]
    rank_2=[]   
    for i in name:
        rank_1.append(f"{i[1]} {i[0]}")
        rank_2.append(f"{i[2]} {i[0]}")  
    rank_1.extend(rank_2)    
    rank_1.sort()   
    rank_1.insert(0,year)
    print(rank_1)
#Run: python babynames.py baby1998.html
def main():
    if len(sys.argv) != 2:
        print('usage: ./babynames.py file')
        sys.exit(1)

    filename = sys.argv[1]
    extract_names(filename)
    sys.exit(1)

if __name__ == '__main__':
  main()

