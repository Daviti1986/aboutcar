#from django.shortcuts import render
#from django.http import HttpResponse
#from .models import Car
#from django.http import Http404
from django.views import generic
from .models import Car
from django.views.generic.edit import CreateView


class IndexView(generic.ListView):
    template_name = 'cars/index.html'


    def get_queryset(self):
        return Car.objects.all()
class CarCreate(CreateView):
    model = Car
    fields = ['Make', 'Model', 'Type', 'Year', 'Fuel_Type', 'VIN_Code', 'Mileage', 'car_image' ]


class DetailView(generic.DetailView):
    model = Car
    template_name = 'cars/detail.html'



































# Create your views here.

#def index (request):
    #all_cars = Car.objects.all()
    #context = {
        #'all_cars': all_cars
    #}
    #return render(request, 'cars/index.html', context)

#def detail(request, car_id):
    #try:
        #car = Car.objects.get(id = car_id)
    #except Car.DoesNotExist:
        #raise Http404('This car  does not exist')
    #return render(request, 'cars/detail.html', {'car':car})
