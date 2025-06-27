def parce_input(user_input:str) -> tuple:
    cmd, *args = user_input.split(' ')
    cmd = cmd.strip().casefold()
    return cmd, *args


def add_contact(args:list, contacts:dict) -> str:
    
    name, phone = args

    if contacts.get(name) != None:
        return f'Sorry, this name is already taken. Please, enter another name.'
    contacts[name] = phone
    return f'Contact {name} added!'


def show_all(contacts:dict):
    for name, phone in contacts.items():
        print(f'{name}: {phone}')


def show_phone(name:str, contacts:dict):
    if contacts.get(name) != None:
        return contacts.get(name)
    else:
        return f'There`s no contact {name}. Please, enter another name.'


def change_contact(name:str, phone:str, contacts:dict):
    if name != '' and contacts.get(name) != None:
        contacts[name] = phone
        return f'Contact updated: {name} {phone}'
    else:
        return f'There`s no contact {name}. Please, enter another name.'
        

def greeting():
    return "Hi! How can I help you?"
