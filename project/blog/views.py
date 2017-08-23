from django.http import HttpResponse
from django.shortcuts import get_list_or_404, render
from django.views import generic

from .models import Meme

# Create your views here.


def index(request):
    memes = get_list_or_404(Meme)
    print(memes)
    return HttpResponse("Hello, world. You're at the polls index.")


class IndexView(generic.ListView):
    template_name = 'blog/index.html'
    la = Meme.objects.order_by('-pub_date')[:5]
    for l in la:
        v = l.image
        k = dir(l.image)

    def get_queryset(self):
        """Return the last five published questions."""
        return Meme.objects.order_by('-pub_date')[:15]
