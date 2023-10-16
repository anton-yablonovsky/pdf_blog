from django.urls import path
from api import views

# define the urls
urlpatterns = [
    path("login/", views.login_view),
    path("logout/", views.logout_view),
    path("session/", views.session_view),
    path("get_csrf/", views.get_csrf),
    path("get_username/", views.get_username),
    path("create_user/", views.create_user),
    path("create_article/", views.create_article),
    path("get_articles_list/", views.get_articles_list),
    path("send_pdf/", views.send_pdf),
]
