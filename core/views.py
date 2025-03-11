# views.py
from django.shortcuts import render
from django.http import JsonResponse
from .models import Country, State
from .forms import LocationForm

def location_view(request):
    form = LocationForm()

    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            # Handle form submission
            country = form.cleaned_data['country']
            state = form.cleaned_data['state']
            # Process your data here
            return render(request, 'core/location_success.html', {'country': country, 'state': state})

    return render(request, 'core/location_form.html', {'form': form})

def get_states(request):
    country_id = request.GET.get('country_id')
    states = State.objects.filter(country_id=country_id).values('id', 'name')
    return JsonResponse(list(states), safe=False)
