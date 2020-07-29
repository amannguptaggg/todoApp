from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('<int:id>/update',views.update,name='update'),
    path('<int:id>/delete',views.delete,name='delete'),
    path('<int:id>/complete',views.complete,name='complete'),
    path('deleteAll',views.deleteAll,name='deleteAll'),
    path('about',views.about,name='about')
]