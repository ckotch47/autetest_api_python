import argparse
import manage_service

parser = argparse.ArgumentParser(description="sample argument parser")

parser.add_argument('-c', help='create test module -c {path} example python manage.py -c src/tests/spaces ')

args = parser.parse_args()

if args.c:
    manage_service.create_module(args.c)
    print('create')

#python manage.py -c src/tests/spaces
