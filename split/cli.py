from colorama import init
import click
from .functions import split_file, print_result

init(autoreset=True)


@click.command()
@click.argument("file")
@click.option("--file-size", help="File size (kb) of file 001, 002, ...", default=199)
@click.option("--number-of-part", help="Number of path", default=0)
@click.option("--del-src", help="Delete source file", default=1)
def main(file, file_size, number_of_part, del_src):
    data = split_file(file, file_size, number_of_part, del_src)
    print_result(data)


def start():
    main(obj={})


if __name__ == "__main__":
    start()