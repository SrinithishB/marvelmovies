from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Phase,Movies

# Create your views here.
def home(request):
    p=Phase.objects.all()
    p1=Movies.objects.filter(phase=p.get(phase=1))
    p2=Movies.objects.filter(phase=p.get(phase=2))
    p3=Movies.objects.filter(phase=p.get(phase=3))
    p4=Movies.objects.filter(phase=p.get(phase=4))
    p5=Movies.objects.filter(phase=p.get(phase=5))
    return render(request,'movies/home.html',{'p1':p1,'p2':p2,'p3':p3,'p4':p4,'p5':p5}),HttpResponse(200)
def fav(request):
    m=Movies.objects.filter(fav=True)
    return render(request,'movies/faviroute.html',{'m':m})
def search(request):
    if request.method=='POST':
        s=request.POST['search']
        if s=='':
            return render(request,'reviews/home.html',{'error':"No result fount"})
        m=Movies.objects.all()
        l=[]
        for i in m:
            if s.lower() in str(i.mname.lower()).split():
                l+=[i]
            try:
                if int(s) == int(i.year):
                    l+=[i]
            except:
                pass

        return render(request,'movies/search.html',{'m':l})
    return render(request,'movies/search.html')
def about(request):
    return render(request,'movies/about.html')
