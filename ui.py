import os
from tkinter import *
from tkinter import ttk
import tkinter
from PIL import Image, ImageTk
from tkinter import messagebox
from developer import Developer
from hand_gesture import run_hand_gestures
from help import Help
from four_finger import run_hand_gestures_4fing
from three_finger import run_hand_gestures_3fing


class Custom_Hand_Gesture:
        def __init__(self,root):
                self.root=root
                self.root.geometry("1920x1030+0+0")
                self.root.title("CUSTOM HAND GESTURE RECOGNITION")

                img3=Image.open(r"E:\Final_Year_Project\Custom_Hand_Gesture_Recognition\images\WALLPAPER123.png")
                img3=img3.resize((1920,1080))
                self.photoimg3=ImageTk.PhotoImage(img3)

                bg_img=Label(self.root,image=self.photoimg3)
                bg_img.place(x=0,y=0,width=1920,height=1080)

#5 RECOGNITION btn

                img9=Image.open(r"E:\Final_Year_Project\Custom_Hand_Gesture_Recognition\images\CUSTOM HAND GESTURE RECOGNITION.png")
                img9=img9.resize((220,220))
                self.photoimg9=ImageTk.PhotoImage(img9)

                b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.handgesture_data)
                b1.place(x=300,y=400,width=350,height=150)

                b1=Button(bg_img,text="HAND RECOGNITION",cursor="hand2",command=self.handgesture_data,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
                b1.place(x=300,y=550,width=350,height=40)

#4fingre_btn

                img4fin=Image.open(r"E:\Final_Year_Project\Custom_Hand_Gesture_Recognition\images\CUSTOM HAND GESTURE RECOGNITION.png")
                img4fin=img4fin.resize((220,220))
                self.photoimg4fin=ImageTk.PhotoImage(img4fin)

                b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.fourfingerGesture)
                b1.place(x=800,y=400,width=350,height=150)

                b1=Button(bg_img,text="FOUR FINGER RECOGNITION",cursor="hand2",command=self.fourfingerGesture,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
                b1.place(x=800,y=550,width=350,height=40)

#3 fingre_btn

                img3fin=Image.open(r"E:\Final_Year_Project\Custom_Hand_Gesture_Recognition\images\CUSTOM HAND GESTURE RECOGNITION.png")
                img3fin=img3fin.resize((220,220))
                self.photoimg4fin=ImageTk.PhotoImage(img3fin)

                b1=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.threefingerGesture)
                b1.place(x=1300,y=400,width=350,height=150)

                b1=Button(bg_img,text="THREE FINGER RECOGNITION",cursor="hand2",command=self.threefingerGesture,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
                b1.place(x=1300,y=550,width=350,height=40)

#developers btn
                img10=Image.open(r"E:\Final_Year_Project\Custom_Hand_Gesture_Recognition\images\dev.jpg")
                img10=img10.resize((220,220))
                self.photoimg10=ImageTk.PhotoImage(img10)

                b1=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.developer_data)
                b1.place(x=300,y=700,width=350,height=150)

                b1=Button(bg_img,text="DEVELOPERS",cursor="hand2",command=self.developer_data,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
                b1.place(x=300,y=850,width=350,height=40)

#help
                img7=Image.open(r"E:\Final_Year_Project\Custom_Hand_Gesture_Recognition\images\hlp.jpg")
                img7=img7.resize((220,220))
                self.photoimg7=ImageTk.PhotoImage(img7)

                b1=Button(bg_img,image=self.photoimg7,cursor="hand2",command=self.help_data)
                b1.place(x=800,y=700,width=350,height=150)

                b1=Button(bg_img,text="HELP",cursor="hand2",command=self.help_data,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
                b1.place(x=800,y=850,width=350,height=40)

#exit btn

                img11=Image.open(r"E:\Final_Year_Project\Custom_Hand_Gesture_Recognition\images\exi.jpg")
                img11=img11.resize((220,220))
                self.photoimg11=ImageTk.PhotoImage(img11)

                b1=Button(bg_img,image=self.photoimg11,cursor="hand2",command=self.iExit)
                b1.place(x=1300,y=700,width=350,height=150)

                b1=Button(bg_img,text="EXIT",cursor="hand2",command=self.iExit,font=("Amasis MT Pro Black",15,),fg="#fff",bg="#007ACC",activeforeground="white",activebackground="#007ACC")
                b1.place(x=1300,y=850,width=350,height=40)


        def open_img(self):
                os.startfile("data")

        def iExit(self):
                self.iExit=tkinter.messagebox.askyesno("Custom Hand Gesture","Do you really want to exit this project ?",parent=self.root)
                if self.iExit >0:
                        self.root.destroy()
                else:
                        return


        def developer_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Developer(self.new_window)

        def handgesture_data(self):
                run_hand_gestures()

        def fourfingerGesture(self):
                run_hand_gestures_4fing()
        
        def threefingerGesture(self):
                run_hand_gestures_3fing()

        def help_data(self):
                self.new_window=Toplevel(self.root)
                self.app=Help(self.new_window)
        

if __name__ == "__main__":
        root=Tk()
        obj=Custom_Hand_Gesture(root)
        root.mainloop()