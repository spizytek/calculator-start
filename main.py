
def add(n1 , n2):
    return n1+n2
  
def div(n1 , n2):
    return n1/n2
  
def mul(n1 , n2):
    return n1*n2
  
def sub(n1 , n2):
    return n1-n2

  
def calculator():
  cont_calc = True
  num1 = 0
  operations = {"+": add, "/": div, "*": mul , "-":sub}
  num1 = int(input("What's the first number? "))
  num2 = int(input("What's the second number? "))
  
  def dict_calc(numb2, symb):
    calc = operations[symb]
    res = calc(num1, numb2)
    print(f"{num1}{symb}{num2} = {res}")
    return res
  
  for sym in operations:
    print(sym)
  selectd_sym = input("Enter operation symbol of choice.. ")
  num1 = dict_calc(num2, selectd_sym)
  
  while (cont_calc != False):
  # sym = (input("Pick another operation: "))
  # an_num = int(input("What's the next number? "))
  # num1 =dict_calc(an_num, sym)
    fdck = (input("Type \"y\" to continue the calculator or \"n\" to exist:  "))
    if (fdck == "y"):
        #recursion
        calculator()
    else:
        cont_calc = False
      
calculator()