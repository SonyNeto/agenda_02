#Exclui um contato no dict .json
import json


def del_contact(contact_info:str):
    with open("contacts.json", 'r', encoding='utf-8') as contacts:
        contacts = json.load(contacts)
        for contact in contacts:
            if contact['name'] == contact_info or contact['number'] == contact_info:
                contacts.remove(contact)

    with open("contacts.json", 'w', encoding='utf-8') as new_contacts:
        json.dump(contacts, new_contacts, indent=4, ensure_ascii=False)

    return print('Contato removido com sucesso!')