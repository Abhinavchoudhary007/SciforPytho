# -*- coding: utf-8 -*-
"""10Jan.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18pYPYISHpPTup0luDpqxR8YIErxqVPgW

Question 1 : Read file
"""

f = open("aboutPython.txt", "r")
print(f.read())

g= open("Ques2.txt", "r")
line_num = 1
for line in g:
    contain_num = False
    for char in line:
        if char.isdigit():
            contain_num = True
            break
    if contain_num:
        print("\nNumerical value in this line" , line_num ,":",line.strip())
    line_num += 1

import datetime
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi
height = float(input("Enter your height in meters: "))
weight = float(input("Enter your weight in kilograms: "))
bmi = calculate_bmi(weight, height)
date = datetime.datetime.now().strftime("%Y-%m-%d")
n = open("BMI.txt", 'a')
n.write("Date: " + date + "\n")
n.write("Height: " + str(height) + " m\n")
n.write("Weight: " + str(weight) + " kg\n")
n.write("BMI: " + str(bmi))

print("Your BMI is :", bmi)
print("BMI Data is recorded succeffully.")

h = open("Ques2.txt", "r")
lines= h.readlines()
j= open("new1.txt", 'w')
line_num=1
for line in lines:
  j.write(f"{line_num}.{line}")
  line_num +=1

print("Serial numbers added successfully to :", j)
j= open("new1.txt","r")
print(j.read())

m = open("program.txt","r")
lines = m.readlines()
m = open("program.txt", "w")
for line in lines:
  line= line.replace("langauge", "Language")
  m.write(line)

print("ALL lines are cooreceted in program.txt")
m = open("program.txt","r")
print(m.read())

k = open("Ayan.txt","r")
lines=k.readlines()

k = open("Ayan.txt","w")
for line in lines:
  if line.strip() and line[0].isdigit() and '.' in line:
    k.write("\n")
    k.write(line)
print("Done Successufully.")

k = open("Ayan.txt","r")
print(k.read())

k = open("Nidhi.txt","r")
lines=k.readline()
print(lines)
words= lines.split()
clean_words=[]
for i in range(len(words)):
  if i == 0 or words[i] != words[i-1]:
    clean_words.append(words[i])
modified_line = " ".join(clean_words)
print(modified_line)