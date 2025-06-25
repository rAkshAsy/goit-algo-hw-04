from colorama import Fore, Back, Style
from pathlib import Path
import sys

def dirscript(path:Path, tabulate=0):
    
    formating_string ='|   '*tabulate
    directory_mark = Fore.BLACK+Back.GREEN+Style.BRIGHT+'[DIRECTORY]'+Style.RESET_ALL
    file_mark = Fore.RED+Back.CYAN+Style.BRIGHT+'[FILE]'+Style.RESET_ALL

    element_path = Path(path)
    if element_path.exists():

        for el_path in element_path.iterdir():
            if el_path.is_dir():
                print(f'{formating_string}|>{directory_mark}: {el_path.name}')
                dirscript(el_path,tabulate+1)
            elif el_path.is_file():
                print(f'{formating_string}|>{file_mark}: {el_path.name}')
    else:
        print(Fore.BLACK+Back.CYAN+Style.BRIGHT+'[WARNING] THIS PATH DOES NOT EXIST [WARNING]'+Style.RESET_ALL)


    


if __name__ == '__main__':
    

    try:
        if sys.argv[1]:
            dirscript(sys.argv[1])
    except:
        print(Fore.BLACK+Back.YELLOW+Style.BRIGHT+'[WARNING] Please, enter absolute path. Example: python main.py D:\Video [WARNING]'+Style.RESET_ALL)
        
