# Email-spammer ⚠️
This a simple email spammer using smtplib module on python **(educational purposes only)** 😺 <br>
```python <b>
import smtplib

toaddrs = 'receivers email'
fromaddrs = 'senders email'
message = 'Your message'
with smtplib.SMTP('smtp.gmail.com', '587') as smtpserver:
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo()
    smtpserver.login(
        'your email', 'add you app token here'
    )  #get your application id from google (more information on readme file)
    for i in range(5):
        smtpserver.sendmail(fromaddrs, toaddrs, message)
        print(i)

```
- [x] Generating your **gmail token** [HELP](https://support.google.com/mail/answer/185833?hl=en)
![Screen Shot 2022-08-22 at 9 38 42 AM](https://user-images.githubusercontent.com/66258991/185838929-f05faf01-44f4-4d38-92c3-188d1b78a71c.png)
