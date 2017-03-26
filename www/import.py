import os
os.environ['DJANGO_SETTINGS_MODULE'] = 'www.settings'

import django
django.setup()

import csv

from edoctor.models import Doctor, Address

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'csv'))


for filename in os.listdir(BASE_DIR):
    full_filename = os.path.join(BASE_DIR, filename)
    with open(full_filename, encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=';', quotechar='\'')

        row = next(reader)
        spec = row[0].strip()

        for row in reader:

            row = list(map(lambda r: r.strip(), row))

            try:
                doctor = Doctor.objects.get(first_name=row[1], last_name=row[0], second_name=row[2])
            except Doctor.DoesNotExist:
                doctor = Doctor(first_name=row[1], last_name=row[0], second_name=row[2], specialization=spec)
                doctor.save()

            try:
                Address.objects.get(street=row[3], house=row[4])
            except Address.DoesNotExist:
                adress = Address(street=row[3], house=row[4])
                adress.doctor = doctor
                adress.save()