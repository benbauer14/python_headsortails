import random

zeroOrOne = random.randint(0,1)

if(zeroOrOne == 0):
    print("heads")
else:
    print("tails")

student_height = [123, 123, 151, 124]
sum = 0

for height in student_height:
    sum = sum + height

print(sum/len(student_height))