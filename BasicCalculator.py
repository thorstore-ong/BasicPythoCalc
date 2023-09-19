def addition(num1, num2) :
  sum = num1 + num2
  return sum

def subtraction(num1, num2) :
  sum = num1 - num2
  return sum

def multiplication(num1, num2) :
  sum = num1 * num2
  return sum


def division(num1, num2) :
  sum = num1 / num2
  return sum

quit = "N"
print("Welcome to the python calculator!")
while quit == "N" :
  var1 = input("Enter first val - ")
  try :
   val1 = int(var1)
  except :
    val1 = -1
  var2 = input ("Enter second val - ")
  try : 
   val2 = int(var2)
  except :
    val2 = -1

  opratr = input("+, -, *, / : ")
  if opratr == "+" :
    answer = addition(val1, val2)
    print(str(val1) + " + "+ str(val2) + " = " + str(answer))
  elif opratr == "-" :
    answer = subtraction(val1, val2)
    print(str(val1) + " - "+ str(val2) + " = " + str(answer))
  elif opratr == "*" :
    answer = multiplication(val1, val2)
    print(str(val1) + " * "+ str(val2) + " = " + str(answer))
  elif opratr == "/" :
    answer = division(val1, val2)
    print(str(val1) + "/"+ str(val2) + " = " + str(answer))
  else :
    print("That is not a valid operator")
    continue
  quit = input("Press Y to quit or N to continue: ")
  if quit == "Y" :
    print("Goodbye!")
    break





 