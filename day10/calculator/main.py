from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply, 
  "/": divide
}

def calculator():
  print(logo)
  
  first_number = float(input("What is the first number?: "))

  for symbol in operations:
    print(symbol)

  cont = False

  while not cont:

    operator = input("Pick an operation: ")

    second_number = float(input("What is the next number?: "))
  
    operation_function = operations[operator]
    answer = operation_function(first_number, second_number)

    print(f"{first_number} {operator} {second_number} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit: ") == "y":
      first_number = answer
    else:
      cont = True
      calculator()

calculator()
