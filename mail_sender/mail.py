from flask_mail import Mail, Message
from conf.config import DEFAULT_MAIL_SENDER

mail = Mail()

def send_email(to, subj, body):
    msg = Message(
        subj,
        recipients=[to],
        html=body,
        sender=DEFAULT_MAIL_SENDER
    )
    mail.send(msg)
