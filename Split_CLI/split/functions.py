from colorama import Fore

BUF = 50*1024*1024*1024


def split_file(file: str, file_size: int, number_of_part: int):
    data = {}
    max_size = int(file_size) * 1024

    chapters = 1
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
