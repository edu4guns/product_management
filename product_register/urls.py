from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.form, name='add'),
    path('<int:id>', views.form, name='edit'),
    path('list/', views.list, name='list'),
    path('delete/<int:id>', views.delete, name='delete'),
]
