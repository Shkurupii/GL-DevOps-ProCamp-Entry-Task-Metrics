from psutil._common import bytes2human


def pprint_title(title):
    print("\n" + title + "\n" + "-" * len(title))


def pprint_list(lst):
    for elem in lst:
        print('%.2f | ' % elem, end=' ')
    print()


def pprint_ntuple(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        print('%-5s : %10s | ' % (name.capitalize(), value), end=' ')
    print()


def pprint_ntuple_with_bytes(nt):
    for name in nt._fields:
        value = getattr(nt, name)
        if name != 'percent':
            value = bytes2human(value)
        print('%-10s : %7s' % (name.capitalize(), value))
