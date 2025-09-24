value=input("enter value(string or number:)")
match value:
    case int():
        print("you entered an integer:",value)
    case str():
        print("you entered a string:",value)
    case _:
        print("you entered invalid data type;")
