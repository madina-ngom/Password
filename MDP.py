import re

while True:
    
    flag = 0
    password = input ("Choissisez votre mot de passe:")

    if not re.search('[a-z]', password):
        flag = 1
        print("Le mot de passs est trop court.")
    
    if not re.search('[0-9]', password):
        flag = 1
        print("Le mot de passe n'a pas de chiffres.")

    if not re.search('[A-Z]', password):
        flag = 1
        print("Le mot de passe n'a pas de majuscules.")

    if not re.search('[@#$!]', password):
        flag = 1
        print("Le mot de passe n'a pas de caractères spéciaux.")
    
    if flag == 0:
        if (len(password) > 8):
            print("Mot de passe accepter.")
            break
        else:
            print("Votre mot de passe est trop court.")