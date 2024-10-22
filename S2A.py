from tkinter import *
def create_contact():
    window = Tk()
    window.title("S2A")
    cnv = Canvas(window,width=500,height=500,bg="white")
    cnv.pack()
    cnv.create_text(150,30,text="контактная информация",anchor=NW,font=(None,15))
    cnv.create_text(350,280,text="a_seferovw",anchor=NW,font=(None,15))
    insta_photo = PhotoImage(file="my_inst1.png")
    insta_w =cnv.create_image(300,80,anchor = NW,image = insta_photo)
    insta_write = PhotoImage(file="write_inst.png")
    insta =cnv.create_image(240,270,anchor = NW,image = insta_write)
    back_image = PhotoImage(file="back_button.png")
    back_button =cnv.create_image(10,10,anchor = NW,image = back_image)


   # window.mainloop()