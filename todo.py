Task=[]

def Addtask():
    newtask=input("Enter you Task")
    Task.append(newtask)
    print(f"The Task '{newtask}' Is Added")

def Viewtask():
    for index, task in enumerate(Task):
        print(f"Task #{index}, {task}")

def Deletetask():
    Viewtask()
    try:
        deletetask=int(input("Select the task to be deleted"))                                                                                                                 `          `                      
        if deletetask < len(Task):
            Task.pop(deletetask)
            print(f"The Task '{deletetask}' has been removed")
    except:
        print("The Task not Found in the task list")    


if __name__ == "__main__":
    print("Welcome to the todo App")

    while True:
        print("\n")
        print("Select Which option to perform")
        print("--------------------------------------")
        print('\n')
        print("1.Add New Task")
        print("2.View Tasks")
        print("3.Delete Task")
        print("4.Quit")

        choice=input("Enter Your Choice")

        if(choice == "1"):
            Addtask()
        elif(choice == "2"):
            Viewtask()
        elif(choice == "3"):
            Deletetask()
        elif(choice == "4"):
            break
        else:
            print("Invalid Input")
    
    print("GoodBye")
