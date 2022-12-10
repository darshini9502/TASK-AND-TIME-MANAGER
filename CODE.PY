import datetime 
import tkinter
# pssd means password, ussnm is username def user_information(ussnm, pssd):
name = input("enter your name please: ") address = input("your address")
age = input("Your age please")
ussnm_ = ussnm+" task.txt"
f = open(ussnm_, 'a') 
f.write(pssd) 
f.write("\nName: ") 
f.write(name)
f.write('\n') 
f.write("Address :") 
f.write(address) 
f.write('\n')
f.write("Age :") 
f.write(age) 
f.write('\n')
f.close()
def signup():
print("Please enter the username by which you wanna access your account") 
username = input("please enter here: ")
password = input("Enter a password: ")
user_information(username, password)
print("Please proceed towards log in")
login()
def login():
print("Please enter your username ") user_nm = input("Enter here: ")
 # Password as entered while logging in pssd_wr = (input("enterr the password"))+'\n'
 try:
usernm = user_nm+" task.txt" f_ = open(usernm, 'r')
# variable 'k' contains the password as saved # in the file
k = f_.readlines(0)[0]
f_.close()
# Checking if the Password entered is same as # the password saved while signing in
if pssd_wr == k:
a=0 while(a!=5):
print("1--to view your data \n2--To add task \n3--Update\task \n4-- VIEW TASK STATUS \n5--Display Task Manager \n6--Exit")
a = input() if a == '1':
view_data(usernm) elif a == '2':
# add task
task_information(usernm) elif a == '3':
task_update(user_nm) elif a == '4':
task_update_viewer(user_nm) elif a=='5':
display_gui(usernm) elif a == '6':
break; else:
print("Wrong input !") else:
print("YOUR PASSWORD OR USERNAME IS WRONG") login()
except Exception as e: print(e)
login()
 def view_data(username): ff = open(username, 'r') print(ff.read()) ff.close()
def display_gui(username): root=tkinter.Tk() root.geometry("400x300") root.title('Task Manager') ff=open(username, 'r') data=ff.read()
ff.close()
task_list = data.splitlines() root.config(bg='#223441') root.resizable(width=False,height=False)
frame = tkinter.Frame(root) frame.pack(pady=30)
lb = tkinter.Listbox( frame,
width=35,
height=10,
font=('Times', 14),
bd=0,
fg='#464646', highlightthickness=0, selectbackground='#a6a6a6', activestyle="none",
)
lb.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
for item in task_list: lb.insert(tkinter.END, item)
sb = tkinter.Scrollbar(frame) sb.pack(side=tkinter.RIGHT, fill=tkinter.BOTH)
 lb.config(yscrollcommand=sb.set) sb.config(command=lb.yview)
#canvas=tkinter.Canvas(root,width=400,height=300) #canvas.create_text(100,50,text=data,fill="black") #canvas.pack()
root.mainloop()
def task_information(username):
print("Enter number of task you want to ADD") j = int(input())
f1 = open(username, 'a')
for i in range(1, j+1):
task = input("enter the task") target = input("enter the target") pp = "TASK "+str(i)+' :'
qq = "TARGET "+str(i)+" :"
f1.write(pp)
f1.write(task)
f1.write('\n')
f1.write(qq)
f1.write(target)
f1.write('\n')
print("Do u want to stop press space bar otherwise enter") s = input()
if s == ' ': break
f1.close()
def task_update(username):
username = username+" TASK.txt"
print("Please enter the tasks which are completed ") task_completed = input()
print("Enter task which are still not started by you") task_not_started = input()
print("Enter task which you are doing") task_ongoing = input()
fw = open(username, 'a')
DT = str(datetime.datetime.now())
 fw.write(DT)
fw.write("\n") fw.write("COMPLETED TASK \n") fw.write(task_completed) fw.write("\n")
fw.write("ONGOING TASK \n") fw.write(task_ongoing) fw.write("\n")
fw.write("NOT YET STARTED\n") fw.write(task_not_started) fw.write("\n")
def task_update_viewer(username): ussnm = username+" TASK.txt" o = open(ussnm, 'r') print(o.read())
o.close()
print("WELCOME TO TASK MANAGER")
a = int(input("If you are a new user press 1 else press 0 ::")) if a == 1:
signup() elif a == 0:
login() else:
print("You have provided wrong input !")
  
