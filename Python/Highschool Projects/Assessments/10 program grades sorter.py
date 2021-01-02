# getting the grades in a list
grades = ["69"]
# the grades sorter is a list
x9 = []
# starting the for loop

for x in grades:
    # appending x to the sorter list
    x9.append(x)
    # getting the next grade
    x = int(x) - 1
    # appending the new grade to the grades list
    grades.append(x)
    # when the grades reach 0, the dor loop stop
    if int(x) == 0:
        break
# printing the sorter list
print("the grades for 9x are:" + str(x9))
