from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, login , logout
# Create your views here.
def SingIn(request):
    if request.user.is_authenticated:
        return render(request, '/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
    return render(request, 'account_app/sing_in.html'  , {})



    return render(request , 'account_app/sing_in.html')

def SingUp(request):
    return render(request , 'account_app/sing_up.html')


def Logout(request):
    logout(request)
    return redirect('/')