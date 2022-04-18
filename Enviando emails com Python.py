from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha

email = 'evandro.ferraz.07@gmail.com'
senha = '****'

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

with open('template.html','r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Evandro Ferraz', data = data_atual)
    
msg = MIMEMultipart()
msg['from'] = 'Evandro Catelani Ferraz'
msg['to'] = meu_email
msg['subject'] = 'Atenção: este é um email de testes.'
    
corpo = MIMEText(corpo_msg, 'html')
msg.attach(corpo)

with smtplib.SMTP(host='smtp.gmail.com', port = 587) as smtp: #587 é a porta do gmail, outros provedores terão portas diferentes.
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email, minha_senha)
    smtp.send_message(msg)


