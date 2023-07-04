from django.urls import path
from .views import SignUp, user_login, login_with_code

urlpatterns = [
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', user_login, name='user_login'),
    path('login/code', login_with_code, name='user_login_code'),
]