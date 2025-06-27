from functions import interaction_comands as ic

def main():

    contact_dict = {}
    msg = '///   hello   ///   add name phone   ///   change name new_phone   ///   all OR phone name   ///   exit OR close   ///'

    while True:
        user_input = input('Enter command: ')

        cmd = ic.parce_input(user_input)


        match cmd[0].casefold():

            case "hello":
                print(ic.greeting())

            case 'exit' | 'close':
                break

            case 'add' if len(cmd) > 2:
                arg_list = [cmd[1], cmd[2]]
                print(ic.add_contact(arg_list, contact_dict))

            case 'all':
                ic.show_all(contact_dict)

            case 'phone' if not len(cmd) < 2:
                print(ic.show_phone(cmd[1], contact_dict))

            case 'change' if not len(cmd) < 3:
                print(ic.change_contact(cmd[1], cmd[2], contact_dict))
            case 'help':
                print(msg)     
            case _:
                print('Something went wrong. You can view all available commands using the command: help')



if __name__ == "__main__":
    main()
