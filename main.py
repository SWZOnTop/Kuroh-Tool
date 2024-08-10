import requests
import os
import msvcrt
from urllib.parse import quote
import json


# Définition des couleurs (simplement pour afficher en noir et blanc si les couleurs ne fonctionnent pas)
PURPLE = "\033[95m"  # Violet
GREEN = "\033[92m"  # Vert
RESET = "\033[0m"  # Réinitialisation des couleurs

def show_banner():
    banner = f"""
{PURPLE}
.-. .-')              _  .-')                ('-. .-.       .-') _                                        
\  ( OO )            ( \( -O )              ( OO )  /      (  OO) )                                       
,--. ,--. ,--. ,--.   ,------.  .-'),-----. ,--. ,--.      /     '._  .-'),-----.  .-'),-----.  ,--.      
|  .'   / |  | |  |   |   /`. '( OO'  .-.  '|  | |  |      |'--...__)( OO'  .-.  '( OO'  .-.  ' |  |.-')  
|      /, |  | | .-') |  /  | |/   |  | |  ||   .|  |      '--.  .--'/   |  | |  |/   |  | |  | |  | OO ) 
|     ' _)|  |_|( OO )|  |_.' |\_) |  |\|  ||       |         |  |   \_) |  |\|  |\_) |  |\|  | |  |`-' | 
|  .   \  |  | | `-' /|  .  '.'  \ |  | |  ||  .-.  |         |  |     \ |  | |  |  \ |  | |  |(|  '---.' 
|  |\   \('  '-'(_.-' |  |\  \    `'  '-'  '|  | |  |         |  |      `'  '-'  '   `'  '-'  ' |      |  
`--' '--'  `-----'    `--' '--'     `-----' `--' `--'         `--'        `-----'      `-----'  `------'  
{RESET}
    """
    print(banner)

def show_categories():
    categories = f"""
{GREEN}
╔════════════════════════════════════════════════════════════════════════════════╗
║ {PURPLE}01. Spam Webhook            {GREEN}02. Delete Webhook             {PURPLE}03. Ping Webhook                 {GREEN}║
╠════════════════════════════════════════════════════════════════════════════════╣
║ {PURPLE}04. Send Image              {GREEN}05. Ban                        {PURPLE}06. Give Rôle                    {GREEN}║
╠════════════════════════════════════════════════════════════════════════════════╣
║ {PURPLE}07. Recherche Username      {GREEN}08. Recherche Nom/Prénom       {PURPLE}09. Recherche Tel N°             {GREEN}║
╠════════════════════════════════════════════════════════════════════════════════╣
║ {PURPLE}10. Lookup IP               {GREEN}11. DDoS IP                    {PURPLE}Q. Sortir du Tool                {GREEN}║
╚════════════════════════════════════════════════════════════════════════════════╝
{RESET}
    """
    print(categories)

def check_ctrl_r():
    """Vérifie si CTRL + R est pressé."""
    if msvcrt.kbhit():
        key = msvcrt.getch()
        if key == b'\x12':  # code pour CTRL + R
            return True
    return False

def wait_for_user_input():
    """Attend que l'utilisateur appuie sur une touche pour revenir au menu principal."""
    input("Appuyez sur Enter pour revenir au menu principal...")

def spam_webhook():
    url = input("Entrez l'URL du Webhook : ")
    message = input("Entrez le message à envoyer : ")
    num_times = int(input("Combien de fois voulez-vous spammer ? "))

    for i in range(num_times):
        if check_ctrl_r():
            return
        response = requests.post(url, json={"content": message})
        if response.status_code == 204:
            print(f"Message envoyé {i + 1}/{num_times}")
        else:
            print(f"Erreur lors de l'envoi du message {i + 1}/{num_times}: {response.status_code}")

    wait_for_user_input()

def delete_webhook():
    url = input("Entrez l'URL du Webhook à supprimer : ")

    response = requests.delete(url)
    if response.status_code == 204:
        print("Webhook supprimé avec succès")
    else:
        print(f"Erreur lors de la suppression du webhook: {response.status_code}")

    wait_for_user_input()

def ping_webhook():
    url = input("Entrez l'URL du Webhook : ")
    user_id = input("Entrez l'ID de l'utilisateur à ping : ")
    message = input("Entrez le message à envoyer (facultatif) : ")
    num_times = int(input("Combien de fois voulez-vous spammer ? "))

    content = f"<@{user_id}> {message}"

    for i in range(num_times):
        if check_ctrl_r():
            return
        response = requests.post(url, json={"content": content})
        if response.status_code == 204:
            print(f"Ping envoyé {i + 1}/{num_times}")
        else:
            print(f"Erreur lors de l'envoi du ping {i + 1}/{num_times}: {response.status_code}")

    wait_for_user_input()

def send_image():
    url = input("Entrez l'URL du Webhook : ")
    image_url = input("Entrez l'URL de l'image : ")
    message = input("Entrez un message (facultatif) : ")

    data = {
        "content": message,
        "embeds": [{"image": {"url": image_url}}]
    }

    response = requests.post(url, json=data)
    if response.status_code == 204:
        print("Image envoyée avec succès")
    else:
        print(f"Erreur lors de l'envoi de l'image: {response.status_code}")

    wait_for_user_input()

