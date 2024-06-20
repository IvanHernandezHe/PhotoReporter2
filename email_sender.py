import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders

def send_email(attachment_path):
    from_addr = 'tu_correo@example.com'
    to_addr = 'destinatario@example.com'
    subject = 'Reporte Fotográfico'
    body = 'Adjunto encontrarás el reporte fotográfico.'

    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    attachment = open(attachment_path, "rb")

    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f"attachment; filename={attachment_path}")

    msg.attach(part)

    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.starttls()
        server.login(from_addr, 'tu_contraseña')
        server.sendmail(from_addr, to_addr, msg.as_string())

    print('Correo enviado con éxito.')
    