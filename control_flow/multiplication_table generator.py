num1=int(input("enter the number to see its multiplication table:"))
print(f"multiplication table for {num1}")
for i in range(1,11):
    product=i*num1
    print(f"{num1}*{i}={product}")
