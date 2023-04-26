height=float(input("enter your height"))
weight=float(input("enter your weight"))
age=int(input("enter your age"))
BMI=weight/(height*height)
if BMI <18.5:
    print("kambode vazn")
elif BMI>=18.5 or BMI<24.5:
    print("vazn monaseb")
elif BMI>=25 or BMI<29.9:
    print("ezafe vazn")
else:
    print("chagiii")