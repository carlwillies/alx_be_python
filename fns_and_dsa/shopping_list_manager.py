def display_menu():
    print("shopping_list manager")
    print("1.Add an item")
    print("2. remove an item")
    print("3.view list")
    print("4.exit")
display_menu()

def main():
    shopping_list=[]
    while True:
        display_menu()
        choice=input("enter your choice")
        if choice=="1":
            item=("enter the item to add")
            if item:
                print("{item} has been added to the list")
            else:
                print("list can't be empty")    
        elif choice=="2":
            item=input("enter the input to remove:")
            if item in shopping_list:
                shopping_list.remove(item)
            print("{item}has been successfully removed ")
        
        elif choice=="3":
            if shopping_list:
                print("shopping_list") 
        else:
            print("your shopping_list is empty")
        if choice=="4":
            print("goodbye")
        else:
            print("invalid choice")
    if __name__==_main_:
        main()                     
    

     





