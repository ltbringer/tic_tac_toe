import os


def log(*args):
    if os.environ.get('ENVIRONMENT') == 'dev':
        print(*args)
