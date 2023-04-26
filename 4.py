import random as rn
value=rn.randint(0,6)
print(value)
value2=rn.randint(0,6)
print(value2)
x=input("do you want to play?")
for i in x:
    if(i=='yes'):
        continue
    else:
        break
print("End")