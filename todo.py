# -*- coding: utf-8 -*-
"""
Created on Sun May  9 15:12:48 2021

@author: Samet
"""

from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle


root = Tk()
root.title ("To Do App")
root.geometry("520x400")
root.configure(background="#778899")


my_font = Font (family ="Forte",size =20,weight ="bold")
my_frame = Frame(root)
my_frame.pack(pady=30)


my_list = Listbox (my_frame, font = my_font,width=20,height=5,
                   bg= "SystemButtonFace", bd=0,
                   fg="#778899",selectbackground="light pink",
                   #selectforeground="green",
                   background= "light blue",
                   activestyle="none"   )
my_list.pack(side=LEFT,fill=BOTH)


    
my_scrollbar= Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT,fill=BOTH)
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

my_entry= Entry(root, font= ("Centaur",18))
my_entry.pack(pady=15)


button_frame = Frame(root)
button_frame.pack(padx=5)

def delete_item():
    my_list.delete(ANCHOR)
    
def add_item():
    my_list.insert(END,my_entry.get())
    my_entry.delete(0,END)
    
def cross_item():
    my_list.itemconfig(my_list.curselection(),fg="red")
    my_list.selection_clear(0,END)
    
def uncross_item():
    my_list.itemconfig(my_list.curselection(),fg="#778899")
    my_list.selection_clear(0,END)
    
def clear_uncross_item():
    indexNumber=0
    while (indexNumber < my_list.size()):
        if (my_list.itemcget(indexNumber,"fg")=="red"):
            my_list.delete(my_list.index(indexNumber)) 
            
        else:
            indexNumber +=1

def save_list():
    save_file = filedialog.asksaveasfilename(initialdir="C:/Users/Samet/Desktop/todolists",
                                             title="Save List",
                                             filetypes=(("Dat Files","*.dat"),
                                                        ("All Files","*.*")))
                                            
    if save_file:
            pass
    else:
            save_file = f"{save_file}.dat"

    indexNumber=0
    while (indexNumber < my_list.size()):
        if (my_list.itemcget(indexNumber,"fg")=="red"):
            my_list.delete(my_list.index(indexNumber)) 
            indexNumber=0
            
        indexNumber +=1   
        
    
    list_elements= my_list.get(0,END)
    output_file= open(save_file,"wb") 
    pickle.dump(list_elements,output_file)
    

def open_list():
    open_file = filedialog.askopenfilename(initialdir="C:/Users/Samet/Desktop/todolists",
                                             title="Open List",
                                             filetypes=(("Dat Files","*.dat"),
                                                        ("All Files","*.*")))
                                            
    if open_file:
        my_list.delete(0,END)
        input_file = open(open_file,"rb")
        contents= pickle.load(input_file)
        for item in contents:
            my_list.insert(END,item)
        

def clear_list():
    my_list.delete(0,END)
        

my_menu = Menu(root)
root.config (menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File",menu=file_menu)

file_menu.add_command (label ="Save List",command=save_list)
file_menu.add_command (label ="Open List",command=open_list)
file_menu.add_separator()
file_menu.add_command (label ="Clear List",command=clear_list)


delete_button = Button(button_frame, text= "Delete Task",
                       command= delete_item)
add_button = Button(button_frame, text="Add Task",
                    command= add_item)

cross_button =Button(button_frame, text="Cross off Task",
                    command= cross_item)
uncross_button =Button(button_frame, text="Uncross off Task",
                    command= uncross_item)
clear_uncross_button = Button(button_frame,text="Clear all Uncrossed Items",
                              command=clear_uncross_item)

delete_button.grid(row=0,column=0)
add_button.grid(row=0,column=1,padx=15)
cross_button.grid(row=0,column=2)
uncross_button.grid(row=0,column=3) 
clear_uncross_button.grid(row=0,column=4,padx=15) 


root.mainloop()



