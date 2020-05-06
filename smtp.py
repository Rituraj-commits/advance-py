import smtplib as smtp
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

server='smtp.gmail.com'
port=587

email='pythonac69@gmail.com'
password='python69py'

_from='pythonac69@gmail.com'
_to='pythonac69@gmail.com'


connection=smtp.SMTP(server,port)
connection.ehlo() 
connection.starttls()
connection.login(email,password)
tmessage=MIMEMultipart()
tmessage['Subject']='HTML Message'
tmessage['From']=email
tmessage['To']=email


html_message='''<html><body><h1>HTML</h1><p><i>This is an HTML tag</i></p></body></html>'''
plain_message='There is no html tag'

msg1=MIMEText(html_message,'html')
msg2=MIMEText(plain_message,'plain')
tmessage.attach(msg1) 
tmessage.attach(msg2)

try:    
	connection.sendmail(_from,_to,tmessage.as_string())
	print("Mail Sent!!")
	
except:
	print("Oops!! Somethong went wrong")
	
finally:
	connection.quit()
									
