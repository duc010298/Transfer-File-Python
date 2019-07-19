from colorama import Fore
import os
import math

BUF = 50*1024*1024*1024


def split_file(file, file_size, number_of_part, del_src):
    data = {}
    if file_size != '199' and number_of_part != '0':
        data["status"] = 0
        data["content"] = "Failure - Cannot split file with both file_size and number_of_part"
        return data

    if not os.path.isfile(file):
        current_dir = os.getcwd()
        file = current_dir + '/' + file
        if not os.path.isfile(file):
            data["status"] = 0
            data["content"] = "Failure - File not exist"
            return data

    del_src = del_src.lower()
    if del_src != 'true' and del_src != 'false':
        data["status"] = 0
        data["content"] = "Failure - Delete source file arg invalid"
        return data

    chapters = 1
    if number_of_part != '0':
        try:
            number_of_part = int(number_of_part)
        except ValueError:
            data["status"] = 0
            data["content"] = "Failure - Number of part invalid"
            return data

        file_size = os.path.getsize(file)
        max_size = file_size / number_of_part
    else:
        try:
            file_size = int(file_size)
        except ValueError:
            data["status"] = 0
            data["content"] = "Failure - File size invalid"
            return data
        max_size = file_size * 1024 - 1

    max_size = int(math.floor(max_size))
    temp = ''
    with open(file, 'rb') as src:
        while True:
            tgt = open(file + '.%03d' % chapters, 'wb')
            written = 0
            while written < max_size:
                if len(temp) > 0:
                    tgt.write(temp)
                tgt.write(src.read(min(BUF, max_size - written)))
                written += min(BUF, max_size - written)
                temp = src.read(1)
                if len(temp) == 0:
                    break
            tgt.close()
            if len(temp) == 0:
                break
            chapters += 1

    if del_src == 'true':
        os.remove(file)

    data["status"] = 1
    data["content"] = "split " + str(chapters) + " files"
    return data


def print_result(data):
    status = data["status"]
    content = data["content"]
    if status == 1:
        print(Fore.GREEN + content)
    elif status == 0:
        print(Fore.RED + content)
