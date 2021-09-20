import sys
import re
import io

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
    # print(rank_1)
    return rank_1
#Run: python babynames.py baby1998.html


def main():
      # Chương trình này có thể nhận đối số đầu vào là một hoặc nhiều tên file
  args = sys.argv[1:]

  if not args:
    print('usage: [--summaryfile] file [file ...]')
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]

  # +++your code here+++
  # Với mỗi tên file, gọi hàm extract_names ở trên và in kết quả ra stdout
  # hoặc viết kết quả ra file summary (nếu có input --summaryfile).
  list_name = []
  for filename in args:
    list_name += extract_names(filename)
  if(summary):
    with open('summary.txt', 'w') as file:
      file.write("\n".join(list_name))
      print("Vui lòng mở file summary.txt để xem kết quả")
  else:
      print(list_name)   
  
if __name__ == '__main__':
  main()
