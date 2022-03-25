import os
from pprint import pprint

def files_read(file_name: str, mode: str, encoding: str):
    with open(file_name, mode, encoding=encoding) as file:
        data = file.readlines()
    return data

def count_str(data: list):
    count = len(data)
    return count

def add_dict(key: str, value: int, data_dict: dict):
    data_dict[key] = value
    return data_dict

def file_write(file_name: str, mode: str, encoding: str, data: str):
    with open(file_name, mode, encoding=encoding) as file:
        file.write(data)
    return data

if __name__ == '__main__':
    test = {}
    FILE_DIR = 'sorted'
    BASE_PATH = os.getcwd()
    dir_path = os.path.join(BASE_PATH, FILE_DIR)
    print(BASE_PATH)
    file_list = os.listdir(dir_path)

    for name_files in file_list:
        # print(name_files)
        dir_path_file = os.path.join(dir_path, name_files)
        add_dict(name_files, count_str(files_read(dir_path_file, 'rt', 'UTF-8')), test)
    a = True
    # pprint(test)
    while a == True:
        if test:
            min_value = min(test.values())
            for key, value in test.items():
                if value == min_value:
                    result = key
            # print(result)
            file_write('itog.txt', 'a', 'UTF-8', f'{result}\n')
            file_write('itog.txt', 'a', 'UTF-8', f'{test[result]}\n')
            dir_path_file = os.path.join(dir_path, result)
            t_list = files_read(dir_path_file, 'rt', 'UTF-8')
            for str_ in t_list:
                file_write('itog.txt', 'a', 'UTF-8', str_)
            file_write('itog.txt', 'a', 'UTF-8', '\n')
            test.pop(result)
        else:
            a = False