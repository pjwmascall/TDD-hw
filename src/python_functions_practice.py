def return_10():
    return 10

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def length_of_string(string):
    return len(string)

def join_string(string1, string2):
    return string1 + string2

def add_string_as_number(numstr1, numstr2):
    return int(numstr1) + int(numstr2)

def number_to_month_name_helper(month_number, month_name_type):
    from datetime import datetime
    return datetime.strptime(str(month_number), "%m").strftime(month_name_type)

def number_to_full_month_name(month_number):
    return number_to_month_name_helper(month_number, "%B")

def number_to_short_month_name(month_number):
    return number_to_month_name_helper(month_number, "%b")

def volume_of_cube(side_length):
    return side_length ** 3

def reverse_string(string):
    return string[::-1]

def fahrenheit_to_celcius(temperature_in_fahrenheit, precision=0):
    return round((temperature_in_fahrenheit - 32) * (5/9), precision)