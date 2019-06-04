import os


def log(*args):
    if os.environ.get('env') != 'prod':
        print(*args)
