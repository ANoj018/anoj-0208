# #list slicing

# L1 =[ 1,8,7, 2,21,15]

# L1.sort()
# print(L1)

# L1.reverse()
# print(L1)

# L1.append(8)
# print(L1)

# L1.insert(2, 10)
# print(L1)

# L1.remove(10)
# print(L1)

# L1.pop(3)
# print(L1)

# write a program to store seven fruits in a list entered by the user
fruits = []
for i in range(7):
    fruit = input("Enter a fruit: ")
    fruits.append(fruit)
print("Fruits list:", fruits)

# wap to accept marks of 6 student and display in list
marks = []
for i in range(6):
    m = int(input(f"Enter marks of student {i+1}: "))
    marks.append(m)
print("Marks of students:", marks)


# write a program to sum a list with 4 numbers
numbers = [10, 20, 30, 40]
total = sum(numbers)
print("The sum is:", total)
