import math
def Cut_or_Bulk():
    if(bmi < 18.5):
        bulk_plan  = maintenance + 400
        return "you need to bulk and so your calories are set to :",bulk_plan
    if( bmi >= 18.5 and bmi < 24.9):
        return "you are in the healthy range for your age and weight you can continue at maintenance : " , maintenance
    if( bmi > 24.9):
        cut_plan = maintenance - 400
        return " you need to cut as you are in the unhealthy range according to your bmi " , cut_plan
        



age = int(input("enter your age : ")) # the users age
weight = float(input("enter your weight in kgs: ")) # current weight
height = float(input("enter your height in centimeters: ")) # the height in centimeters
bmi = (weight/height/height)*10000  #BMI formula
print(bmi) 

question = input("do you want to continue and find out your Body fat percentage (yes/no): ")
if (question == "no"):
    print("okay have a good day")
else:
    waist = float(input("enter your waist: (in centimeters)")) # the users waist measurements (used to find body fat percentage)
    neck = float(input("enter your necks circumference: (in centimeters)"))
    BF = 495/(1.0324 - 0.19077*math.log(waist-neck,10)+0.15456*math.log(height,10)) - 450 #Body Fat formula
    print("%",BF)
    question2 = input("do you want to find out your lean mass? (yes/no)")
    if(question2 == "no"):
        print("okay have a great day")
    if(question2 == "yes"):
        FM = weight * (BF/100) # fat mass
        LM = weight - FM # lean mass
        print(" you have ",LM," kgs of lean mass")
diet_plan = input("do you want a diet plan specified to your needs (yes/no)")
if(diet_plan == "no"):
    print("okay moving on")
else:
    exercise = input("how much do you exercise per week?(alot / moderate / little / none)")
    BMR = 10 * weight + 6.25 * height - 5 * age  +5  # calculation for the basal metabolic rate
    if (exercise == "none"):
        maintenance = BMR * 1.2
    elif ( exercise == "little"):
        maintenance = BMR * 1.4
    elif (exercise == "moderate"):
        maintenance = BMR * 1.6
    elif (exercise == "alot"): 
        maintenance = BMR * 1.8
    print(Cut_or_Bulk())
goal_weight = int(input("enter your goal weight"))

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([LM,FM])
ypoints = np.array([goal_weight,weight])

plt.plot(xpoints, ypoints)
plt.show()