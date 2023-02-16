#!/usr/bin/env python
# coding: utf-8

# In[48]:


from tkinter import *  
import tkinter as tk  
from PIL import ImageTk, Image  


# In[ ]:


# Creation of the new window  
windw = tk.Tk() # creating the required window  
windw.geometry("500x500") # geometry of the window  
windw.title('Image Viewer') # title of the window  
Label(windw, text = "Image Viewer App", font = ('bold', 20)).pack() # label  
   
#creating the required frame  
frames = Frame(windw, width = 230, height = 200, bg = 'white')  
frames.place(relx=0.50,rely=0.5,anchor='center')  
  
# creating the two, next and back buttons  
# The back button, to move to previous image  
Button(windw, text = 'Back', command=Backward,bg= 'light blue').place(relx=0.05,rely=0.5,anchor='w')  
  
# The next button, to move to next image  
Button(windw, text = 'Next', command=Forward,bg = 'light blue').place(relx=0.95,rely=0.5,anchor='e')
  
# opening of the images  
# assigning a variable for each image to be stored  
img1 = ImageTk.PhotoImage(Image.open("C:/Users/Muskan/Downloads/Image Gallery/download (1).jpg"))  
img2 = ImageTk.PhotoImage(Image.open("C:/Users/Muskan/Downloads/Image Gallery/download (2).jpg"))  
img3 = ImageTk.PhotoImage(Image.open("C:/Users/Muskan/Downloads/Image Gallery/download (3).jpg"))  
   
# adding all the images to a list  
imglst = [img1, img2, img3]  
j = 0  
img_label = Label(frames, image = imglst[j])   
  
# packing the images into the window  
img_label.pack()  
  
# defining a forward function to be called when next image is to be displayed  
def Forward():  
    global j # creating a global variable j  
    j = j + 1  
    try:  
        img_label.config(image = imglst[j])  
    except:  
        j = -1  
        Forward() # calling the forward function  
  
# defining a backward function to be called when next image is to be displayed  
def Backward():  
    global j # creating a global variable j  
  
    j = j - 1  
    try:
        img_label.config(image = imglst[j])  
    except:  
        j = 0  
        Backward() # calling the forward function  
  
# Calling the mainloop method to execute our code  
windw.mainloop()  


# In[ ]:




