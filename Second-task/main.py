from pathlib import Path


def get_cats_info(path:Path) -> list[dict]:
    '''
    Fuction return list of dictionaries, where each dictionary has information about one cat.  
    '''
    cats_list = [] # List for prepared data
    
    # Reading and fill list 'cats_list' data from file 
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            raw_data = file.readlines()
            for el in raw_data:
                cat_id, cat_name, cat_age = el.split(',')
                cats_list.append({
                    'id': cat_id,
                    'name': cat_name,
                    'age': int(cat_age)
                })
            return cats_list
        
    except FileNotFoundError:
        return 'File not found'
    except OSError:
        return 'File is corrupted'



# Script that use function total_salary(path)
file_name = 'cats.txt'
directory = Path(__file__).parent

cats_info = get_cats_info(directory / file_name)

if type(cats_info) == list:
    for cat in cats_info:
        print(cat)
if type(cats_info) == str:
    print(f'[Error]: {cats_info}')


