print("this code is to calculate the average height of students \n")
height = input("enter the height").split()
for n in range(0,len(height)):
    height[n] = int(height[n])
tot_height = 0
for x in height:
    tot_height += x
print(f"the totoal height = {tot_height}")
num_of_students = 0
for y in height:
    num_of_students += 1 
print(f"the num of students = {num_of_students}")
avg_height = round(tot_height/num_of_students)
print(f"the average height is : {avg_height}")
