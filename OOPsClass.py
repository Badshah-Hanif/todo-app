#simple object orinted programming


class Simple:

   
    todo = []
    
    #insert value:
    def add_insert(self):
        print("\n=== welcome to Insert Menu ===")
        input_value=input("enter your todo work : ")
        com_value = input_value.lower()
        Simple.todo.append(com_value)
        print(f"the {com_value} task is successfully insert.")
        print("=*=*=*=*=*=*=*=*=*=*=\n")   
    
    #view tasks
    def view(self,todo):
        print("=== welcome to view Menu ===")
        length=len(todo)
        if length==0 or not todo:
            print("No items found.")
        else:
            for i,task in enumerate(todo,1):
                print(f"task {i}  {task}")
            print("the above all task is your todo tasks. ")
        print("=*=*=*=*=*=*=*=*=*=*=\n")   
                
    #DELET TASK FROM TODO
    def delet_task(self,todo):
        print("\n=== welcome to Delete Menu ===")
        length = len(todo)
        if not todo:
            print("to do list is empty : ")
        else:  
            input_value=input("enter value do you want to remove : ")
            com_value = input_value.lower()
            if com_value in todo:
                indx=todo.index(com_value)
                rmv=todo.pop(indx)
                print(f"The {rmv} task successfully remove")
            else:
                print(f"the {com_value} dose not exist")
        print("=*=*=*=*=*=*=*=*=*=*=\n")        
        
            
    #update task
    def update_task(self,todo):
        print("\n=== welcome to update Menu ===")
        if not todo:
            print("to do list is empty: ")
        else:
            search_value=input("enter value do you want to update : ")   
            com_value=search_value.lower()      
            if com_value in todo:
                indx=todo.index(com_value)
                updat_value=input("enter new value : ")
                recom_value=updat_value.lower()
                todo[indx]=recom_value
                print(f"the {recom_value} task is successfully updated.")
            else:
                print(f"the {search_value} is not exist")
                add_value=input("do you want to add the given value Y/N :  ")
                if add_value == 'y' or add_value == 'Y':
                    todo.append(com_value)
                    print(f"{com_value} task is successfully added")
                elif add_value == 'n' or add_value=='N':
                    print("")
                else:
                    print("enter valid input")  
        print("=*=*=*=*=*=*=*=*=*=*=\n")    
        
#====== MAIN BODY OF THE PROGRAM ======            

t = Simple()
print("\n welcome to TODO LIST app ")
 
while True:
    print("===== Main Menu =====")
    print("1 for add Task\n2 for view Tasks\n3 for delete task\n4 for update Task\n5 for exit the program\n")
    print("======= SELECT YOUR MENU =======")
    check=(input("ENTER YOUR MENU HERE ::>>  "))
    print("=*=*=*=*=*=*=*=*=*=*=*=\n")
    if check==1 or check=="1":
        t.add_insert()
    elif check ==2 or check=="2":
        t.view(t.todo)
    elif check ==3 or check=="3":
        t.delet_task(t.todo)
    elif check==4 or check=="4":
        t.update_task(t.todo)
    elif check==5 or check=="5":
        break
    else:
       print("PLEASE ENTER VALID INPUT") 