from pathlib import Path
from django.urls import path

from .views import index,item,detail,create_item,ItemUpdateView,ItemDeleteView,my_view

app_name = "food"

urlpatterns = [
    path('',index,name='index'),
    path('item/',item,name='item'),
    path('detail/<int:pk>/',detail,name='detail'),
    path('add/',create_item,name='add'),
    path('update/<int:pk>/',ItemUpdateView.as_view(),name='update'),
    path('delete/<int:pk>/',ItemDeleteView.as_view(),name='delete'),
    path('my_view',my_view,name='my_view'),
 
]
