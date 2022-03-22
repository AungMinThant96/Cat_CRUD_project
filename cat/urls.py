from django.urls import path
from . import views
app_name = "cat"
urlpatterns = [
    path('',views.MainView.as_view(),name="all"),
    path('breed/',views.BreedView.as_view(),name="breedview"),
    path('breed/add',views.BreedCreate.as_view(),name="breedcreate"),
    path('breed/update/<int:pk>/',views.BreedUpdate.as_view(),name="breedupdate"),
    path('breed/delete/<int:pk>/',views.BreedDelete.as_view(),name="breeddelete"),
    path('cat/',views.CatCreate.as_view(),name="catcreate"),
    path('cat/catupdate/<int:pk>/',views.CatUpdate.as_view(),name="catupdate"),
    path('cat/catdelete/<int:pk>/',views.CatDelete.as_view(),name="catdelete"),
    ]
