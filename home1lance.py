import re
li = []
st = ""
with open("/home/lance/pylan/2.txt","r") as f:
  a = f.readlines()
  for i in a:
    li.append(i.strip())
    b = set(li)
et = ".".join(b)
st += et
bst =  re.split('=|\.',st)

key = bst[0::2]
value = bst[1::2]

duplicated = set()
for i in range(0,len(key)):
 for k in range(0,len(key)):
    if i != k:
       if key[i] in key[k]:
        duplicated.add(key[k])
        print value[i]
