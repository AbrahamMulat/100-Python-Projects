# --- coding: utf-8 ---
# @FileName  :BMI_calculator.py
# @Time      :11/11/2022 8:22 PM
# @Author    :Abraham
# @Software  :PyCharm

# Body mass index (BMI) is a person’s weight in kilograms divided by the square of height in meters.
# BMI is an inexpensive and easy screening method for weight category—underweight, healthy weight, overweight, and obesity.


def calculate_BMI(weight, height):
    bmi = round(weight / (height ** 2), 2)
    if bmi < 18.5:
        print(f"Your BMI is {bmi}, you are Underweight!!")
    elif 18.5 <= bmi < 25:
        print(f"Your BMI is {bmi}, you are healthy Weight!!")
    elif 25 <= bmi < 30:
        print(f"Your BMI is{bmi}, you are Overweight!!")
    else:
        print(f"your BMI is {bmi}, you are obese!!")
    return


weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in meter: "))

calculate_BMI(weight, height)
