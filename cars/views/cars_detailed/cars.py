from django.views import generic
from .models import Car

class IndexView(generic.ListView):
    template_name = 'cars/index.html'


    def get_queryset(self):
        return Car.objects.all()


class DetailView(generic.DetailView):
    model = Car
    template_name = 'cars/detail.html'