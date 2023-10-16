#You can contact me to get the tool without encryption
#Thanks for using my project
#alzaeem
#History: 1/7/2020
import marshal
exec(marshal.loads(''))

import random
a="qwertyuioplkjhgfdsazxcvbnm"
b="QWERTYUIOPLKJHGFDSAZXCVBNM"
n="1234567890"

w=10
g=a+b+n
x=0
while True:
       pas="".join(random.sample(g,w))
       print("" ,pas)
       x+=1

       if x==10000:

              break

print