def perform_operation(num1,num2,operation):
    if operation=="add":
        return num1+num2
    elif operation=="substract":
        return num1-num2
    elif operation=="multiplication":
        return num1*num2
    elif operation=="division":
        if num2==0:
            return "error:division by zero is not allowed"
        else:
            return num1/num2