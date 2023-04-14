from django.shortcuts import render
from django.http import HttpResponse
# from .models import Burger
# from .forms import BurgerForm
# from django.template import loader
# Create your views here.

def index(request):
    return render(request, 'index.html', {})

# folium
def camping(request):
    return render(request, "camping.html",{})

# 데이터 파악
def data_understanding(request):
    return render(request, 'data_understanding.html', {})

# 데이터 시각화
def data_visualization(request):
    return render(request, 'data_visualization.html', {})

# report

def report(request):
    return render(request, 'report.html', {})

def report2(request):
    return render(request, 'report2.html', {})

def report3(request):
    return render(request, 'report3.html', {})

def report4(request):
    return render(request, 'report4.html', {})

def report5(request):
    return render(request, 'report5.html', {})

# def burger_view(request):
#     burger_all = Burger.objects.all()
    
#     if request.method == 'POST': #method가 post일 때
#         form = BurgerForm(request.POST)
#         if form.is_valid(): # Form이 유효하면 저장
#             form.save()
            
#     form = BurgerForm()
    
#     return render(request, 'burger.html', {'burger_list' : burger_all, 'burger_form' : form})

# def delete(request, pk):
#     burger = Burger.objects.get(pk=pk)
#     burger.delete()
#     return redirect('burger_view')