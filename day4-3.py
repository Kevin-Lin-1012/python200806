import os.path
dic={}
def buildmenu():
    print('歡迎進入成績查詢系統')
    print()
    print('1.輸入成績\n2.列出成績\n3.查詢成績\n4.離開')

if os.path.isfile('score.txt'):
    print('file存在')
    z=open('score.txt','r')
    for row in z.readlines():
        data=row.split(':')
else:
    print('file不存在')
    x=open('score.txt','w')
while True:
    buildmenu()
    sel=int(input('輸入選項'))
    if sel==1:
        while True:
            f=input('輸入名字\(按0可退出)')
            if f=='0':
                print(dic)
                print()
                break
            e=input('輸入分數')
            dic[f]=e
            print()
    elif sel==2:
        print(dic)
        print()
    elif sel==3:
        while True:
            c=input('輸入欲查之人名\(按0可跳出)')
            if c=='0':
                break
            if c in dic:
                print(dic[c])
            else:
                print('無此人')
                print()
    elif sel==4:
        break
    else:
        print('輸入錯誤')
    x=open('score.txt','w')
    for k,v in dic.items(): 
        x.write(k)
        x.write(':')
        x.write(v)
        x.write('\n')
    x.close()       

            



    
    
