import smtplib
from email.message import EmailMessage
import glob

msg=EmailMessage()


#Enter Subject of Mail below
msg['Subject']='Attachment not found in System'


#Enter who is sending this mail
msg['From']='Document Processing Team'

#Enter Mail Address to whom you want to send mail
msg['To']='i.devchaudhary17@gmail.com','d1782000@gmail.com'


#Text Content yoou want in your message
#We use file 'EmailContent' everytime we can update that file
#make sure 'EmailContent' is at same location as of our python file
with open('EmailContent.txt') as message:
    data=messag.read()
    msg.set_content(data)

    
#Attcahment we want in our Email
#File to be attach must be at same location as of our python file
for files in glob.glob('*.xlsx'):
    f=open(files,'rb')
    file.data=f.read()
    file_name=f.name()
    msg.add_attachment(file_data,maintype='application',subtype='xlsx',filename=file_name)

#setting up server to send mail

server=smtplib.SMTP.SSL('smtp.gmail.com',465)
server.login('trysingh94@gmail.com','xxxxxx@xxxxx')
server.send_message(msg)

server.end()
print('Email Send')
