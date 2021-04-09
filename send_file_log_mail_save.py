import email, smtplib, ssl, base64, os
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

subject = "SENDING LOG_FILE BY SERVER"
body = '''\

Chers collègues,

Ci-joint le fichier log de notre serveur pour le suivi de son fonctionnement.

Cordialement.

'''
sender_mail = "aina.juno.rafidison@esti.mg"
password = os.environ["mdp"]

#creer un message en plusieurs et definir des en-tetes
message = MIMEMultipart()
message['From'] = sender_mail
message['To'] =  "aina.apsa18@gmail.com" #le mail destinataire
message['Subject'] = subject

#ajouter du corps a l' e-mail
message.attach(MIMEText(body, "plain"))

filename = "test.txt"
#filename = "/var/log/nginx/access.log" #Le fichier qu'on va envoyer

#ouvrir le fichier pdf en binaire
with open(filename, "rb") as attachement:
    #ajouter un fichier comme  application/octet-stream
    #le client de messagerie peut generalement le telecharger automatiquement en tant que piece jointe
    part = MIMEBase("application", "octet-stream")
    part.set_payload(attachement.read())
#encoder le fichier en caracteres ASCII a envoyer par email
encoders.encode_base64(part)

#ajouter un en-tete comme paire key/value a la piece jointe
part.add_header(
    "Content-Disposition", f"attachement; filename={filename}"
)

#ajouter une piece jointe au message et convertir le message en chaine
message.attach(part)
text = message.as_string()

#connectez-vous au serveur en utilisant un context securise et envoyer un e-mail
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_mail, password)
    server.sendmail(sender_mail, message['To'].split(","), text)
    server.quit()
