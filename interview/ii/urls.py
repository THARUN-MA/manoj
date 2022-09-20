from django.conf.urls import url,include
from ii import views

app_name='ii'

urlpatterns=[
    url('login/',views.login,name='login'),
    url('signup/',views.signup,name='signup'),
    url('logout/',views.logout,name='logout'),
    url('dashboard/',views.dashboard,name='dashboard'),
]
