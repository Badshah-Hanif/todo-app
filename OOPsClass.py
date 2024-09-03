#simple object orinted programming


class Simple:
   
    todo = []
    # def __init__():
        # pass
    
    #insert value:
    def add_insert(self):
        input_value=input("enter your todo work : ")
        Simple.todo.append(input_value)
    
    #view tasks
    def view(self,todo):
        length=len(todo)
        if length==0 or not todo:
            print("No items found.")
        else:
            for i,task in enumerate(todo,1):
                print(f"task {i}  {task}")
                
    #DELET TASK FROM TODO
    def delet_task(self,todo):
        length = len(todo)
        if not todo:
            print("to do list is empty : ")
        else:  
            try:
                input_value=input("enter value do you want to remove : ")
                indx=todo.index(input_value)
                rmv=todo.pop(indx)
                print(f"The {rmv} task successfully remove")
            except ValueError:
                print("the {input_value} dose not exist")
            
    #update task
    def update_task(self,todo):
        try:
            search_value=input("enter value do you want to update : ") 
            indx=todo.index(search_value)
            updat_value=input("enter new value : ")
            todo[indx]=updat_value
        except ValueError:
            print("the {search_value} is not exist")
              
             
        
            

t = Simple()
t.add_insert()
t.view(t.todo)
#print(t)    
        

print(" welcome to TODO LIST app ")
#s=Simple()
    
while True:
    #try:
    print("1 for add value\n2 for view\n3 for delete task\n4 for update\n5 for exit")
    check=(input("select menu :  "))
    if check==1 or check=="1":
        t.add_insert()
    if check ==2 or check=="2":
        t.view(t.todo)
    if check ==3 or check=="3":
        t.delet_task(t.todo)
    if check==4 or check=="4":
        t.update_task(t.todo)
    if check==5 or check=="5":
        break
    else:
       print("PLEASE ENTER VALID INPUT") 
   
   
   #except TypeError:
      # print("PLEASE ENTER VALID INPUT")

     


#if __name__=="main":
    #main()

    