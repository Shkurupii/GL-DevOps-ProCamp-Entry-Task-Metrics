import sys

import psutil
from psutil import AccessDenied
from tabulate import tabulate

from .my_utils import pprint_title


def main():
    pprint_title("NETWORK")

    pprint_title("net if addrs")
    net_if_addrs = psutil.net_if_addrs()
    table = []
    headers = ['if_name', 'family', 'address', 'netmask', 'broadcast', 'ptp']
    for if_name, if_addrs in net_if_addrs.items():
        table = table + [[if_name] + list(_) for _ in if_addrs]
    print(tabulate(table, headers=headers))

    pprint_title("net connections")
    try:
        net_connections = psutil.net_connections(kind='inet')
        table = []
        headers = ['fd', 'family', 'type', 'laddr', 'raddr', 'status', 'pid']
        for conn in net_connections:
            table = table + [map(str, conn)]
        print(tabulate(table, headers=headers))
    except AccessDenied:
        sys.exit("\n!!! AccessDenied, root permissions is required !!! \n")

    pprint_title("net connections counters")
    try:
        net_connections = psutil.net_connections(kind='inet')
        status_set = set(conn.status for conn in net_connections)
        counter = {}
        for status in status_set:
            counter[status] = sum([1 for conn in net_connections if conn.status == status])
        table = [counter]
        print(tabulate(table, headers='keys'))
    except AccessDenied:
        sys.exit("\n!!! AccessDenied, root permissions is required !!! \n")


if __name__ == '__main__':
    main()
