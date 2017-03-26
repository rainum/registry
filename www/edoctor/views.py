# common
import datetime

# django
from django.shortcuts import render
from django.http import JsonResponse
from django.utils.dateparse import parse_date

# my
from edoctor.models import Address, Doctor, Talon


DATES = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']


def home(request):
    addresses = set()

    for address in Address.objects.all():
        addresses.add(address.street)

    data = {
        'addresses': addresses,
    }
    return render(request, 'home.html', data)


def select_address(request):

    data = request.POST or request.GET

    street = data.get('street')
    building = data.get('building')

    try:
        address = Address.objects.get(street=street, house=building)

        data = {
            'doctor': {
                'id': address.doctor.id,
                'first_name': address.doctor.first_name,
                'last_name': address.doctor.last_name,
                'second_name': address.doctor.second_name,
            }
        }
        return JsonResponse(data)
    except Address.DoesNotExist:
        data = {
            'error': 'Адресс в базе данных не найден',
        }
        return JsonResponse(data)


def select_date(request):
    data = request.POST or request.GET

    doctor_id = data.get('doctorId')
    date_str = data.get('date')

    try:
        doctor = Doctor.objects.get(id=doctor_id)
    except Doctor.DoesNotExist:
        data = {
            'slots': [],
        }
        return JsonResponse(data)

    date = parse_date(date_str)

    index = date.weekday()
    weekday = DATES[index]

    start_date = getattr(doctor, '%s_start' % weekday)
    end_date = getattr(doctor, '%s_end' % weekday)

    if not start_date or not end_date or not doctor.duration:
        data = {
            'slots': [],
        }
        return JsonResponse(data)

    current = start_date
    slots = []
    while current < end_date:
        tmp_date = datetime.datetime(year=date.year, month=date.month, day=date.day, hour=current.hour,
                                     minute=current.minute)
        try:
            Talon.objects.get(doctor=doctor, date_of_receipt=tmp_date)
            available = False
        except Talon.DoesNotExist:
            available = True

        slot = {
            'time': current.strftime('%H:%M'),
            'available': available,
        }
        slots.append(slot)

        current += doctor.duration


    data = {
        'slots': slots,
    }
    return JsonResponse(data)
