#Cria uma nova instância de Contact a partir de um contato no dict contacts.json
import json

from agenda_2.contacts.contacts import Contact


def rescue_contact(contact_info:str) -> Contact:
    with open("contacts.json", 'r', encoding='utf-8') as contacts:
        contacts = json.load(contacts)
        for contact in contacts:
            if contact['name'] == contact_info or contact['number'] == contact_info:
                return Contact(contact['name'], contact['number'])

c=rescue_contact('991234567')