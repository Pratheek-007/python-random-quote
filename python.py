#plt.show()
for i in range(len(person)):
plt.imsave("C:\\Users\Sahil\Desktop\Minor\object detection\object detection\image\save\image"+str(i)+".jpg",person[i])
#end of object detection
def vide():
os.startfile("C:\\Users\Sahil\Desktop\Minor\object detection\object detection\image\save")
#GUI part
root=Tk("Project")
bu1=PhotoImage(file="C:/Users/Sahil/Desktop/data/bu.png")
bu2=PhotoImage(file="C:/Users/Sahil/Desktop/data/open.png")
#set width and height
lb=Label(root,text="Helmet Detection",anchor=CENTER,font=('Times New Roman',30))
lb.pack()
#background image code
canvas=Canvas(root,width=800,height=500)
image=ImageTk.PhotoImage(Image.open("C:\\Users\\Sahil\\Desktop\\data\\lo.png"))
canvas.create_image(0,0,anchor=NW,image=image)
canvas.pack()
#button 1
button1 = Button(root, image=bu1, command=object_detection,border=0)
button1.pack(side="left", fill='both', expand=True, padx=4, pady=4)
#button 2 code
button = Button(root, image=bu2, command=vide,border=0)
button.pack(side="right", fill='both', expand=True, padx=4, pady=4)
root.mainloop()
#end of gui
