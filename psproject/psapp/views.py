from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

def index(request):
    movie = Movie.objects.all()
    context = {
        'movie_list': movie
    }
    return render(request, 'index.html', context)

def detail(request, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(request, "details.html", {'movie': movie})

def add_movie(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('psapp:index')
    else:
        form = MovieForm()
    return render(request, 'add.html', {'form': form})

def update(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('psapp:index')
    else:
        form = MovieForm(instance=movie)
    return render(request, 'edit.html', {'form': form, 'movie': movie})

def delete(request, id):
    movie = Movie.objects.get(id=id)
    if request.method == "POST":
        movie.delete()
        return redirect('psapp:index')
    return render(request, 'delete.html', {'movie': movie})
