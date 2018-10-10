import smtplib
smtpObj = smtplib.SMTP_SSL('smtp.gmail.com', 465)
smtpObj.ehlo()
print(smtpObj.ehlo())
a=smtpObj.login("ksthameem27@gmail.com","Shinchan")
print(a)
b=smtpObj.sendmail('ksthameem27@gmail.com', 'vishnusrkv@gmail.com',
'Subject: this is python.\nDear Viz, Happy marriage life')
print (b)

