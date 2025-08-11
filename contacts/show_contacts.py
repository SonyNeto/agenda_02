#Imprime uma lista com os contatos (nome e número) do dict .json
import json


def show_contacts():
        with open("contacts.json", 'r', encoding='utf-8') as contacts:
            contacts = json.load(contacts)
            contact_list=[]
            for contact in contacts:
                contact_list.append([contact['name'].title(), contact['number']])
                contact_list.sort()
            for contact in contact_list:
                print(f"{contact[0]} : {contact[1]}")

show_contacts()