def ban_member():
    url = input("Entrez l'URL du Webhook : ")
    user_id = input("Entrez l'ID de l'utilisateur à bannir : ")
    reason = input("Entrez la raison du bannissement : ")

    data = {
        "content": f"Bannissement de <@{user_id}> pour la raison suivante : {reason}"
    }

    response = requests.post(url, json=data)
    if response.status_code == 204:
        print(f"Utilisateur <@{user_id}> banni avec succès")
    else:
        print(f"Erreur lors du bannissement: {response.status_code}")

    wait_for_user_input()

def give_role():
    url = input("Entrez l'URL du Webhook : ")
    user_id = input("Entrez l'ID de l'utilisateur : ")
    role_id = input("Entrez l'ID du rôle : ")

    data = {
        "content": f"Rôle <@&{role_id}> attribué à <@{user_id}>"
    }

    response = requests.post(url, json=data)
    if response.status_code == 204:
        print(f"Rôle attribué à l'utilisateur <@{user_id}>")
    else:
        print(f"Erreur lors de l'attribution du rôle: {response.status_code}")

    wait_for_user_input()

def search_on_social_media(query):
    platforms = {
        "Facebook": f"https://www.facebook.com/search/top/?q={quote(query)}",
        "Twitter": f"https://twitter.com/search?q={quote(query)}",
        "Instagram": f"https://www.instagram.com/explore/tags/{quote(query)}/",
        "LinkedIn": f"https://www.linkedin.com/search/results/all/?keywords={quote(query)}",
        "TikTok": f"https://www.tiktok.com/search?q={quote(query)}",
        "Reddit": f"https://www.reddit.com/search/?q={quote(query)}",
        "Pinterest": f"https://www.pinterest.com/search/pins/?q={quote(query)}",
        "YouTube": f"https://www.youtube.com/results?search_query={quote(query)}"
    }
    
    print("\nRésultats de recherche :")
    for platform, link in platforms.items():
        print(f"{platform}: {link}")
    print()

def search_username():
    username = input("Entrez le nom d'utilisateur à rechercher : ")
    search_on_social_media(username)
    wait_for_user_input()

def search_name_surname():
    name = input("Entrez le prénom : ")
    surname = input("Entrez le nom de famille : ")
    query = f"{name} {surname}"
    search_on_social_media(query)
    wait_for_user_input()

def search_phone_number():
    phone_number = input("Entrez le numéro de téléphone à rechercher : ")
    search_on_social_media(phone_number)
    wait_for_user_input()

def lookup_ip():
    ip_address = input("Entrez l'adresse IP à rechercher : ")
    api_url = f"https://ipinfo.io/{ip_address}/json"  # Utilisez ipinfo.io ou un autre service d'API d'IP

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()

        print("\nInformations sur l'adresse IP :")
        print(f"IP: {data.get('ip', 'Non disponible')}")
        print(f"Ville: {data.get('city', 'Non disponible')}")
        print(f"Région: {data.get('region', 'Non disponible')}")
        print(f"Pays: {data.get('country', 'Non disponible')}")
        print(f"Organisation: {data.get('org', 'Non disponible')}")
    except requests.RequestException as e:
        print(f"Erreur lors de la récupération des informations IP : {e}")

    wait_for_user_input()
def send_request_to_ip():
    ip_address = input("Entrez l'adresse IP : ")
    request_type = input("Entrez le type de requête (GET, POST, PUT, DELETE) : ").upper()
    url = f"http://{ip_address}"

    if request_type not in ["GET", "POST", "PUT", "DELETE"]:
        print("Type de requête invalide.")
        return

    data = None
    if request_type in ["POST", "PUT"]:
        data = input("Entrez les données à envoyer (en JSON) : ")
        try:
            data = json.loads(data)
        except json.JSONDecodeError:
            print("Erreur dans le format des données JSON.")
            return

    try:
        if request_type == "GET":
            response = requests.get(url)
        elif request_type == "POST":
            response = requests.post(url, json=data)
        elif request_type == "PUT":
            response = requests.put(url, json=data)
        elif request_type == "DELETE":
            response = requests.delete(url)
        
        print(f"\nRéponse HTTP {response.status_code}: {response.reason}")
        print("Contenu de la réponse:")
        print(response.text)

    except requests.RequestException as e:
        print(f"Erreur lors de la requête : {e}")

    wait_for_user_input()

def main():
    os.system("title SWZ Tool")  # Nom de la fenêtre CMD

def main():
    os.system("title Kuroh Tool")  # Nom de la fenêtre CMD

    while True:
        show_banner()
        show_categories()

     # Récupération du nom de l'ordinateur
        pc_name = os.getenv("COMPUTERNAME")

        # Personnalisation du prompt
        choice = input(f"kuroh-tool@python ⇒ {pc_name} : ").upper()

        if choice == '1':
            spam_webhook()
        elif choice == '2':
            delete_webhook()
        elif choice == '3':
            ping_webhook()
        elif choice == '4':
            send_image()
        elif choice == '5':
            ban_member()
        elif choice == '6':
            give_role()
        elif choice == '7':
            search_username()
        elif choice == '8':
            search_name_surname()
        elif choice == '9':
            search_phone_number()
        elif choice == '10':
            lookup_ip()
        elif choice == '11':
            send_request_to_ip()
        elif choice == 'Q':
            print("A une pochaine fois !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

if __name__ == "__main__":
    main()