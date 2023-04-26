import random
list1=['stone','paper','sissor']
char=random.choice(list1)
user=input("enter the stone or paper or sisor:")
count_user=0
count_char=0
if char==list1[0] and user=="paper":
    count_user=count_user+1
elif char==list1[1] and user=="sissor":
    count_user=count_user+1
elif char==list1[1] and user=="stone":
    count_char=count_char+1
elif char==list1[2] and user=="paper":
    count_char=count_char+1
elif char==list1[2] and user=="stone":
    count_user=count_user+1
if char==list1[0] and user=="sissor":
    count_char=count_char+1
else:
    if char>user:
        print ("winer is char and point is:",count_char,char)
    elif user>char:
        print("winer is user and point is:",count_user)
    else:
        print("khonsa")