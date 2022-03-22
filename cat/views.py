from django.shortcuts import render,get_object_or_404
from django.views import View
from cat.models import Cat,Breed
from django.contrib.auth.mixins import LoginRequiredMixin
from cat.forms import CatForm
from django.urls import reverse,reverse_lazy
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Create your views here.
class MainView(LoginRequiredMixin,View):
    def get(self,request):
        breed_count = Breed.objects.all().count()
        cat_value = Cat.objects.all()
        ctx = {"breed_count":breed_count,"cat_value":cat_value}
        return render(request,'cat/main_view.html',ctx)

class BreedView(LoginRequiredMixin,View):
    def get(self,request):
        breed_value = Breed.objects.all();
        return render(request,'cat/breed_view.html',{"breed_value":breed_value})

class BreedCreate(LoginRequiredMixin,CreateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy("cat:breedview")

class BreedUpdate(LoginRequiredMixin,UpdateView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy("cat:breedview")

class BreedDelete(LoginRequiredMixin,DeleteView):
    model = Breed
    fields = '__all__'
    success_url = reverse_lazy("cat:breedview")

class CatCreate(LoginRequiredMixin,View):
    def get(self,request):
        form = CatForm()
        return render(request,'cat/cat_create.html',{"form":form});

    def post(self,request):
        form = CatForm(request.POST)
        if not form.is_valid():
            return render(request,'cat/cat_create.html',{"form":form});
        cat = form.save()
        return HttpResponseRedirect(reverse("cat:all"))

class CatUpdate(LoginRequiredMixin,View):
    def get(self,request,pk):
        value = get_object_or_404(Cat,pk=pk)
        form = CatForm(instance=value)
        return render(request,'cat/cat_create.html',{"form":form})

    def post(self,request,pk):
        value = get_object_or_404(Cat,pk=pk)
        form = CatForm(request.POST,instance=value)
        if not form.is_valid():
            return render(request,'cat/cat_create.html',{"form":form})
        cat = form.save()
        return HttpResponseRedirect(reverse("cat:all"))

class CatDelete(LoginRequiredMixin,View):
    def get(self,request,pk):
        cat = get_object_or_404(Cat,pk=pk)
        #form = CatForm(instance=value)
        return render(request,'cat/cat_delete.html',{"cat":cat})

    def post(self,request,pk):
        value = get_object_or_404(Cat,pk=pk)
        value.delete()
        return HttpResponseRedirect(reverse("cat:all"))
            
    
        
