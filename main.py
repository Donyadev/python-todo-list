
#======To-Do List=======

def int_check(message, error_message,num1,num2):
    while True:
        try:
            opt = int(input(message))
            if num2 <= opt <= num1:
                return opt
            else:
                print(error_message)
        except ValueError:
            print("Please enter a valid integer!")
def str_check(message,error_message):
    while True:
        task=input(message)
        if not task.strip():
            print(error_message)
        else:
            return task
def task_exists(task,task_list):
    count = 0
    new_name = task
    while new_name in task_list:
        count += 1
        new_name = f"{task}{count}"
    return new_name
def show_tasks(task_list):
    if not task_list:
        print("No tasks found!")
        return False
    print("======Tasks=====")
    print("[ ] Pending")
    print("[✓] Completed")
    num = 0
    for task in task_list:
        num += 1
        if not task_list[task]:
            print(f"Task {num}: {task} [pending]")
        else:
            print(f"Task {num}: {task} [✓]")
    return True
def yes_no(message,error_message):

    while True:
        answer=input(message).lower()
        if answer == "y" or answer == "n":
            return answer
        else:
            print(error_message)
def num_to_dic(number,task_list):
    if number > 0:
        number -= 1
    selected_task = list(task_list.keys())[number]
    return selected_task
def save_task(task_list):
    with open("To_Do List.txt", "w", encoding="utf-8") as f:
        f.write("======Tasks=====\n")
        f.write("[ ] Pending\n")
        f.write("[✓] Completed\n")
        num = 0

        for task in task_list:
            num += 1
            if not task_list[task]:
                f.write(f"Task {num}: {task} [pending]\n")
            else:
                f.write(f"Task {num}: {task} [✓]\n")
    print("Tasks saved successfully!")

#Menu
print("========= MAIN MENU ==========*")
print("1. Add Task")
print("2. View Tasks")
print("3. Complete Task")
print("4. Delete Task")
print("5. Save Tasks")
print("6. Exit")
print("==============================*")

task_list = {}

while True:
    option = int_check("What would you like to do?", "please choose an option between 1 and 6",6,1)

    #Exit
    if option ==6:
        if not task_list:
            print('Thank you for using this program!')
            break
        exit_opt = yes_no("Do you want to save before exiting? (y/n)", "invalid Input!only y/n")
        if exit_opt == "y":

           save_task(task_list)

           print('Thank you for using this program!')
           break
        else:
           print('Thank you for using this program!')
           break

    #Add
    elif option ==1:
        task_name= str_check("Enter Task:", "Name cant be empty!")
        new_name= task_exists(task_name,task_list)
        task_list[new_name]= False
        print("Task added successfully!")
        print(task_list)
        print(f"Total Tasks: {len(task_list)}")

    #View
    elif option ==2:
        show_tasks(task_list)

    #Complete
    elif option ==3:
        if not show_tasks(task_list):
            continue
        compete_opt= int_check("Enter Task Number to Complete:","invalid Number!",len(task_list),1)
        selected_task= num_to_dic(compete_opt,task_list)
        task_list[selected_task]= True
        print(f"Task Number {compete_opt}: Completed")

    #Delete
    elif option ==4:
        if not show_tasks(task_list):
            continue
        delete_opt= int_check("Enter Task Number to Delete:","invalid Number!",len(task_list),1)
        selected_delete= num_to_dic(delete_opt,task_list)
        task_list.pop(selected_delete)
        print(f"Task Number {delete_opt}: Deleted")
        print(task_list)

    #Save
    elif option ==5:
        if not task_list:
            print("No tasks found!")
        else:
            save_task(task_list)









