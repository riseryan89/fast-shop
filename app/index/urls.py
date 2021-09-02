from app.index.views import index, register, login_view, logout_view, get_pop_up
from django.urls import path

urlpatterns = [
    path("", index, name="index"),
    path("register", register, name="register"),
    path("pop_up/<int:pop_up_id>", get_pop_up, name="get_pop_up"),
    path("login", login_view, name="login"),
    path("logout", logout_view, name="logout"),
]
