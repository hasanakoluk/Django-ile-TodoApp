from django.shortcuts import render,redirect
from .models import *
from .forms import *
# Create your views here.
def todo_anasayfa(request):
    # todos = ToDo.objects.all()
    kategoriler = Kategori.objects.all()
    alt_kategoriler = AltKategoriler.objects.all()
    return render(request,'todoapp/anasayfa.html',{
        # "todos":todos,
        "kategoriler":kategoriler,
        "alt_kategoriler":alt_kategoriler
        })


def kategori_view(request,kategori_slug):
    kategori = Kategori.objects.get(slug = kategori_slug)

    todos = ToDo.objects.filter(kategori__id = kategori.id)

    return render(request,"todoapp/kategori.html",{
        'kategori':kategori,
        'todos':todos
    })

def detay_view(request, todo_slug):
    

   todo = ToDo.objects.filter(slug = todo_slug)

   return render(request,"todoapp/detay.html",{
        'todo':todo
    })


def todo_ekle_view(request):


    if request.method == "POST":
        form = Todo_Ekle(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("index_page")
        else:
              form = Todo_Ekle()
              return render(request,"todoapp/todo_ekle.html",{
              'form':form
        })

    form = Todo_Ekle()
    return render(request,"todoapp/todo_ekle.html",{
      'form':form
    })


def todo_edit_view(request,todo_slug):
    todo = ToDo.objects.get(slug = todo_slug)

    if request.method == "POST":
        form = Todo_Ekle(request.POST,request.FILES,instance=todo)
        if form.is_valid():
            form.save()
            return redirect("index_page")

        else:
                form = Todo_Ekle(instance=todo)
                return render(request,"todoapp/edit.html",{
                'form':form
            })  
        


    form = Todo_Ekle(instance=todo)
    return render(request,"todoapp/edit.html",{
        'form':form
    })


def todo_delete_view(request,todo_slug):

    todo = ToDo.objects.get(slug = todo_slug)

    if request.method == "POST":
        todo.delete()
        return redirect('index_page')
     
    return render(request, "todoapp/delete.html",{
        'todo':todo
    })

    
def alt_kategori_view(request, alt_kategori_slug):
    alt_kategori = AltKategoriler.objects.get(slug = alt_kategori_slug)

    todos = ToDo.objects.filter(alt_kategoriler__id = alt_kategori.id)

    return render(request,'todoapp/alt_kategori.html',{
        'alt_kategori':alt_kategori,
        'todos':todos
    })    
           
