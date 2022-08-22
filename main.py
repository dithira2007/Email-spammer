import smtplib
toaddrs = 'receivers email'
fromaddrs = 'senders email'
message = 'Your message'
with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
  smtpserver.ehlo()
  smtpserver.starttls()
  smtpserver.ehlo()
  smtpserver.login('your email', 'add you app token here') #get your application id from google (more information on readme file)
  for i in range(5):
    smtpserver.sendmail(fromaddrs, toaddrs, message)
    print(i)