import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
symbols="!@#$%^&*()."
string=lower+upper+number+symbols
length=int(input("enter the length: "))
password="".join(random.sample(string,length))
print("your password is: ",password)
