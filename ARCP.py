from tkinter import *
from tkinter import font
import math

class Calc():
    def __init__(self):
        self.total = 0
        self.current = ""
        self.new_num = True
        self.op_pending = False
        self.op = ""
        self.eq = False

    def num_press(self, num):
        self.eq = False
        temp = text_box.get()
        temp2 = str(num)
        if self.new_num == True:
            self.current = temp2
            self.new_num = False
        else:
            if temp2 == '.' and '.' in temp:
                    return
            self.current = temp + temp2
            while len(self.current) > 1 and self.current[0] == '0' and self.current[1] != '.':
                self.current = self.current[1:]
        self.display(self.current)

    def calc_total(self):
        self.eq = True
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        else:
            self.total = float(text_box.get())

    def display(self, value):
        text_box.delete(0, END)
        text_box.insert(0, value)

    def do_sum(self):
        if self.op == "add":
            self.total += self.current
        elif self.op == "minus":
            self.total -= self.current
        elif self.op == "times":
            self.total *= self.current
        elif self.op == "divide" and self.current:
            self.total /= self.current
        else:
            self.total = 0
        self.new_num = True
        self.op_pending = False
        self.display(self.total)

    def operation(self, op):
        self.current = float(self.current)
        if self.op_pending == True:
            self.do_sum()
        elif self.eq == False:
            self.total = self.current
        self.new_num = True
        self.op_pending = True
        self.op = op
        self.eq = False

    def cancel(self):
        self.eq = False
        if self.new_num == False:
            self.current = "0"
            self.display(0)
            self.new_num = True

    def all_cancel(self):
        self.cancel()
        self.new_num = False
        self.total = 0

    def sign(self):
        self.eq = False
        self.current = -(float(text_box.get()))
        self.display(self.current)

    def pi(self):
        self.current = math.pi
        self.eq = False
        self.new_num = True
        self.display(self.current)

    def kv(self):
        temp = float(text_box.get())
        self.current = temp * temp
        self.eq = True
        self.new_num = True
        self.total = self.current
        self.display(self.current)

    def sqrt(self):
        temp = float(text_box.get())
        self.current = math.sqrt(temp)
        self.eq = True
        self.new_num = True
        self.total = self.current
        self.display(self.current)

    def sin(self):
        temp = float(text_box.get())
        self.current = math.sin(math.radians(temp))
        self.eq = True
        self.new_num = True
        self.total = self.current
        self.display(self.current)

    def tan(self):
        temp = float(text_box.get())
        self.current = math.tan(math.radians(temp))
        self.eq = True
        self.new_num = True
        self.total = self.current
        self.display(self.current)


class My_Btn(Button):
    def btn_cmd(self, num):
        self["command"] = lambda: sum.num_press(num)



# Windows settings
sum = Calc()
root = Tk()
root.geometry("433x485") #Window size
root.resizable(0, 0) #window isn't resizeble
calc = Frame(master=root, height = 400, width = 400, bg="black") # change background
root.title("AR Calculator Project")
dFont = font.Font(weight='bold') # Font
font.families()

# Create grid
calc.grid()

# Enter button
text_box = Entry(calc, justify=RIGHT, width = 69)
text_box.grid(row = 0, column = 0, columnspan = 8, pady = 20)
text_box.insert(0, "0")

# Create number buttons
numbers = "789456123"
i = 0
bttn = []
for j in range(1,4):
    for k in range(3):
        bttn.append(My_Btn(calc, text = numbers[i]))
        bttn[i].grid(row = j, column = k)
        bttn[i].config(height= 4, width=14, bg="grey")
        bttn[i].btn_cmd(numbers[i])
        i += 1

# Button 0
bttn_0 = Button(calc, text = "0")
bttn_0["command"] = lambda: sum.num_press(0)
bttn_0.grid(row = 4, column = 1)
bttn_0.config(height=4,width=14, bg="grey")

# Divide button
bttn_div = Button(calc, text = chr(247))
bttn_div["command"] = lambda: sum.operation("divide")
bttn_div.grid(row = 1, column = 3)
bttn_div.config(height=4,width=14)

# Multiplication button
bttn_mult = Button(calc, text = "X")
bttn_mult["command"] = lambda: sum.operation("times")
bttn_mult.grid(row = 2, column = 3)
bttn_mult.config(height=4,width=14)

# Subtraction button
minus = Button(calc, text = "-")
minus["command"] = lambda: sum.operation("minus")
minus.grid(row = 3, column = 3)
minus.config(height=4,width=14)

# Decimal button
point = Button(calc, text = ".")
point["command"] = lambda: sum.num_press(".")
point.grid(row = 4, column = 2)
point.config(height=4,width=14, bg="grey")

# Addition button
add = Button(calc, text = "+")
add["command"] = lambda: sum.operation("add")
add.grid(row = 4, column = 3)
add.config(height=4,width=14)

# "±" number
neg= Button(calc, text = "±")
neg["command"] = sum.sign
neg.grid(row = 4, column = 0)
neg.config(height=4,width=14, bg="grey")

# Clear button
clear = Button(calc, text = "C")
clear["command"] = sum.cancel
clear.grid(row = 5, column = 1)
clear.config(height=4,width=14, bg = "red4")

# AC button
all_clear = Button(calc, text = "AC")
all_clear["command"] = sum.all_cancel
all_clear.grid(row = 5, column = 2)
all_clear.config(height=4,width=14, bg = "red4")

# Equation button
equals = Button(calc, text = "=")
equals["command"] = sum.calc_total
equals.grid(row = 5, column = 3)
equals.config(height=4,width=14)

# Pi number button
pi = Button(calc, text = "π")
pi["command"] = sum.pi
pi.grid(row = 6, column = 3)
pi.config(height=4,width=14, bg="cornflower blue")

# Square button
kv = Button(calc, text = "x²")
kv["command"] = sum.kv
kv.grid(row = 6, column = 1)
kv.config(height=4,width=14, bg="cornflower blue")

# Root number button
sqrt = Button(calc, text = "√")
sqrt["command"] = sum.sqrt
sqrt.grid(row = 6, column = 2)
sqrt.config(height=4,width=14, bg="cornflower blue")

# Sin button
sin = Button(calc, text = "sin")
sin["command"] = sum.sin
sin.grid(row = 6, column = 0)
sin.config(height=4,width=14, bg="cornflower blue")

# Tan button
tan = Button(calc, text = "tan")
tan["command"] = sum.sin
tan.grid(row = 5, column = 0)
tan.config(height=4,width=14, bg="cornflower blue")

# Programm start
root.mainloop()