from django.urls import path
from .views import MenuListView, MenuCreateView, MenuDeleteView, MenuDetailView



urlpatterns = [
    path('', MenuListView.as_view(), name='list'),
    path('create/', MenuCreateView.as_view(), name='create'),
    path('delete/<int:pk>', MenuDeleteView.as_view(), name='delete'),
    path('detail/<int:pk>', MenuDetailView.as_view(), name='detail'),
]