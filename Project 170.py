# -*- coding: utf-8 -*-
"""
Created on Sat Aug 13 14:31:45 2022

@author: Fierce bird//
"""

from tkinter import*

root=Tk()
root.title("Grade Marking")
root.geometry("500x600")

Grade_3_label=Label(root)
Grade_5_label=Label(root)
Grade_10_label=Label(root)

class Grade3():
    def __init__(self,arts,math):
        self.arts = arts
        self.maths = math
    def percentage(self):
        total_marks = self.maths + self.arts
        Grade = total_marks * 100
        Grade_3_percent = Grade/200
        Grade_3_label["text"]=Grade_3_percent
        
class Grade5():
    def __init__(self,arts,math,SS):
        self.arts = arts
        self.maths = math
        self.SS = SS
    def percentage(self):
        total_marks = self.maths + self.arts + self.SS
        Grade = total_marks * 100
        Grade_5_percent = Grade/300
        Grade_5_label["text"]=Grade_5_percent

class Grade10():
    def __init__(self,arts,math,SS,foriegn_language):
        self.arts = arts
        self.maths = math
        self.SS = SS
        self.foriegn_language = foriegn_language
    def percentage(self):
        total_marks = self.maths + self.arts + self.SS + self.foriegn_language
        Grade = total_marks * 100
        Grade_10_percent = Grade/400
        Grade_10_label["text"]=Grade_10_percent

Grade3_obj = Grade3(100,95)

Grade3_btn=Button(root,text="Grade 3",command=Grade3_obj.percentage)
Grade3_btn.pack(padx=20,pady=20)
Grade_3_label.pack(padx=20,pady=20)

Grade5_obj = Grade5(90,95,100)

Grade5_btn=Button(root,text="Grade 5",command=Grade5_obj.percentage)
Grade5_btn.pack(padx=20,pady=20)
Grade_5_label.pack(padx=20,pady=20)

Grade10_obj = Grade10(90,95,100,70)

Grade10_btn=Button(root,text="Grade 10",command=Grade10_obj.percentage)
Grade10_btn.pack(padx=20,pady=20)
Grade_10_label.pack(padx=20,pady=20)

root.mainloop()



