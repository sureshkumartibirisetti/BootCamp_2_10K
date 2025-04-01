import math
import random
a=0
b=0
a_s=0
b_s=0
ladder={1:38,4:14,8:30,21:42,28:76,50:67,71:92,86:99}
snakes={32:10,36:6,48:26,63:18,88:24,95:56,97:78} 
while(a<100 and b<100):
    a_temp=a
    temp=a
    x=random.randint(1,6)
    if(x==1 or x==6):
        a_s=1
    if(a_s==1):
        a+=x
        if(a in ladder):
            a=ladder[a]
        if(a in snakes):
            a=snakes[a]
        if(a<100):
            if(x==6):
                x=random.randint(1,6)
                a+=x
                if(a in ladder):
                    a=ladder[a]
                if(a in snakes):
                    a=snakes[a]        
                if(x==6):
                    x=random.randint(1,6)
                    a=temp
        elif(a==100):
            print("🎉 Player 1 wins the game! 🎉")
            break
        else:
            a=a_temp
    
    b_temp=b
    temp1=b
    y=random.randint(1,6)
    if(b_s==1):
        b+=y
        if(b<100):
            if(b in ladder):
                b=ladder[b]
            if(b in snakes):
                b=snakes[b]
            if(y==6):
                y=random.randint(1,6)
                b+=y
                if(b in ladder):
                    b=ladder[b]
                if(b in snakes):
                    b=snakes[b]
                if(y==6):
                    y=random.randint(1,6)
                    b=temp1
        elif(b==100):
            print("🎉 Player 2 wins the game! 🎉")
            break
        else:
            b=b_temp




