#!/usr/bin/env python3

def admin_login(username, password):
    if ((username =='admin' or username=='ADMIN') and password=='12345'):
        return "Access granted"
    return "Access denied"

def hows_the_weather(temperature):
    temp = "It's too dang hot out there!"
    if temperature<40:
        temp = "It's brisk out there!"
    elif temperature>=40 and temperature <65:
        temp = "It's a little chilly out there!"
    elif temperature >=65 and temperature < 85 :
        temp = "It's perfect out there!"
    return temp

def fizzbuzz(num):
    _three = num % 3
    _five = num % 5

    if _three == 0 and _five != 0:
        return 'Fizz'
    elif _three != 0 and _five == 0:
        return 'Buzz'
    elif _three == 0 and _five == 0:
        return 'FizzBuzz'
    else:
        return num


def calculator(operation, num1, num2):
    if operation == '+':
        return (num1 + num2)
    elif operation == '-':
        return (num1 - num2)
    elif operation == '*':
        return (num1 * num2)
    elif  operation == '/':
        return (num1 / num2)
    else:
        print("Invalid operation!")
        return None 
    

