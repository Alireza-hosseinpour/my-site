from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Post

app_name = 'blog'


def index_view(request):
    return render(request, 'index.html', {})


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


