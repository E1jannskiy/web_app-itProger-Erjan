from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView


def news_home(request):
    news = Articles.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news' : news})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'

# def news_detail_view(request, pk):
#     data = Articles.objects.get(id=pk)
#
#     context = {
#         'data': data
#     }
#
#     return render(request, 'news/details_view.html', context)

class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'

    # fields = ['title', 'anons', 'full_text', 'date']
    form_class = ArticlesForm


class NewsDeleteView(DeleteView):
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'



def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной!'

    form = ArticlesForm

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)