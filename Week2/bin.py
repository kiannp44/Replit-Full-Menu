def bin(n): 
#binary function. convert any positive value to binary 

  b = []             #empty list for binary result
  
  if n == 0: 
    return [0]
    
  while n > 0:
    q = n // 2       # integer quotient division by 2
    r = n % 2        #remainder 
    b.insert(0, r)
    n = q

  return b

def do_binary(): 
    num = int(input("enter one number: ")) #input values 

    print("conversion is  ",bin(num))