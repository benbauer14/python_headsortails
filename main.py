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

scores = [90, 34, 61, 61, 92, 61, 71]
highscore = scores[0]
for score in scores:
    if(score > highscore):
        highscore = score

print(highscore)