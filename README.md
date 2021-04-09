# Send_file-MAIL-with-Python
## Envoyer un fichier venant d'un serveur avec python.

Mais soyez patient 😄, tout d'abord nous allons installer **les dépendances nécessaires** si votre python vient juste d'installer :
</br>**pip3 install smtplib** 
</br>**pip3 install ssl**
</br>**pip3 install email**
</br> Dans notre code *send_file_log_mail_save.py*, il y a ceci : <img src="img/mdp.png" width="700px" height="80px">
</br> Il faut que votre ***mot de passe*** soit enregistrer dans votre système c'est-à-dire dans *déclarer comme une variable système* si non je peux connecter avec votre email 😅 en utilisant le mot de passe que vous écrivez ici. Pour le faire , il suffit juste de faire comme ceci sur votre terminal: 
</br>**mdp="votre mot de passe"** et après **export mdp** pour vérifier que votre variable est enregistrée comme variable système tapez 👉 **env**

Donc voilà 😄, comme vous voyez ce petit scrypte a comme fonction de 🖇️***récuperer le fichier*** de votre choix et de ***l'envoyer à un destinataire par email.***
Et pour le lancer automatiquement, je vous conseille d'utiliser **crontab** 👍 ➡️ 

### Voici donc une petite explication pour vous aider
</br> <img src="img/crontab.png" width="600px" height="300px">

</br> Comme vous pouvez voir en-dessus l'explication, voici un exemple pour lancer notre scrypte :
</br> Nous allons faire executé notre scrypte qui permet d'envoyer le ***fichier log de notre serveur par email***  tous  ***le premier mardi du mois à 14h00***
</br> <img src="img/capture_1.png" width="600px" height="300px">
