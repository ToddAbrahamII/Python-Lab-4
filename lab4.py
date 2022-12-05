#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 14:01:44 2022

@author: toddabrahamii
"""
import random
import math
import statistics

#Problem 1
number_set = []
variance_set = []

counter = 0
check = 0
total_number = 0
variance_number = 0
vn = 0
mean = 0
standard_deviation = 0

#Fill list with 50 random integers and total them
for i in range(50):
    random_number = random.randint(1,500)
    number_set.append(random_number)
    total_number += random_number

#Calculates the Mean
mean =total_number/len(number_set)

#Calculate Variance
for x in range(len(number_set)):
    if x <= 50:
        variance_number=(number_set[x] - mean)**2
        variance_set.append(variance_number)
        
vn = sum(variance_set)/49

#Calculate Standard Deviation
standard_deviation = vn**0.5


#Prints results
print("Problem #1:")
print(number_set)
print()
print("Mean: ", mean)
print("Standard Deviation: ", round(standard_deviation,2))
print()
print("Accuracy Check!")
print("Mean: ", statistics.mean(number_set))
print("Standard Deviation: ", round(statistics.stdev(number_set),2))


#Problem #2
print("------------------")
print("Problem #2: ")

exponential = 10
steps = 10
z = math.e**10
result = 1



#Calculation 1
for i in range(1,steps+1):
   result += (exponential**i)/(math.factorial(i))
   

#Print steps of expansion 1
print("The exponential is: ", exponential)
print("There are ", steps, " steps of expansion")
print("The ground truth for e**10 is", math.e**10)
print("Our result is: ", result)
print()

#Calculation 2
result = 1
steps = 20
for i in range(1,steps+1):
   result += (exponential**i)/(math.factorial(i))


#print steps of expansion 2
print("The exponential is: ", exponential)
print("There are ", steps, " steps of expansion")
print("The ground truth for e**10 is", math.e**10)
print("Our result is: ", result)
print ()

#Calculation 3
result = 1
steps = 100
for i in range(1,steps):
   result += (exponential**i)/(math.factorial(i))
   
#print steps of expansion 2
print("The exponential is: ", exponential)
print("There are ", steps, " steps of expansion")
print("The ground truth for e**10 is", math.e**10)
print("Our result is: ", result)
print()

#Problem #3
print("------------------")
print("Problem #3: ")

#Problem 3 variables
x_list = []
x = 0
solution = 0
check = 0

#x1 + 13 * x2 - x3 + x4 + 12 * x5 - x6 -11 + x7 * x8 + x9 -10 = 66

#Loop to perform formula
while check == 0:
    for i in range (1,11):
        x = random.randint(1,9)
        x_list.append(x)
    solution = x_list[1] + 13 * x_list[2] - x_list[3] + x_list[4] + 12 * x_list[5] - x_list[6] - 11 + x_list[7] * x_list[8] + x_list[9] - 10
    if solution == 66:
        check = 1 
        print("One of the solutions is: ", x_list)
        break
        
    x_list = []
 

