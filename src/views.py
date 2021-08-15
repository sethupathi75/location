
from django.shortcuts import redirect, render
from django.http import HttpResponse, response
from sethu.form import loginModel
from sethu.models import login
from app.models import student
from app.form import empId


def Register(request):
    # print(login.objects.get(id=id))
    if request.method=="POST":
        form=loginModel(request.POST)
        # print(form.data['email'])
        if form.is_valid():
            if form.data['password'].isalnum() or form.data['password'].startswith('@') and form.data['password'].isalpha or form.data['password'].isidentifier():
                print('fail')
                # err="pass error"
                return render(request,'sethu/register.html',{'err':"* check your password include @ and number",'title':"register"}) 
                
            else:
                print('pass')
                form.save()
                return render(request,'sethu/register.html',{'err1':"success",'title':"register"})
                # return redirect('/msg',err="success")
    return render(request,'sethu/register.html',{'title':"register",'user':False})


def Login(request):
    
    
    data=student.objects.all()
    
    if request.method=="POST":
        form1=loginModel(request.POST)
        password=form1.data['password']
        email=form1.data['email']
        if form1.is_valid():
           
            
            
            valid=login.objects.filter(password=password,email=email)
            for i in valid:
                name_id=i.email
            if len(valid)==0:
                
                return render(request,"sethu/login.html",{'err':'sorry ,your record does not  have','title':"login"})
            else:
                
                    
                return render(request,"sethu/home.html",{'data':data,'user':True,'name_id':name_id,'title':"home"})
    
            
    return render(request,"sethu/login.html",{'title':"login",'user':False})


def home(request):
    data=student.objects.all()
    return render(request,"sethu/home.html",{'data':data,'title':"home",'user':False})


def reorder(request,id):
    data1=student.objects.all()
    data=student.objects.get(id=id)
    if request.method=="POST":
        form=empId(request.POST,request.FILES,instance=data)
        if form.is_valid:
            form.save()
            # return redirect('/',user='sethu')
            return render(request,"sethu/home.html",{'user':True,'data':data1})
    return render(request,'sethu/reorder.html',{'data':data,'title':"recall"})


# def time(request):
#     data={'name' :'sethu'}
#     return render(request,"sethu/one.html",context=data)
# def date(request):
#     cook=request.session.get('count')

#     print(cook)
#     count=int(cook)+1
#     request.session['count']=count
#     print(request.session.get_expiry_date())
#     return render(request,"sethu/one.html",{'total':count})



    # //cookkies
    # cook=request.COOKIES.get('count')
    # print(cook)
    # count=int(cook)+1
    # response= render(request,"sethu/one.html",{'total':count})
    # response.set_cookie('count',count)
    # return response



