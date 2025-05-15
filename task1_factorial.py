#calculate factorial 
def factorial(num,fact):
    if num==0 or num ==1:
        return fact
    fact *= num
    return factorial(num-1,fact)
    
num = int(input("Enter the number: "))
result = factorial(num,1)
print("Factorial of",num,"is:",result)
