from django.shortcuts import render,redirect

# Create your views here.
def homepage(request):
    # return render(request, "common/header/hrheadheader.html")
    return render(request, "common/homepage1.html")


def logout(request):
    return redirect('homepage')