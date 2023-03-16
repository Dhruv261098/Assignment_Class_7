# Dhruv Desai
# C0883865


# Q1

name = input("Enter your name")

def function():
    print(len(name))

function()


# Q2

def count_characters(str):
  char_frequency = {}
  for char in str:
    if char in char_frequency:
      char_frequency[char] += 1
    else:
      char_frequency[char] = 1
  return char_frequency

print(count_characters('google.com'))


# Q3

str = "Dhruv Desai C0883865"
print(str.capitalize())
print(str.casefold())
print(str.isalnum())
print(str.isdigit())
print(str.encode())
print(str.islower())
print(str.expandtabs())
print(str.istitle())


# Q4

def f_to_c(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    print(celsius)

f_to_c(98)


