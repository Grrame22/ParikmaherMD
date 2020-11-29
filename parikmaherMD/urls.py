from . import views
from django.urls import path

urlpatterns = [
    path("", views.HomePageView.as_view(), name="home_page"),
    path("hairdressing_filter/<int:id>/", views.HairdressingAreaView.as_view(),
         name="hairdressing_area"),
    path("hairdressing/<int:id>/", views.ParticularHairdressingView.as_view(),
         name="hairdressing"),
]
