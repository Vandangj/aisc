x1=[1,1,-1,-1]
x2=[1,-1,1,-1]

targets=[1,-1,-1,-1]
w1=0
w2=0
b=0
alpha=1 #learning rate

epoch=0

while True:

    print("epoch:",epoch)

    old_w1=w1
    old_w2=w2
    old_b=b

    for i in range(len(x1)):
        y_in=w1*x1[i]+w2*x2[i]+b
        if y_in>0:
            y=1
        elif y_in<0:
            y=-1
        else:
            y=0

        if targets[i]!=y:
            w1=w1+alpha*targets[i]*x1[i]
            w2=w2+alpha*targets[i]*x2[i]
            b=b+alpha*targets[i]

        dw1=w1-old_w1
        dw2=w2-old_w2
        db=b-old_b

        print("x1:",x1[i]," ","x2:",x2[i]," ","dw1:",dw1," ","dw2:",dw2," ","db:",db)
        
    print()
    epoch+=1
    if old_w1==w1 and old_w2==w2 and old_b==b:
        break

// code ends here 

epoch: 0
x1: 1   x2: 1   dw1: 1   dw2: 1   db: 1
x1: 1   x2: -1   dw1: 0   dw2: 2   db: 0
x1: -1   x2: 1   dw1: 1   dw2: 1   db: -1
x1: -1   x2: -1   dw1: 1   dw2: 1   db: -1

epoch: 1
x1: 1   x2: 1   dw1: 0   dw2: 0   db: 0
x1: 1   x2: -1   dw1: 0   dw2: 0   db: 0
x1: -1   x2: 1   dw1: 0   dw2: 0   db: 0
x1: -1   x2: -1   dw1: 0   dw2: 0   db: 0
