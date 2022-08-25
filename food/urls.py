from pathlib import Path
from django.urls import path

from .views import index,item,detail,create_item,ItemUpdateView,ItemDeleteView,my_view,HomePage,ItemDetailView,ItemCreateView

app_name = "food"

urlpatterns = [
    path('',HomePage.as_view(),name='index'),
    path('item/',item,name='item'),
    path('detail/<int:pk>/',ItemDetailView.as_view(),name='detail'),
    path('add/',ItemCreateView.as_view(),name='add'),
    path('update/<int:pk>/',ItemUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',ItemDeleteView.as_view(),name='delete'),
    path('my_view',my_view,name='my_view'),
 
]
