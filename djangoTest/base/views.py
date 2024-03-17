from django.shortcuts import render, redirect
from .forms import VINForm
import requests

def generate_vin(request):
    if request.method == 'POST':
        form = VINForm(request.POST)
        if form.is_valid():
            vin_instance = form.save(commit=False)
            vin_instance.serial_number = get_serial_number_from_server(vin_instance)
            vin_instance.save()
            return redirect('vin_list')
    else:
        form = VINForm()
    return render(request, 'vin_generator_app/generate_vin.html', {'form': form})

def get_serial_number_from_server(vin_instance):
    # Simulate sending a POST request to the server to get serial number
    response = requests.post('http://webtest.pekauto.com', json={
        'version': vin_instance.version,
        'equipment_code': vin_instance.equipment_code,
        'year_of_issue': vin_instance.year_of_issue,
        'place_of_production': vin_instance.place_of_production,
    })
    return response.text

def vin_list(request):
    vins = VIN.objects.all()
    return render(request, 'vin_generator_app/vin_list.html', {'vins': vins})
