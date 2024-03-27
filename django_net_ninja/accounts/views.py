from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


# Create your views here.
def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log user in
            login(request, user)

            return redirect("articles:list")
    else:
        form = UserCreationForm()
    return render(request, "accounts/signup.html", {"form": form})


def login_view(request):
    print("login")
    print(request.method)
    if request.method == "POST":
        print("if request.method")
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            print("form.is_valid")
            user = form.get_user()
            login(request, user)
            if "next" in request.POST:
                print("if login view")
                return redirect(request.POST.get("next"))
            else:
                print("else login view")
            return redirect("articles:list")

    else:
        print("else request.method")

        form = AuthenticationForm()

    return render(
        request,
        "accounts/login.html",
        {
            "form": form,
        },
    )


def logout_view(request):
    if request.method == "POST":
        logout(request)
        print('log out view')
        return redirect("articles:list")
