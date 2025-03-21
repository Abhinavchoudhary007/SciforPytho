# -*- coding: utf-8 -*-
"""27classQuestions.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rXHXw52cBRp1Hck7mxbsA5yGp3gEeHNp
"""

student = []
print("\n 1. Add Student ")
print("\n 2. Display Students ")
print("\n 3. Exit")

choice=int(input("Enter your choice: "))
if choice == 1:
    name= input("Enter student name: ")
    roll = int(input("Enter student roll number: "))
    marks = int(input("Enter student marks: "))
    student.append({"name": name, "roll": roll, "marks": marks})
    print(student)
    print("Student added successfully.")

elif choice == 2:
  if not student:
    print("No students found.")
  else :
    print("Student List:")
    for student in student:
      print(f"Name: {student['name']}, Roll: {student['roll']}, Marks: {student['marks']}")

elif choice == 3:
  print("Exiting the program.")

print("Prime number between 1 to 100 :")
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i, end = " ")

n = int(input("Enter the number of term in fabonnaci series :"))
a,b=0,1
print(" Fabonnaci series: ", end = " ")
for _ in range(n):
  print(a , end= " ")
  a, b = b , a+b

n = int(input(" Enter the number to find Factorial :"))
factorial = 1
if n < 0 :
  print("Factorial doesnt exist for negative ")
elif n == 0:
  print("Factorial of 0 is 1")
else :
  for i in range (1 , n + 1):
    factorial = factorial * i
  print("Factorial of ", n , "is ", factorial)

print("Even number from 1 to 100 :")
for i in range(1,101):
    if i%2==0:
        print(i, end = " ")
print("\nOdd number from 1 to 100 :")
for i in range(1,101):
    if i%2 !=0:
        print(i, end = " ")

Ques = [
    {"Ques": "What is captial of India?", "Options": ["1. Goa", "2. Mumbai", "3. Delhi", "4. Kolkata"], "answer": 3},
    {"Ques": "What is 5+5?", "Options": ["1. 5", "2. 6", "3. 8", "4. 10"], "answer": 4},
]

correct_ans = 0
wrong_ans = 0

for i, q in enumerate(Ques):
    print("Q", i + 1, ":", q['Ques'])
    for option in q['Options']:
        print(option)
    try:
        answer = int(input("Enter your answer: "))
        if answer == q["answer"]:
            print("Correct Answer")
            correct_ans += 1
        else:
            print("Wrong Answer")
            wrong_ans += 1
    except ValueError:
        print("Invalid input. Please enter a valid option.")

print("Quiz Completed!")
print("Correct Answers:", correct_ans)
print("Wrong Answers:", wrong_ans)