task=input("describe your task")
priority=("high,medium,low")
time_bound=("is the task time_bound?(yes/no)")
match priority:
    case "high":
        if time_bound==yes:
            print(f"remider:{task} is high priority task and recquires immediate action today")
        else:
            print(f"remider:{task} is high priority task and recquires implementation soon")
    case "medium" :
        if time_bound=="yes":
            print(f"{task} is medium priority and requires attention in few days to come")
        else:
            print(f"{task} is medium but can be addressed later") 
    case "low":
        if time_bound==yes:
            print(f"{task} is low priority task to be addressed")
        else:
            print(f"Note:{task} is low priority task , consider completing it when you have free time ") 
    case _:
        print(f"invalid priority level.")
                    


          