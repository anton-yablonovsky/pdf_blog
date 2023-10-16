import json
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.middleware.csrf import get_token
from django.contrib.auth.models import User
from .models import Article
from django.http import FileResponse
from django.views.decorators.csrf import csrf_exempt


@require_POST
def login_view(request):
    data = json.loads(request.body)
    print(data)
    username = data.get("username")
    password = data.get("password")

    if username is None or password is None:
        return JsonResponse(
            {"detail": "Please provide username and password."}, status=400
        )

    user = authenticate(username=username, password=password)

    if user is None:
        return JsonResponse({"detail": "Invalid credentials."}, status=400)

    login(request, user)
    return JsonResponse({"detail": "Successfully logged in."})


@require_GET
def logout_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({"detail": "You're not logged in."}, status=400)

    logout(request)
    return JsonResponse({"detail": "Successfully logged out."})


@require_GET
def session_view(request):
    return JsonResponse({"is_authenticated": request.user.is_authenticated})


@require_GET
def get_csrf(request):
    token = get_token(request)
    return JsonResponse({"token": token})


@require_GET
def get_username(request):
    username = request.user.username
    return JsonResponse({"username": username})


@require_POST
def create_user(request):
    data = json.loads(request.body)
    username = data.get("username")
    password = data.get("password")
    User.objects.create_user(username=username, password=password)
    return JsonResponse({"status": "ok"})


@require_POST
def create_article(request):
    pdf = request.FILES["pdf"]
    article = Article.objects.create(title=pdf.name, pdf=pdf)
    article.save()
    return JsonResponse({"status": "ok"})


@require_GET
def get_articles_list(request):
    articles_list = Article.objects.all()
    return JsonResponse({"articles_list": [article.title for article in articles_list]})


@require_POST
def send_pdf(request):
    data = json.loads(request.body)
    file_name = data.get("title")
    pdf = open(f"media/{file_name}", "rb")
    response = FileResponse(pdf)
    return response
