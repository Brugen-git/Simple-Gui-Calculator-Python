from distutils.cmd import Command
from mimetypes import common_types
import tkinter as tk
from tkinter.dialog import DIALOG_ICON
from tkinter.font import BOLD
LIGHT_GRAY="#F5F5F5"
WHITE="#FFFFFF"
DIGITS_FONT_STYLE=("Times New Roman",24,"bold")
DEFAULT_FONT_STYLE=("Times New Roman",20)
OFF_WHITE="#F8FAFF"
LABEL_COLOR="Black"
SMALL_FONT_SIZE=("Times New Roman",16,"bold")
LARGE_FONT_SIZE=("Times New Roman",40)
class Calculator:
    def __init__(self):
        self.window=tk.Tk()
        self.window.geometry("500x500")
        self.window.resizable(0,0)
        self.window.title("Calculator V1")
        self.total_expression=""
        self.current_expression=""
        self.display_frame=self.create_display_frame()
        self.buttons_frame=self.create_buttons_frame()
        self.total_label, self.label=self.create_display_labels()
        self.digits={
            7:(1,1),8:(1,2),9:(1,3),
            4:(2,1),5:(2,2),6:(2,3),
            1:(3,1),2:(3,2),3:(3,3),
            0:(4,2),'.':(4,1)
        }
        self.operations={"/":"\u00F7","*":"\u00D7","-":"-","+":"+"}
        self.buttons_frame.rowconfigure(0,weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(x,weight=1)
            self.buttons_frame.columnconfigure(x,weight=1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_equals_button()

    def create_display_frame(self):
        frame=tk.Frame(self.window, height=100, bg=LIGHT_GRAY ,highlightbackground = "light blue", highlightthickness = 2, bd=0)
        frame.pack(expand=True, fill="both")
        return frame


    def create_buttons_frame(self):
        frame=tk.Frame(self.window, highlightbackground = "light blue", highlightthickness = 2, bd=0)
        frame.pack(expand=True, fill="both")
        return frame


    def create_display_labels(self):
        total_label=tk.Label(self.display_frame, text=self.total_expression,anchor=tk.E, font=SMALL_FONT_SIZE, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24)
        total_label.pack(expand=True,fill="both")
        label=tk.Label(self.display_frame, text=self.current_expression,anchor=tk.E, font=LARGE_FONT_SIZE, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24)
        label.pack(expand=True,fill="both")
        return total_label,label


    def create_digit_buttons(self):
        for digit,grid_value in self.digits.items():
            button=tk.Button(self.buttons_frame, text=str(digit), bg="White", fg=LABEL_COLOR, font=DIGITS_FONT_STYLE,activebackground="light cyan", borderwidth="0.5",command=lambda x=digit:self.add_to_expression(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)


    def create_operator_buttons(self):
        i=0
        for operator, symbol in self.operations.items():
            button=tk.Button(self.buttons_frame,text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,activebackground="light cyan", borderwidth="0.5", command=lambda x=operator: self.append_operator(x))
            button.grid(row=i,column=4, sticky=tk.NSEW)
            i+=1

    def clear(self):
        self.current_expression=""
        self.total_expression=""
        self.update_label()
        self.update_total_label()


    def create_clear_button(self):
        button=tk.Button(self.buttons_frame,text="Clear", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,activebackground="light cyan", borderwidth="0.5", command=self.clear)
        button.grid(row=0,column=1,columnspan=3, sticky=tk.NSEW)
    
    def evaluate(self):
        self.total_expression+=self.current_expression
        
        
        self.update_total_label()
        try:
            if self.total_expression=="1+":
                self.current_expression="One Plus"
            elif self.total_expression=="65":
                self.current_expression="UPES"
            else:
                self.current_expression=str(eval(self.total_expression))
                self.total_expression=""
        except Exception as e:
            self.current_expression="ERROR"
        finally:
            self.update_label()

    def create_equals_button(self):
        button=tk.Button(self.buttons_frame,text="=", bg="Light Blue", fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,activebackground="light cyan", borderwidth="0.5", command=self.evaluate)
        button.grid(row=4,column=3,columnspan=2, sticky=tk.NSEW)

    def update_total_label(self):
        self.total_label.config(text=self.total_expression)
    

    def add_to_expression(self,value):
        self.current_expression+=str(value)
        self.update_label()

    def append_operator(self,operator):
        self.current_expression+=operator
        self.total_expression+=self.current_expression
        self.current_expression=""
        self.update_total_label()
        self.update_label()

    def update_label(self):
        self.label.config(text=self.current_expression[:20])

    def run(self):
        self.window.mainloop()

if __name__ =="__main__":
    cal=Calculator()
    cal.run()