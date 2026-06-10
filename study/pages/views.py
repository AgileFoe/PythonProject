from django.shortcuts import render, redirect
from .models import discribe
from .forms import DiscribeForm
from django.views.generic import DetailView, UpdateView, DeleteView


def page1(request):
    news = discribe.objects.all()
    return render(request, 'pages/page1.html', {'news': news})


class NewsDetailView(DetailView):
    model = discribe
    template_name = 'pages/details_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model = discribe
    template_name = 'pages/create.html'

    form_class = DiscribeForm

class NewsDeleteView(DeleteView):
    model = discribe
    success_url = '/pages/'
    template_name = 'pages/delete.html'


def create(request):
    error = ""
    if request.method == 'POST':
        form = DiscribeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "invalid form"
            print(form.errors)

    form = DiscribeForm()

    data = {
        'form': form,
        'error': error
    }
    return render(request, 'pages/create.html', data)