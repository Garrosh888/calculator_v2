from tkinter import*
import S2A
import data_button
from data_button import Data_button

def equal(btn):
    data  = entry.get()
    for i in range(len(data)):
        if data[i] == "×":
            number1 = 0
            number2 = 0
            if i + 1 < len(data):#проверяем есть ли число после знака умножить
            #while data[i + 1]:
                if data_button.dictionary_buttons_type[data[i + 1]] == "number":#проверяем являеться ли символ числом
                    number2 = int(data[i+1])    
                    #print(number2)
                    for g in range(i+2,len(data)):
                        if data_button.dictionary_buttons_type[data[g]] == "number":
                            number2*=10
                            number2+=int(data[g])
                        else:
                            break
                    print(number2)




def s2a_button(btn):
    window.withdraw()
    S2A.create_contact()


def click_operation(btn):
    if get_last_symbol_type() == "operation":
        delete_last_symbol(btn)
        entry.insert(len(entry.get()) + 1, btn["text"])  # insert - вставка
    else:
        entry.insert(len(entry.get()) + 1, btn["text"])  # insert - вставка



def get_type(btn):
    return data_button.dictionary_buttons_type[btn]

def get_last_symbol_type():
    if len(entry.get()) == 0:
        return None
    last_symbol = entry.get()[-1]
    return get_type(last_symbol)

def delete_last_symbol(btn):
    entry.delete(len(entry.get())-1,"end")

def delete_all(btn):
    entry.delete(0,"end")

def set_button(value,row,column,click):#создание всех кнопок
    btn  = Button(cnv,text = value,font=(None,25),fg= "#454545",bg ="#fff",width=6,height=1)
    btn.bind("<Button-1>",lambda event: click(btn))#lambda
    btn.grid(row= row,column= column  )#row - номер строки, column - номер стопца

def test_function(btn):# это та функция которая все красит
    btn["bg"] = "green"
    entry.insert(len(entry.get()) +1, btn["text"])#insert - вставка
    print(get_last_symbol_type())


window = Tk()
window.title("my_cuculator")
cnv = Canvas(window,width=400,height=600,bg="black")
cnv.pack()
entry = Entry(cnv, font=(None, 35), width=19)
entry.grid(row = 0, column= 0, columnspan=4)
last_symbol = None
list_marks_1 = [Data_button("S2A",s2a_button,get_type("S2A")),Data_button("0",test_function,"number"),Data_button(".",test_function,"point"),Data_button("=",equal,"equal")]
#словарь это то что внутри { }
#list_marks_1 - список, каждый елемент списка это словарь, в каждом словаре по одному елемнту,ключ это то чо написано на
#кнопке значение это то что выполняется при нажатии на кнопку
list_marks_2 = [Data_button("1",test_function,data_button.dictionary_buttons_type["1"]),Data_button("2",test_function,"number"),
                Data_button("3",test_function,"number"),Data_button("+",click_operation,"operation")]#
list_marks_3 = [Data_button("4",test_function,"number"),Data_button("5",test_function,"number"),
                Data_button("6",test_function,"number"),Data_button("-",click_operation,"operation")]
list_marks_4 = [Data_button("7",test_function,"number"),Data_button("8",test_function,"number"),
                Data_button("9",test_function,"number"),Data_button("×",click_operation,"operation")]
list_marks_5 = [Data_button("С",delete_all,"clear_all"),Data_button("⌫",delete_last_symbol,"clear_last"),
                Data_button("÷",click_operation,get_type("÷"))]
list_marks = [list_marks_1,list_marks_2,list_marks_3,list_marks_4,list_marks_5]
row = 5#это типо у нас 5 строк
column = 0

for list in list_marks:
    for data_btn in list:
        set_button(data_btn.title,row,column,data_btn.function)
        column = column + 1
    row = row - 1
    column = 0
#цикл который создает и размищает кнопки на конве
window.mainloop()

