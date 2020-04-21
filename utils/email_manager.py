# Developed by Miguel Angel Perdigon Orta
# Email: miguelperdigon91@gmail.com
# 17/09/2018

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import smtplib
from logging import error
from unidecode import unidecode


def send(recipients, cc, subject, body, files,):
    try:
        email_user = 'example@server.org'
        email_password = '********'
        sent_from = 'Sent by my Company'
        to = recipients

        msg = MIMEMultipart()

        msg['From'] = email_user
        msg['To'] = ", ".join(recipients)
        msg['CC'] = ", ".join(cc)
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))

        for file_name in files:
            attachment = files[file_name]

            if type(attachment) is str:
                file_name = unidecode(attachment)
                attachment = open(file_name, "rb")
                attachment = attachment.read()
            else:
                attachment = attachment.getvalue()

            p = MIMEBase('application', 'octet-stream')
            p.set_payload(attachment)
            encoders.encode_base64(p)

            p.add_header('Content-Disposition', "attachment; filename= %s" % file_name)
            msg.attach(p)

        # smtp.gmail.com if you will use gmail
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(email_user, email_password)
        server.sendmail(sent_from, to, msg.as_string())
        server.close()

        return True

    except Exception as e:
        error(str(e))
        return False
