num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
operation=input("chose the operation(+,-,*,/):")
match operation:
    case "+":
        result =num1+num2
        print(f"the sum is{result}")
    case "-":
        result=num2-num1
        print(f"the difference is {result}") 
    case "*":
        result=num1*num2
        print(f"the multiplication of num1 and num2 is {result}")
    case"/":
        result=num2/num1
        print(f"the result of division is {result}")
        if num1==0:
            print("invalid input")           