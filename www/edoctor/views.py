# django
from django.shortcuts import render
from django.http import JsonResponse

# my
from edoctor.models import Address


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