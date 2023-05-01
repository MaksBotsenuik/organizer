import os
import keys as k

if __name__ == "__main__":
    path = str(input())
    files = os.listdir(path = path)
    print(files)
    for file in files:
        if '.' in file:    
            extention = file.split('.')
            new_path = path+ '\\' + k.file_types_to_names[extention[-1]]
            try:
                os.mkdir(new_path)
            except FileExistsError:
                pass
            os.rename(path + '\\' + file, new_path+'\\'+file)
    files = os.listdir(path = path)
    print(files)