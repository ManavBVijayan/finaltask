
from django.shortcuts import render
from .models import department, employee

def getdata(request):
    if request.method=='POST':
        name=request.POST.get('name')
        dob=request.POST.get('dob')
        age=request.POST.get('age')
        appform=employee(name=name,dob=dob,age=age)
        appform.save()
        return render(request,'final.html')
    template_name = 'appform.html'
    deptcontext = department.objects.all()
    empcontext = employee.objects.all()

    return render(request, template_name,{'department': deptcontext,'employee': empcontext } )
def index(request):
    return render(request,'home.html')
def final(request):
    return render(request,'final.html')