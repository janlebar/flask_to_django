from django.shortcuts import render, redirect
import requests
from .forms import VINForm
from .models import VIN

def home(request):
    form = VINForm(request.POST or None)
    serial_number = None
    vin_generated = None

    if form.is_valid():
        vin = form.save(commit=False)
        vin_serial = get_next_serial_number(vin.version, vin.equipment_code, vin.year_of_issue, vin.place_of_production)
        vin.serial_number = vin_serial
        vin_generated = str(vin)
        form = VINForm()

    context = {
        'form': form,
        'vin_generated': vin_generated,
    }
    return render(request, 'home.html', context)

def get_next_serial_number(version, equipment_code, year_of_issue, place_of_production):
    payload = {
        'version': version,
        'equipment_code': equipment_code,
        'year_of_issue': year_of_issue,
        'place_of_production': place_of_production
    }
    response = requests.post('http://webtest.pekauto.com', json=payload)
    serial_number = response.json().get('serial_number')
    return serial_number

def add_vin_to_database(request):
    if request.method == 'POST':
        vin_string = request.POST.get('vin_string')
        vin = VIN.objects.create(version=vin_string[:3], equipment_code=vin_string[3:6], 
                                  year_of_issue=vin_string[6:8], serial_number=vin_string[9:16], 
                                  place_of_production=vin_string[17:])
        vin.save()
    return redirect('home')

