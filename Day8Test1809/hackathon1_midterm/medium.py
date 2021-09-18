def anagram_number(number):
    a=str(number)[::-1]
    if a==str(number):
        return True
    else :
         return False

def roman_to_int(s):
      rom_dict = {'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900,'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
      i = 0
      int1 = 0
      while i < len(s):         
         if i+1<len(s) and s[i:i+2] in rom_dict:
            int1+=rom_dict[s[i:i+2]]
            i+=2
         else:
            #print(i)
            int1+=rom_dict[s[i]]
            i+=1
      return int1