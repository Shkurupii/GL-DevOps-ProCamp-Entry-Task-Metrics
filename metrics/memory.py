import psutil
from tabulate import tabulate

from .my_utils import pprint_title


def main():
    pprint_title('MEMORY')
    pprint_title('virtual memory')
    table = zip(
        psutil.virtual_memory()._fields,
        psutil.virtual_memory()
    )
    print(tabulate(table, disable_numparse=True))

    pprint_title('swap')
    table = zip(
        psutil.swap_memory()._fields,
        psutil.swap_memory()
    )
    print(tabulate(table, disable_numparse=True))


if __name__ == '__main__':
    main()
