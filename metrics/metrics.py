import importlib
import sys
from os import name
from subprocess import call
from time import sleep

# print("This is the name of the program:", sys.argv[0])
# print("Number of elements including the name of the program:", len(sys.argv))
# print("Number of elements excluding the name of the program:", (len(sys.argv) - 1))
# print("Argument List:", str(sys.argv))
# print()

supported_metrics = [
    'cpu',
    'disk',
    'memory',
    'network',
]


def helper():
    print('Valid arguments are:')
    for metric in supported_metrics:
        print(metric)
    print()


def clear():
    _ = call('clear' if name == 'posix' else 'cls')


if len(sys.argv) != 2:
    print("Oops!  Specify one argument! Try again...")
    helper()
    print("Exit!")
    sys.exit(1)

if not sys.argv[1] in supported_metrics:
    print("Oops!  Bad argument! Try again...")
    helper()
    print("Exit!")
    sys.exit(1)


def main():
    while True:
        try:
            module_name = 'metrics.' + sys.argv[1]
            module = importlib.import_module(module_name)
            module.main()
            sleep(3)
            clear()
        except KeyboardInterrupt:
            print("\nFinished")
            sys.exit(0)


if __name__ == '__main__':
    main()
