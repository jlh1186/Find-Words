#Takes a Sample and Match it with a words in the Dicionary
import re


dic = open("dictionary.txt","r")

test = 'Y'
pattern = r'^en..$y'
def tet(s):
    while(s != 'Q'):
         for real in dic:
              match = re.match(pattern,real)
              if match:
                   print(real)
              continue
         s = 'Q'
   return 1
tet(test)
dic.close()
