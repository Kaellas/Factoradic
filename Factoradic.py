def decimal_to_factoradic(decimal):
  
  if decimal == 0:
    return "0"
  
  rem = ""
  n = len(str(abs(decimal)))
  i = 2
  
  while decimal > 0:
    rem = str(decimal % i) + rem
    decimal = decimal // i
    i += 1
    
  return rem


def factoradic_to_decimal(factoradic):
  
  import math
  
  if factoradic == "":
    return 0
  
  res = 0
  n = len(factoradic)
  
  for i in range(1, n + 1):
    res += int(factoradic[i-1])*math.factorial(n-i+1)
    
  return res

# Example usage
dtf = decimal_to_factoradic(100001)
print(dtf)

print(factoradic_to_decimal(dtf))
