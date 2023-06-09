from django.shortcuts import render
from app.models import Student

def add_data(request):
    return render(request, 'student_data.html')

def stu_insert(request):
    if request.method=='POST':
        stu_name=request.POST['stu_name']
        stu_email=request.POST['stu_email']
        stu_layer=request.POST['stu_layer']
        newuser = Student.objects.create(stu_name=stu_name,stu_email=stu_email,stu_layer=stu_layer)
        data =Student.objects.all()
        return render(request,'home.html',{'key1':data})

def student_detail_page(request): 
    if request.method=='GET':
        data = Student.objects.all()      
        return render(request, 'home.html',{'key1':data})
    
    elif request.method=='POST':
        layer = request.POST.get('injest')
        # print(layer)
        if layer=='injest':
            print(layer)
            data = Student.objects.filter(stu_layer='injest').values()
            return render(request, 'home.html',{'key1':data})
        elif layer=='conform':
            print(layer)
            data = Student.objects.filter(stu_layer='conform').values()
            return render(request, 'home.html',{'key1':data})
        elif layer=='Pre-comform':
            print(layer)
            data = Student.objects.filter(stu_layer='Pre-comform').values()
            return render(request, 'home.html',{'key1':data})
# def injest_data(request):
#     data = Student.objects.filter(stu_layer='injest').values()
#     return render(request, 'injest.html',{'key':data})   

# def student_pre_conform(request):
#     data = Student.objects.filter(stu_layer='Pre-comform').values()
#     return render(request, 'pre_conform.html',{'key':data})

# def student_conform(request):
#     data = Student.objects.filter(stu_layer='conform').values()
#     return render(request, 'conform.html',{'key':data})

