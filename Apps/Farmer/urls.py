from django.urls import path

from . import views


urlpatterns = [
    path('', views.Home, name="Home"),
    path('AddProduct/', views.AddProduct, name="AddProduct"),
    path('UploadProduct/', views.UploadProduct, name="UploadProduct"),
    path('EditProduct/<int:id>', views.EditProduct, name="EditProduct"),
    path('UpdateProduct/<int:id>', views.UpdateProduct, name="UpdateProduct"),
    path('DeleteProduct/<int:id>', views.DeleteProduct, name="DeleteProduct")

]
