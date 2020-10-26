from django.shortcuts import render, redirect, get_object_or_404
''' render to return template(html pages), redirect to return similar to render, get_object_404 for validation'''
from django.views.generic import ListView, DetailView
from .models import Character
from .forms import CharacterForm

# Create your views here.

class IndexView(ListView):  # inherit from ListView # pylint: disable=too-many-ancestors
    '''all characters list view'''
    template_name = 'index.html'         # set template_name manually
    context_object_name = 'character_list'          # set context name

    def get_queryset(self):         # what to return(model)
        return Character.objects.all()          # all models

class CharacterDetailView(DetailView):   # pylint: disable=missing-class-docstring
    model = Character
    template_name = 'character_detail.html'

def create(request):   # crete manually without CreateView
    if request.method == 'POST':    # POST means sending data to the server
        form = CharacterForm(request.POST)
        if form.is_valid():
            form.save()              # save form, send data to server? 
            return redirect('index')    # redirect to main page(index url)
    form = CharacterForm()

    # render means the page to display
    # request, templatename, form to pass on
    return render(request, 'create.html', {'form': form})

def edit(request, pk):
    '''pk for primary key'''
    character = get_object_or_404(Character, pk=pk)
    # define instance for form below
    form = CharacterForm(request.POST or None, instance=character)
    if form.is_valid():
        form.save()
        return redirect('index')
    return render(request, 'edit.html', {'form':form})

def delete(request, pk):
    character = get_object_or_404(Character, pk=pk)
    if request.method=='POST':
        character.delete()
        return redirect('index')
    return render(request, 'delete.html', {'object':character})

