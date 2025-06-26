from pathlib import Path


def get_cats_info(path:Path) -> list[dict]:
    '''
    Fuction return list of dictionaries, where each dictionary has information about one cat.  
    '''
    cats_list = [] # List for prepared data
    
    try:
        # Reading and fill list 'cats_list' data from file 
        with open(path, 'r', encoding='UTF-8') as file:
            raw_data = file.readlines()

        # Data processing and tuple  return
        if raw_data:
            for el in raw_data:
                        if not el.strip():
                            continue
                        el = el.strip()
                        cat = el.split(',')
                        if len(cat) == 3:
                            try:
                                cats_list.append({'id': cat[0], 'name': cat[1], 'age': int(cat[2])})
                            except ValueError:
                                cats_list.append('YOU HAVE TROBLE WITH AGE OF THIS CAT')

                        else:
                            cats_list.append('Something wrong with this cat...')

    except FileNotFoundError:
        return 'File not found'
    except OSError:
        return 'File is corrupted'
    
    return cats_list
        
        

if __name__ == "__main__":
    # Script that use function total_salary(path)
    file_name = 'cats.txt'
    directory = Path(__file__).parent

    cats_info = get_cats_info(directory / file_name)

    if type(cats_info) == list:
        for cat in cats_info:
            print(cat)
    if type(cats_info) == str:
        print(f'[Error]: {cats_info}')


