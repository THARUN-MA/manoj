from django.shortcuts import render,redirect
from ii.models import userdetail,userfiles,counter
# Create your views here.
def index(request):
    request.session['usr']=""
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":
        if userdetail.objects.filter(email=request.POST['your-email']).exists():
            return redirect('ii:signup')
        else:
            userdetail(email=request.POST['your-email'],name=request.POST['full-name'],password=request.POST['password']).save()
            return redirect('ii:login')
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        if userdetail.objects.filter(email=request.POST['inputEmail'],password=request.POST['inputPassword']).exists():
            print('YSE')
            request.session['usr']=request.POST['inputEmail']
            return redirect('ii:dashboard')
        else:
            print('NO')
            return redirect('ii:login')
    return render(request,'login.html')

def logout(request):
    request.session['usr']=""
    return render(request,'index.html')


def dashboard(request):
    if request.session['usr']:
        context={}
        iidd=counter.objects.all()
        context['data']=userfiles.objects.all()
        if request.method=="POST":
            if request.FILES['myfile']:
                userfiles(aid=iidd[0].aid,title=request.FILES['myfile'].name,files=request.FILES['myfile']).save()
                counter.objects.filter(aid=iidd[0].aid).update(aid=str(int(iidd[0].aid)+1))

        # iidd=counter.objects.all()
        # counter.objects.filter(aid=iidd[0].aid).update(aid=str(int(iidd[0].aid)+1))



        return render(request,'dashboard.html',context)
    else:
        return redirect('ii:login')

def viewanalysis(request,value=None):
    if request.session['usr']:
        return render(request,'viewanalysis.html')
    else:
        return redirect('ii:login')
