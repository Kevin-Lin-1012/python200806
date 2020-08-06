import os.path
if os.path.isfile('you.txt'):
    print('file存在')
else:
    print('file不存在')
x=open('you.txt','w')
x.write('you')
x.close()

y=open('you.txt','r')
text=y.read()
print(text)
y.close()

z=open('you.txt','a')
z.write(' sucks')
z.close()

a=open('you.txt','r')
b=a.read()
print(b)
a.close()