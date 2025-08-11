#Insere um contato no dict contacts.json
import json


def insert_contact(name:str, number:str):
    with open("contacts.json", 'r', encoding='utf-8') as contacts:
        contacts = json.load(contacts)

    contact = {
        "id": len(contacts)+1,
        "name": name,
        "number": number
    }

    contacts.append(contact)

    with open("contacts.json", 'w', encoding='utf-8') as new_contacts:
        json.dump(contacts, new_contacts, indent=4, ensure_ascii=False)

    return print('Contato criado com sucesso!')