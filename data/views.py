from django.db.models import Q
from django.shortcuts import render
from django.views.generic import ListView

# from django.views.generic import View

# Create your views here.
from data.models import Data


class IndexView(ListView):
    model = Data

    def get(self, request, *args, **kwargs):
        items = Data.objects.all()
        context = {
            'items': items
        }
        return render(request, 'index.html', context)


def search(request):
    queryset_list = Data.objects.order_by('-title')
    if 'q' in request.GET:
        q = request.GET['q']
        if q:
            queryset_list = queryset_list.filter(Q(title__icontains=q) |
                                                 Q(name__icontains=q) |
                                                 Q(description__icontains=q)).distinct()

    context = {
        'items': queryset_list
    }
    return render(request, 'search.html', context)
