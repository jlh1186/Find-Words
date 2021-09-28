#Takes a Sample and Match it with a words in the Dicionary
import re


dic = open("dictionary.txt","r")

test = 'Y'
pattern = r'^p'
while(test != 'Q'):
    for real in dic:
            match = re.match(pattern,real)
            if match:
                print(real)
            continue
    test = 'Q'
dic.close()
