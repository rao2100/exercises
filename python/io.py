import tkinter as tk
import tkinter.messagebox
import datetime
import math


def greet():
    # name = input("What is your name?")
    # print("Hello, {}, nice to meet you!".format(name))
    print("Hello, {}, nice to meet you!".format(input("What is your name? : ")))

def count():
    user_input = input("What is the input string? : ")
    print("{} has {} characters.".format(user_input, len(user_input)))

def count_gui_get_len(top):    
    # tk.messagebox.showinfo( "Hello Python", "Hello World")
    top.result_text.set(top.entry_user.get() + " has " + str(len(top.entry_user.get())) + " characters.")

def count_gui():    
    top = tk.Tk()    
    # add widgets
    top.label_userinput = tk.Label(top, text="User Input")    
    top.label_userinput.grid(row=0)
    top.entry_user = tk.Entry(top, bd =5)    
    top.entry_user.grid(row=0,column=1)
    top.result_text = tk.StringVar()
    top.label_result = tk.Label(top, text="result", textvariable = top.result_text)    
    top.label_result.grid(row=1,column=1)
    top.button_getlen = tk.Button(top, text ="Get length!", command = lambda: count_gui_get_len(top))
    top.button_getlen.grid(row=1)
    top.mainloop()
 
def retirement():
    print("Retirement Calculator")
    now = datetime.datetime.now()    
    age = input("What is your current age? : ")
    retirement_age = input("At what age would you like to retire? : ")
    years_left = int(retirement_age) - int(age)
    year_retire = now.year + years_left
    if(years_left < 0):
        print("Congratulations you can already retire...")    
        return
    print("You have {} years left until you can retire.".format(years_left))
    print("It's {}, so you can retire in {}.".format(now.year, year_retire))

def print_quotes():
    quote = input("What is the quote? : ")
    author = input("Who said it? : ")
    print(author + " says, " + "\"" + quote + "\"")

def mad_lib():
    noun = input("Enter a noun : ")
    verb = input("Enter a verb : ")
    adj = input("Enter an adjective : ")
    adverb = input("Enter an adverb : ")
    output = "Do you <verb> your <adj> <noun> <adverb> ? That's hilarious!".replace("<verb>", verb).replace("<adj>", adj).replace("<noun>", noun).replace("<adverb>", adverb)
    print(output)
 
def simple_math():
    first_input = input("What is the first number? : ")    
    second_input = input("What is the second number? : ")
    first_value = 0
    second_value = 0
    try:
        first_value = int(first_input)
        second_value = int(second_input)
    except ValueError:
        print("Error non numeric value entered!")
        return
    if(first_value < 0 or second_value < 0):
        print("Error negative number entered!")
        return
    
    print(
        first_input + " + " + second_input + " = " + str(first_value + second_value) + "\n"
        + first_input + " - " + second_input + " = " + str(first_value - second_value) + "\n"
        + first_input + " * " + second_input + " = " + str(first_value * second_value) + "\n"
        + first_input + " / " + second_input + " = " + str(first_value / second_value) + "\n"
    )
    
    


# greet()
# count()
# count_gui()
# retirement()
# simple_math()
# print_quotes()
mad_lib()



