import psutil
from tabulate import tabulate

from .my_utils import pprint_title


def main():
    pprint_title("CPU")

    pprint_title("cores")
    cores = psutil.cpu_count(logical=True)
    table = [[cores]]
    print(tabulate(table))

    pprint_title("load average")
    table = [[str(_) for _ in psutil.getloadavg()]]
    print(tabulate(table, headers=['1', '5', '15'], floatfmt='.2f'))

    pprint_title("times")
    table = psutil.cpu_times_percent(interval=1, percpu=True)
    print(tabulate(table, showindex=True, headers='keys', floatfmt='.2f'))

    pprint_title("utilization")
    table = [[str(_) for _ in psutil.cpu_percent(interval=1, percpu=True)]]
    print(tabulate(table, headers=[_ for _ in range(cores)], floatfmt='.2f'))


if __name__ == '__main__':
    main()
