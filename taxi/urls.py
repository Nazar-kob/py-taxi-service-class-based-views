from django.urls import path

from .views import index, ManufacturerListView, CarListView,\
    CarDetailView, DriverListView, DriverDetailView

urlpatterns = [
    path("", index, name="index"),
    path("manufacturers/",  ManufacturerListView.as_view(), name='manufacturers-list'),
    path("cars/",  CarListView.as_view(), name='cars-lit'),
    path("cars/<int:pk>", CarDetailView.as_view(), name='car_detail'),
    path("drivers/", DriverListView.as_view(), name='drivers-list'),
    path("drivers/<int:pk>", DriverDetailView.as_view(), name='driver_detail')

]

app_name = "taxi"
