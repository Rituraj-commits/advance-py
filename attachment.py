import smtplib as smtp
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders


server='smtp.gmail.com'
port=587

email='pythonac69@gmail.com'
password='python69py'

_from='pythonac69@gmail.com'
_to='pythonac69@gmail.com'
_subject='Attachment'


tmessage=MIMEMultipart()
tmessage['Subject']=_subject
tmessage['From']=_from
tmessage['To']=_to


fileName='hello.txt'
openFile=open(fileName,'rb')

mimref=MIMEBase('application','octect_stream')
mimref.set_payload((openFile.read()))
encoders.encode_base64(mimref)
mimref.add_header('Content-disposition','openfile;filename='+fileName)
tmessage.attach(mimref)


connection=smtp.SMTP(server,port)
connection.ehlo() 
connection.starttls()
connection.login(email,password)
connection.sendmail(_from,_to,tmessage.as_string())
connection.quit()

