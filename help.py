from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import cv2
import webbrowser


class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Help")

# This part is image labels setting start 

        # backgorund image 
        bg1=Image.open(r"D:\face_Recognition_system\images\forhelp.jpg")
        bg1=bg1.resize((1920,1080))
        self.photobg1=ImageTk.PhotoImage(bg1)

        # set image as lable
        bg_img = Label(self.root,image=self.photobg1)
        bg_img.place(x=0,y=0,width=1920,height=1080)

        # ------------------------------------------------------------------------------------------------------------------- 

        # student button 1

        std_img_btn=Image.open(r"D:\face_Recognition_system\images\weblogo.jpg")
        std_img_btn=std_img_btn.resize((180,180))
        self.std_img1=ImageTk.PhotoImage(std_img_btn)

        std_b1 = Button(bg_img,command=self.website,image=self.std_img1,cursor="hand2")
        std_b1.place(x=1190,y=400,width=180,height=180)

        # Detect Face  button 2
        det_img_btn=Image.open(r"D:\face_Recognition_system\images\fblogo.png")
        det_img_btn=det_img_btn.resize((180,180))
        self.det_img1=ImageTk.PhotoImage(det_img_btn)

        det_b1 = Button(bg_img,command=self.facebook,image=self.det_img1,cursor="hand2",)
        det_b1.place(x=500,y=400,width=180,height=180)


        # Attendance System  button 3
        att_img_btn=Image.open(r"D:\face_Recognition_system\images\youtubelogo.jpg")
        att_img_btn=att_img_btn.resize((180,180))
        self.att_img1=ImageTk.PhotoImage(att_img_btn)

        att_b1 = Button(bg_img,command=self.youtube,image=self.att_img1,cursor="hand2",)
        att_b1.place(x=730,y=400,width=180,height=180)

        # Help  Support  button 4
        hlp_img_btn=Image.open(r"D:\face_Recognition_system\images\outlooklogo.jpg")
        hlp_img_btn=hlp_img_btn.resize((180,180))
        self.hlp_img1=ImageTk.PhotoImage(hlp_img_btn)

        hlp_b1 = Button(bg_img,command=self.Mail,image=self.hlp_img1,cursor="hand2",)
        hlp_b1.place(x=960,y=400,width=180,height=180)




        # create function for button 
    
    
    def website(self):
        self.new = 1
        self.url = "https://techvidvan.com/tutorials/hand-gesture-recognition-tensorflow-opencv/"
        webbrowser.open(self.url,new=self.new)
    
    def facebook(self):
        self.new = 1
        self.url = "https://www.facebook.com/"
        webbrowser.open(self.url,new=self.new)
    
    def youtube(self):
        self.new = 1
        self.url = "https://www.youtube.com/@n1kesjk"
        webbrowser.open(self.url,new=self.new)
    
    def Mail(self):
        self.new = 1
        webbrowser.open("mailto:?to=nrougejk12@gmail.com&subject=Need help about: ", new=1)





if __name__ == "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()