from app.models import User, PopUp, Product, Category
from django.shortcuts import redirect, render, get_object_or_404
from app.forms import RegisterForm, LoginForm
from django.contrib.auth import login, authenticate, logout

# Create your views here.
from app.utls import now, save_delivery_company


def index(request):
    category = request.GET.get("category")
    pop_up = PopUp.objects.filter(ended_at__gt=now()).all()

    if not category:
        category_obj = None
        products = Product.objects.order_by("-created_at").all()
    else:
        category_obj = Category.objects.filter(id=category).first()
        products = Product.objects.filter(category=category_obj).order_by("-created_at").all()

    return render(request, "index.html", {"pop_up": pop_up, "product": products, "category_obj": category_obj})



def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        msg = "올바르지 않은 데이터 입니다."
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            msg = "회원가입완료"
        return render(request, "register.html", {"form": form, "msg": msg})
    else:
        return render(request, "register.html", {})


def login_view(request):
    is_ok = False
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            raw_password = form.cleaned_data.get("password")
            remember_me = form.cleaned_data.get("remember_me")
            msg = "올바른 유저ID와 패스워드를 입력하세요."
            try:
                user = User.objects.get(user__email=email)
            except User.DoesNotExist:
                pass
            else:
                if user.user.check_password(raw_password):
                    msg = None
                    login(request, user.user)
                    is_ok = True
                    request.session["remember_me"] = remember_me
                    return redirect("index")
        else:
            msg = "올바르게 입력해주세요."
    else:
        msg = None
        form = LoginForm()
        if request.user.is_authenticated:
            return redirect("index")
    return render(request, "login.html", {"form": form, "msg": msg, "is_ok": is_ok})


def logout_view(request):
    logout(request)
    return redirect("login")


def get_pop_up(request, pop_up_id):
    pop_up = get_object_or_404(PopUp, id=pop_up_id)

    return render(request, "pop_up.html", {"pop_up": pop_up})
