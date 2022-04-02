def calc(num1,num2,op): 
  #function of calculator. takes 2 nums & operations to get result 

  if op == '*' :
    return (num1*num2);  #operation statement for multiplication 
    
  if op =='+' :
    return (num1+num2);   #operation statement for addition
    
  if op =='/' :
    return (num1/num2);   #operation statement for division
    
  if op =='-' :
    return (num1-num2);   #operation statement for subtraction 
  

def do_calc():
    num1 = int(input("enter one number: ")) #input values 
    num2 = int(input("enter second number: "))

    op = input("enter an operation: * - / + ") #operation fnc
    print("answer is  ",calc(num1,num2,op))
