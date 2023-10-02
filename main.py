print("calcualte the higheat score")
score = input("enter the score ").split()
for n in range(0,len(score)):
    score[n] = int(score[n])

max_score = 0
for x in score:
    if x > max_score:
        max_score = x 

print(f"the maximum score is {max_score}")
