from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("singup/",views.singup,name="singup"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("profile/",views.profile,name="profile"),
    path("account/",views.account,name="account"),
    path("transaction/",views.transaction,name="transaction"),
    path("userlogout/",views.userlogout,name="userlogout"),
]