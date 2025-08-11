#Modifica um contato no dict .json
import json


def change_contact(contact_info:str, new_name:str, new_number:str):
    with open("contacts.json", 'r', encoding='utf-8') as contacts:
        contacts = json.load(contacts)
        for contact in contacts:
            if contact['name'] == contact_info or contact['number'] == contact_info:
                contact['name']=new_name
                contact['number']=new_number

    with open("contacts.json", 'w', encoding='utf-8') as new_contacts:
        json.dump(contacts, new_contacts, indent=4, ensure_ascii=False)

    return print('Contato alterado com sucesso!')
