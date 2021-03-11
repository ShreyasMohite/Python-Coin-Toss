from tkinter import *
import random
from PIL import ImageTk
from PIL import *
from PIL import Image

class Toss:
    def __init__(self,root):
        self.root=root
        self.root.title("Coin Toss")
        self.root.geometry("400x400")
        self.root.iconbitmap("logo581.ico")
        self.root.resizable(0,0)



        



        def on_enter1(e):
            but_Heads['background']="black"
            but_Heads['foreground']="cyan"
  
        def on_leave1(e):
            but_Heads['background']="SystemButtonFace"
            but_Heads['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"
        
        def on_enter3(e):
            but_Tails['background']="black"
            but_Tails['foreground']="cyan"
  
        def on_leave3(e):
            but_Tails['background']="SystemButtonFace"
            but_Tails['foreground']="SystemButtonText"


        coin=["Heads","Tails"]

        
        def clear():
            lab_select_toss.config(text="Toss Again")
            lab_result.config(text="Result")
            lab_toss.config(text="")

        
        def heads():
            result=random.choice(coin)
            player="Heads"
            lab_toss.config(text=result)
            if result==player:
                lab_result.config(text="Player won")
            else:
                lab_result.config(text="Player lose")

        
        def Tails():
            result=random.choice(coin)
            player="Tails"   
            lab_toss.config(text=result)
            if result==player:
                lab_result.config(text="Player won")
            else:
                lab_result.config(text="Player lose")

            
#======================frame======================
        mainframe=Frame(self.root,width=400,height=400,relief="ridge",bd=3,bg="gray77")
        mainframe.place(x=0,y=0)

        lab_select_toss=Label(mainframe,text="Select Toss",font=("times new roman",16))
        lab_select_toss.place(x=150,y=10)

        self.original = Image.open("C:\\Users\\SHREYAS\\Desktop\\shreyas python\\img_to_text\\imgs\\black.png")
        resized = self.original.resize((255,160),Image.ANTIALIAS)
        self.image = ImageTk.PhotoImage(resized)
        #bglab=Label(F1,image=self.image,bd=2).place(x=0,y=0)
        photo_image=Label(mainframe,image=self.image,bd=2)
        photo_image.place(x=60,y=55)

        lab_toss=Label(mainframe,text="",font=("times new roman",16))
        lab_toss.place(x=170,y=250)

        lab_result=Label(mainframe,text="Result",font=("times new roman",16))
        lab_result.place(x=170,y=290)


        but_Heads=Button(mainframe,width=12,text="Heads",font=('times new roman',13),cursor="hand2",command=heads)
        but_Heads.place(x=10,y=330)
        but_Heads.bind("<Enter>",on_enter1)
        but_Heads.bind("<Leave>",on_leave1)

        but_clear=Button(mainframe,width=12,text="Clear",font=('times new roman',13),cursor="hand2",command=clear)
        but_clear.place(x=140,y=330)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

        but_Tails=Button(mainframe,width=12,text="Tails",font=('times new roman',13),cursor="hand2",command=Tails)
        but_Tails.place(x=270,y=330)
        but_Tails.bind("<Enter>",on_enter3)
        but_Tails.bind("<Leave>",on_leave3)


if __name__=="__main__":
    root=Tk()
    Toss(root)
    root.mainloop()