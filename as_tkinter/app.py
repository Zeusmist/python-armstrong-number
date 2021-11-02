import tkinter as tk

root = tk.Tk()

canvas1 = tk.Canvas(root, width=400, height=300, relief='raised')
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(200, 140, window=entry1)

label2 = tk.Label(root, text='Please input your Number?:')
label2.config(font=('helvetica', 10))
canvas1.create_window(200, 100, window=label2)


def display_label(text):
    label1 = tk.Label(root, text=text)
    label1.config(font=('helvetica', 14))
    canvas1.create_window(200, 230, window=label1, width=400)


def AmstrongNumber():
    try:
        x1 = int(entry1.get())
        if x1 >= 100 and x1 <= 999:
            cubeSum = 0
            stringified = str(x1)
            for x in stringified:
                cubeSum += int(x) * int(x) * int(x)
            if cubeSum == x1:
                display_label("This is an Amstrong Number")
            else:
                display_label("This is not an Amstrong Number")
        else:
            display_label("Value is not a three digit number")
    except ValueError:
        display_label('Please enter an integer')


button1 = tk.Button(text='Check if its an Amstrong Number',
                    command=AmstrongNumber, bg='brown', fg='white')
canvas1.create_window(200, 180, window=button1)

root.mainloop()
