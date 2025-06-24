from pathlib import Path


def total_salary(path:Path) -> tuple:
    '''
    Fuction return tuple that include total and average salary 
    '''

    salary_list = [] # List for prepared data
    
    # Reading and preparation data from file 
    try:
        with open(path, 'r', encoding='UTF-8') as file:
            raw_data = file.readlines()
            for el in raw_data:
                _, salary = el.split(',')
                salary_list.append(int(salary))
    except FileNotFoundError:
        return 'File not found'
    except OSError:
        return 'File is corrupted'


    # Data processing and tuple  return 
    if len(salary_list) != 0:
        total_result = sum(salary_list)
        average_result = total_result / len(salary_list)
        return total_result, average_result


# Script that use function total_salary(path)
file_name = 'some_data.txt'
directory = Path(__file__).parent

data_tuple = total_salary( directory / file_name )

if type(data_tuple) == tuple:
    print(f'Total salary: {data_tuple[0]:.2f}\nAverage salary: {data_tuple[1]:.2f}')
if type(data_tuple) == str:
    print(f'[ERROR]: {data_tuple}')
