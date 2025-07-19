task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case x if x == "high":
        if time_bound == "yes":
            print(f"Remainder: '{task}' is a high priority task that requires immediate attention today!")
        else:
            print(f"Remainder: '{task}' is a high priority task but does not require immediate attention")
    case x if x == "low":
        if time_bound == 'no':
            print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
        else:
            print(f"Note: '{task}' is a low priority task. But it time bound!.")
    case _ :
        print("Invalid response!")
        