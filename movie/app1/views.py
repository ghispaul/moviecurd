from django.shortcuts import render
from django.urls import reverse_lazy

from app1.models import Movies
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
# def home(request):
#     k=Movies.objects.all()
#     return render(request,'home.html',{'movies':k})
class home(ListView):
    model = Movies

    template_name = 'home.html'

    context_object_name = 'movies'


# def addmovie(request):
#     if (request.method == "POST"):
#         t = request.POST['t']
#         d = request.POST['d']
#         y = request.POST['y']
#         l = request.POST['l']
#         i = request.FILES['i']
#         b = Movies.objects.create(title=t, description=d, year=y, language=l, image=i)
#         b.save()
#
#         return render(request, 'home.html')
#     return render(request,'add.html')

class addmovie(CreateView):
    model = Movies


    fields = ['title','description','year','language','image']
    template_name = 'add1.html'

    success_url = reverse_lazy('app1:home')

# def details(request,p):
#     k=Movies.objects.get(id=p)
#     return render(request,'details.html',{'m':k})

class details(DetailView):
    model = Movies

    template_name = 'details.html'

    context_object_name = 'm'

# def edit(request,p):
#     k=Movies.objects.get(id=p)
#     if(request.method=='POST'):
#         k.title=request.POST['t']
#         k.description=request.POST['d']
#         k.year=request.POST['y']
#         k.language=request.POST['l']
#         if(request.FILES.get('i')==None):
#             k.save()
#         else:
#             k.image=request.FILES.get('i')
#         k.save()
#         return home(request)
#     return render(request,'editmovies.html',{'m':k})

class edit(UpdateView):
    model = Movies

    fields = ['title','description','year','language','image']

    template_name = 'edit1.html'

    success_url = reverse_lazy('app1:home')

# def delete(request,p):
#     k=Movies.objects.get(id=p)
#     k.delete()
#     return home(request)

class delete(DeleteView):
    model = Movies
    template_name = 'delete.html'
    success_url = reverse_lazy('app1:home')