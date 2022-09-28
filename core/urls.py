from django.urls import path
from . import views


app_name    =   'core'

urlpatterns = [
    path ('', views.IndexView.as_view(), name='index'),
    path ('add/', views.AddView.as_view(), name='add'),
    path ('polls/<int:pk>/', views.PollsView.as_view(), name='polls'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'),
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete')
    
]