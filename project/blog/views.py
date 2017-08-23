from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render
from django.views import generic

from .models import Meme

# Create your views here.


class IndexView(generic.ListView):
    template_name = 'blog/index.html'

    def get_queryset(self):
        """Return the last five published questions."""
        return Meme.objects.order_by('-pub_date')[:15]
