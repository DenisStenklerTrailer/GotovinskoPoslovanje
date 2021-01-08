from tkinter import *

def view_command():
    list1.delete(0, END)
    for row in GotovinskoPoslovanjeBackend.view():
        list1.insert(END,row)

def view_plus_command():
    list1.delete(0, END)
    for row in GotovinskoPoslovanjeBackend.view_plus():
        list1.insert(END,row)

def view_minus_command():
    list1.delete(0, END)
    for row in GotovinskoPoslovanjeBackend.view_minus():
        list1.insert(END,row)

def search_command():
    list1.delete(0,END)
    for row in GotovinskoPoslovanjeBackend.search(date_text.get(), purpose_text.get(), money_text.get()):
        list1.insert(END, row)

def add_command_plus():
    GotovinskoPoslovanjeBackend.insert(date_text.get(), purpose_text.get(), float(money_text.get()))
    list1.delete(0,END)
    list1.insert(END,(date_text.get(), purpose_text.get(), money_text.get()))
    stanje_command()

def add_command_minus():
    GotovinskoPoslovanjeBackend.insert(date_text.get(), purpose_text.get(), (-1)*(float(money_text.get())))
    list1.delete(0,END)
    list1.insert(END,(date_text.get(), purpose_text.get(), money_text.get()))
    stanje_command()

def stanje_command():
    global resultLabel
    stanje = GotovinskoPoslovanjeBackend.sum()
    resultLabel["text"] = round(stanje[0][0],2) if stanje[0][0] else "VNESI ZAČETNO STANJE"

def Get_Selected_Row(event):
    global selected_tuple
    index = list1.curselection()[0]
    selected_tuple=list1.get(index)
    entry1.delete(0,END)
    entry1.insert(END,selected_tuple[1])
    entry2.delete(0, END)
    entry2.insert(END,selected_tuple[2])
    entry3.delete(0, END)
    entry3.insert(END,selected_tuple[3])

def delete_command():
    GotovinskoPoslovanjeBackend.delete(selected_tuple[0])
    view_command()
    stanje_command()

def update_command():
    GotovinskoPoslovanjeBackend.update(selected_tuple[0], date_text.get(), purpose_text.get(), money_text.get())
    view_command()
    stanje_command()

try:
    window = Tk()
    print("TEST")
    window.wm_title("GOTOVINSKO POSLOVANJE KRAJEVNE SKUPNOSTI")

    ################ TEXTS ################
    # DATUM #
    label1 = Label(window, text="DATUM")
    label1.grid(row=0, column=0)
    # NAMEN #
    label2 = Label(window, text="NAMEN")
    label2.grid(row=0, column=2)
    # € #
    label3 = Label(window, text="€")
    label3.grid(row=0, column=4)

    label3 = Label(window, text="STANJE:")
    label3.grid(row=9, column=4)

    ################ INPUTS ################
    date_text = StringVar()
    entry1 = Entry(window, textvariable = date_text)
    entry1.grid(row=0, column=1)

    purpose_text = StringVar()
    entry2 = Entry(window, textvariable = purpose_text)
    entry2.grid(row=0, column=3)

    money_text = StringVar()
    entry3 = Entry(window, textvariable = money_text)
    entry3.grid(row=0, column=5)
    import GotovinskoPoslovanjeBackend

    ################ LIST BOX ################

    list1 = Listbox(window, height=10, width=58)
    list1.grid(row=1, column=0, rowspan=10, columnspan=4)

    ################ SCROLLBAR ################

    sb1 = Scrollbar(window)
    sb1.grid(row=1,column=4, rowspan=10)
    list1.configure(yscrollcommand=sb1.set)
    sb1.configure(command=list1.yview)

    list1.bind('<<ListboxSelect>>', Get_Selected_Row)

    ################ BUTTONS ################

    b2 = Button(window, text = "PRIHODEK",height=2, width=12, command=add_command_plus)
    b2.grid(row=3, column=5, rowspan=2)

    b3 = Button(window, text = "ODHODEK",height=2, width=12, command=add_command_minus)
    b3.grid(row=5, column=5, rowspan=2)

    b4 = Button(window, text = "PRIKAŽI VSE", width=12, command=view_command)
    b4.grid(row=1, column=4)

    b4 = Button(window, text = "VSI PRIHODKI", width=12, command=view_plus_command)
    b4.grid(row=1, column=5)

    b4 = Button(window, text = "VSI ODHODKI", width=12, command=view_minus_command)
    b4.grid(row=1, column=6)

    b5 = Button(window, text = "IZBRIŠI", width=12, command=delete_command)
    b5.grid(row=5, column=6)

    b1 = Button(window, text = "IŠČI", width=12, command=search_command)
    b1.grid(row=3, column=6)

    b1 = Button(window, text = "POSODOBI", width=12, command=update_command)
    b1.grid(row=4, column=6)

    b1 = Button(window, text = "ZAPRI", width=12, command=window.destroy)
    b1.grid(row=9, column=6)

    ################ LABELS ################

    # Create and emplty Label to put the result in
    resultLabel = Label(window, text = "")
    resultLabel.grid(row=9,column=5)

    stanje_command()

    window.mainloop()
except Exception as e:
    import time
    print(e)
    time.sleep(5)