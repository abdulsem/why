from django.urls import path
from . import views
from . views import MyTokenObtainPair
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . views import Whynot
app_name = 'one'
urlpatterns = [
    path("",views.getUser),
    path('api/token/', MyTokenObtainPair.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('give', views.giveuser, name='give'),
    path('img', views.givepost, name='img'),
    path('imgg', views.givepostt, name='img'),
    path('imggl',Whynot.as_view() , name='ilmg'),
    path('l/<str:pk>',views.deletpostt , name='delet'),
]
