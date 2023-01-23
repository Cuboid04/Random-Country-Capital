from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Country And Capitals")
import random
list1=[]
list2=[]
countrybox=Entry(root)
capitalbox=Entry(root)
countrybox.place(relx=0.5, rely=0.1, anchor=CENTER)
capitalbox.place(relx=0.5, rely=0.2, anchor=CENTER)
label1=Label(root)
label2=Label(root)
label3=Label(root)
label4=Label(root)
def add_names():
    country=countrybox.get()
    list1.append(country)
    label1["text"] = str(list1)
    capital=capitalbox.get()
    list2.append(capital)
    label2["text"] = str(list2)
    

def random_name():
    country_length= len(list1)
    capital_length= len(list2)
    random_no = random.randint(0, country_length-1)
    random_no1 = random.randint(0, capital_length-1)
    name1=list1[random_no]
    label3["text"]= str(name1)
    name2=list2[random_no1]
    
    label4["text"]= str(name2)
    
    
btn1=Button(root,text="Display A Random Country And Capital", command=random_name)
btn=Button(root, text="Add A Country", command=add_names)
btn.place(relx=0.5, rely=0.3, anchor=CENTER)
btn1.place(relx=0.5, rely=0.6, anchor=CENTER)
label1.place(relx=0.5, rely=0.4, anchor=CENTER)
label2.place(relx=0.5, rely=0.5, anchor=CENTER)
label3.place(relx=0.5, rely=0.7, anchor=CENTER)
label4.place(relx=0.5, rely=0.8, anchor=CENTER)

root.mainloop()