from tkinter import *
root=Tk()
#root.geometry('{}*{}'.formate(800,600))
root.maxsize(width=800, height=600)
root.title("MS-Logo paint")
class draw:
    def __init__(self,root):
        self.root=root
        self.radiobuttonValue = IntVar()
        self.radiobuttonValue.set(1)
        self.leftframe=Frame(root)
        self.leftframe.pack(side=LEFT, fill = Y)
        self.canvas=Canvas(root,width=800,height=600,relief=RAISED, borderwidth=5)   
        self.canvas.pack(side = RIGHT)
        self.canvas.bind("<ButtonPress-1>",self.btpress)
        self.canvas.bind("<B1-Motion>",self.line)
        self.canvas.bind("<ButtonRelease-1>",self.make)
        self.create()
    def btpress(self,event):
        self.x0=event.x
        self.y0=event.y
        
    def delteAll(self):
        self.canvas.delete("all")

    def line(self,event):
        if(self.radiobuttonValue.get() == 5):
            self.canvas.create_line(self.x0,self.y0,event.x,event.y)
        elif(self.radiobuttonValue.get() == 6):
            self.canvas.create_line(self.x0,self.y0,event.x,event.y)
            self.x0=event.x
            self.y0=event.y
        
    def create(self):
        self.labelThickness = Label(
                            self.leftframe,
                            text = "drawing tools list:")
        self.labelThickness.grid(row = 0,
                                 column = 0, pady = 2, padx = 3)
        Radiobutton(self.leftframe,
                    text = "line",
                    variable = self.radiobuttonValue,
                    value = 1).grid(padx = 3, pady = 2,
                                    row = 1, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "Circle",
                    variable = self.radiobuttonValue,
                    value = 2).grid(padx = 3, pady = 2,
                                    row = 2, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "Triangle",
                    variable = self.radiobuttonValue,
                    value = 3).grid(padx = 3, pady = 2,
                                    row = 3, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "Rectangle",
                    variable = self.radiobuttonValue,
                    value = 4).grid(padx = 3, pady = 2,
                                    row = 4, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "Pattern-1",
                    variable = self.radiobuttonValue,
                    value = 5).grid(padx = 3, pady = 2,
                                    row = 5, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "Pencil",
                    variable = self.radiobuttonValue,
                    value = 6).grid(padx = 3, pady = 2,
                                    row = 6, column = 0,
                                    sticky = NW
                                    )
        
        self.clearbt = Button(self.leftframe, text = "clear paper",
                                      command = self.delteAll)
        self.clearbt.grid(padx = 3, pady = 2,
                                    row = 7 , column = 0,
                                    sticky = NW)
    def make(self,event):
        if self.radiobuttonValue.get() == 1:
            self.canvas.create_line(self.x0,self.y0,event.x,event.y)

        elif self.radiobuttonValue.get() == 2:
            self.canvas.create_oval(self.x0,self.y0,event.x,event.y)

        elif self.radiobuttonValue.get() == 3:
            self.canvas.create_line(self.x0,self.y0,event.x,event.y)
            self.canvas.create_line(self.x0-(event.x-self.x0),event.y,event.x,event.y)
            self.canvas.create_line(self.x0,self.y0,self.x0-(event.x-self.x0),event.y)

        elif(self.radiobuttonValue.get() == 4):
            self.canvas.create_rectangle(self.x0,self.y0,event.x,event.y)         
            
            
            
        

obj=draw(root)
mainloop()

    
    