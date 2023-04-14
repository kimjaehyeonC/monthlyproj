"""
URL configuration for assignment project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from introduce.views import index, data_understanding, data_visualization, report, report2, report3, report4, report5, camping

urlpatterns = [
#     path('introduce/', include('introduce.urls')),
    path('', index, name = 'index'),
#     path('burger/', burger_view),
#     path('<int:pk>/delte', views.delte, name = 'delete'),
    path('camping/',camping),
    path('data_visualization/',data_visualization),
    path('data_understanding/',data_understanding),
    path('data_visualization/report/',report),
    path('data_visualization/report2/',report2),
    path('data_visualization/report3/',report3),
    path('data_visualization/report4/',report4),
    path('data_visualization/report5/',report5),
    path('admin/', admin.site.urls),
]
