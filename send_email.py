import smtplib
import sys

import os

#settings
smtp_server = os.environ['notif_smtp_server'] if 'notif_smtp_server' in os.environ else 'smtp.gmail.com'
smtp_port = int(os.environ['notif_smtp_port']) if 'notif_smtp_port' in os.environ else 587

user_email = os.environ['notif_user_email'] if "notif_user_email" in os.environ else None   # soemthing@gmail.com
user_pass = os.environ['notif_user_pass'] if "notif_user_pass" in os.environ else None  # somepass

if user_email is None:
  print("Please, set user e-mail!")
  print("export notif_user_email=your.email@server.com")

if user_pass is None:
  print("Please, set user pas environment variable!")
  print("export notif_user_pass=yourpasssthatnooneknow")

print("%s : %s" % ("smtp_server",smtp_server))
print("%s : %s" % ("smtp_port", smtp_port))
print("%s : %s" % ("user_email", user_email))
print("%s : %s" % ("user_pass", "***"))

print("%s : %s" % ("address to send from", user_email))

# mail message
if len(sys.argv) < 4:
  print("No enough input params are found!")
  print("Use:")
  print("")
  print("python send_email recepiend@address.com \"your subject here\" \"Your message here\"")
  print("")
  exit()

recipient_e_mail = sys.argv[1]
subject = sys.argv[2]
msg = sys.argv[3]

print("%s : %s" % ("recipient_e_mail", recipient_e_mail))
print("%s : %s" % ("subject", subject))
print("%s : %s" % ("msg", msg))

print("Logging in..")
server = smtplib.SMTP(smtp_server, smtp_port)
if smtp_server == 'smtp.gmail.com':
  server.ehlo()
server.starttls()
server.login(user_email, user_pass)
print("Done")

print("Sending..")
full_msg = "\r\n".join([
  "From: %s" % user_email,
  "To: %s" % recipient_e_mail,
  "Subject: %s" % subject,
  "",
  msg
  ])

server.sendmail(user_email, recipient_e_mail, full_msg)
server.quit()
print("Done!")
