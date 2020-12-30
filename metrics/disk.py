import psutil
from tabulate import tabulate

from .my_utils import pprint_title


def main():
    pprint_title("DISK")

    pprint_title("partitions")
    table = disk_partitions = psutil.disk_partitions()
    print(tabulate(table, showindex=True, headers='keys'))

    pprint_title("usage")
    fields = psutil.disk_usage('/')._fields
    table = []
    mount_points = [_.mountpoint for _ in disk_partitions]
    for mount_point in mount_points:
        row = [mount_point] + [getattr(psutil.disk_usage(mount_point), field) for field in fields]
        table.append(row)
    print(tabulate(table, showindex=True, headers=fields))


if __name__ == '__main__':
    main()
