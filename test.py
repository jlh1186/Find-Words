#Takes a Sample and Match it with a words in the Dicionary
import re


dic = open("dictionary.txt","r")

ques = 'Y'

pattern = r'^en...s$'
def test():
    while(ques != 'Q'):
         for real in dic:
              match = re.match(pattern,real)
              if match:
                   print(real)
              continue
         ques = 'Q'
    return 0
test()
dic.close()
