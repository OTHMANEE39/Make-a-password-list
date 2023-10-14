import random
a="qwertyuioplkjhgfdsazxcvbnm"
b="QWERTYUIOPLKJHGFDSAZXCVBNM"
n="1234567890"
s="+×÷=/_€£₹₩)(*&^%$#@!-':;,?.,`~\|<>{}[]¿¡"
w=10
g=a+b+n+s
x=0
while True:
       pas="".join(random.sample(g,w))
       print("" ,pas)
       x+=1

       if x==9999999999999999999999999999999999:
              break

print