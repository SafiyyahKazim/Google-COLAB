def calculator():
    #for function
  num1 = int(input("Enter the first number: "))
#to 
  num2 = int(input("Enter the second number: "))
  operator = input("Add, subtract, multiply, or divide: ")
  if operator == "Add": 
    return num1 + num2
  elif operator == 'Subtract':
    return num1 - num2
  elif operator =='Multiply':
    return num1 * num2
  elif operator == "Divide":
    return num1 / num2
calculator()