import smtplib
from tkinter import*
def sentmassege():
 address_info=address.get()
email_body_info=email_body.get()
print(address_info,email_body_info)
sender_email="ENTERYOUREMAILHER"
sender_password="ENTERYOURPASSWORDHERE"
server=smptplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(sender_email,sender_password)
print("login successful")
server.sendmail(sender_email,address_info,email_body_info)
print("message sent")
address_entry.delete(0,END)
email_body_entry.delete(0,END)
app=Tk()
app.geometry("500*500")
app.title("python mail send App")
heading=Label(text="python mail sending App",bg="yellow",fg="black",font="10",width="500",height="3")
handling.pack()
address_field=Label(text="Reciepnt Address: ")
email_body_field=Label(text="message: ")
address_field.place(x=15,y=70)
email_body.place(x=15,y=140)
address=stringVar()
email_body=stringVar()
address_entry=Entry(textvariable=address,width="30")
email_body_entry=Entry(textvariable=email_body,width="30")
address_entry.place(x=15,y=100)
email_body_entry.place(x=15,y=180)
Button=Button(app,text="send message",Command=sentmessage,width="30",height="2",bg="grey")
button.place(x=15,y=220)
mainloop()




