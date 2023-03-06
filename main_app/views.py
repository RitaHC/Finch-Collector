from django.shortcuts import render, redirect
from .models import Finches, Toy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import FeedingForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView

# finchces = [
#     {'name': 'lolo', 'age': 3},
#     {'name': 'solo', 'age': 2},
#     {'name': 'dolo', 'age': 1},
# ]
# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def finches_index(request):
    finches = Finches.objects.all()
    return render(request, 'finches/index.html', {'finches': finches})

def finches_detail(request, finch_id):
    finch = Finches.objects.get(id=finch_id)
    #render feeding form 
    feeding_form = FeedingForm()
    #render toys
    id_list = finch.toys.all().values_list('id')
    toys_finch_dosent_have = Toy.objects.exclude(id__in=id_list)

    return render(request, 'finches/detail.html', {'finch':finch, 'feeding_form': feeding_form, 'toys': toys_finch_dosent_have})


    
class FinchesCreate(CreateView):
    model = Finches
    fields = '__all__'

class FinchesUpdate(UpdateView):
    model = Finches
    fields = ['name','age']

class FinchesDelete(DeleteView):
    model = Finches
    success_url ='/finches/'

def add_feeding(request, finch_id):
    form = FeedingForm(request.POST)

    if form.is_valid():
        
        new_feeding = form.save(commit=False)
        new_feeding.finch_id = finch_id
        new_feeding.save()
    return redirect('detail', finch_id=finch_id)


def assoc_toy(request, finch_id, toy_id):
    Finches.objects.get(id=finch_id).toys.add(toy_id)
    return redirect('detail', finch_id=finch_id)

def unassoc_toy(request, finch_id, toy_id):
    Finches.objects.get(id=finch_id).toys.remove(toy_id)
    return redirect('detail', finch_id=finch_id)



# ToyList
class ToyList(ListView):
    model = Toy
    template_name = 'toys/index.html'

# ToyDetail
class ToyDetail(DetailView):
    model = Toy
    template_name = 'toys/detail.html'

# ToyCreate
class ToyCreate(CreateView):
    model = Toy
    fields = ['name', 'color']

    # define what the inherited method is_valid does(we'll update this later)
    def form_valid(self, form):
        # we'll use this later, but implement right now
        # we'll need this when we add auth
        # super allows for the original inherited CreateView function to work as it was intended
        return super().form_valid(form)

# ToyUpdate
class ToyUpdate(UpdateView):
    model = Toy
    fields = ['name', 'color']

# ToyDelete
class ToyDelete(DeleteView):
    model = Toy
    success_url = '/toys/'

