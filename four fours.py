import math
import random
print("Did You Know That You Can Make Any Number From Four 4's")
number=random.randint(1,100)
user_input = input("Try Making {} Using Four 4's: ".format(number))

user_input=user_input.replace("fact","math.factorial")
user_input=user_input.replace("sq","math.sqrt")
user_input=user_input.replace("^","**")

count=0
for i in user_input:
    if i=="4":
        count+=1
      
if count>4:
    print("Too Many Fours Dumbo")
elif(count<4):
    print("Not Enough Fours Youre Bad")
else:
    answer = eval(user_input)
    print(answer)
    if answer == number:
        print("Correct")
