#Takes a Sample and Match it with a words in the Dicionary
import re


dic = open("dictionary.txt","r")
dic.close()

pattern = r'^en...y$'
def test():
    ques = 'Y'
    while(ques != 'Q'):
         for real in dic:
              match = re.match(pattern,real)
              if match:
                   print(real)
              continue
         ques = 'Q'
    return 1
test()

