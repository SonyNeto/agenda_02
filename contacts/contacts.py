from agenda_2.contacts.change_contact import change_contact
from agenda_2.contacts.delete_contact import del_contact
from agenda_2.contacts.insert_contact import insert_contact


class Contact:
    def __init__(self, name:str, number:str):
        self.name = name
        self.number = number
        self.info = name or number

    def save_contact(self):
        insert_contact(self.name, self.number)

    def apply_del(self):
        del_contact(self.info)

    def apply_change(self, new_name=None, new_number=None): #Lembrar de definir a entrada de number com apenas números
        if new_name is not None:
            self.name = new_name
        if new_number is not None:
            self.number = new_number
        change_contact(self.info, self.name, self.number)

#c = Contact('Sebastião', '996533216')
#c.apply_del()
#c.save_contact()
#c.apply_change('991234567')