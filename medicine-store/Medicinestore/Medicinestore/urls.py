from django.contrib import admin
from django.urls import path
from medicinecore import views

urlpatterns=[
    path("admin",admin.site.urls),
    path("signup/",views.signup,name="signup"),
    path("login/",views.login_view,name="login"),
    path("home/", views.medicine_list, name="medicine_list"),
    path("add/", views.add_medicine, name="add_medicine"),
    path("edit/<int:pk>/", views.edit_medicine, name="edit_medicine"),
    path("delete/<int:pk>/", views.delete_medicine, name="delete_medicine"),
    path("logout/", views.logout_view, name="logout"),
]
