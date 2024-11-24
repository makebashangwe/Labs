''' Class: CSE 1321L
Section: J51
Term: FALL 2024
Instructor:
Name: Makeba Waddy
Lab6B, My Math
'''


def my_max(num1,num2):
    if num1 > num2:
        return num1
    if num2 > num1:
        return num2
def my_min(num1,num2):
    if num1 < num2:
        return num1
    if num2 < num1:
        return num2

def my_avg(num1,num2):
    sum = num1+num2
    avg = sum / 2
    return avg