from sre_constants import SUCCESS
from django.shortcuts import render,HttpResponseRedirect,redirect

from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView
from .forms import Employeeform,userresi
from .models import Employee_Mst,Designation_Mst
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib import auth, messages
from django.views.generic.base import View

# Create your views here.

# def data(request):
#     if request.method=='POST':
#         dic=Employeeform(request.POST)
#         if dic.is_valid():
#             dic.save()
#             messages.success(request,'Registation sucsessfully .')
#     else:
#         dic=Employeeform()
#     return render(request,'core/home.html',{'form':dic})


        
def employee_regi__view(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm=Employeeform(request.POST)
            if fm.is_valid():
                usr=request.user
                first_name=fm.cleaned_data['first_name']
                last_name=fm.cleaned_data['last_name']
                designationld=fm.cleaned_data['designationld']
                date_of_joining=fm.cleaned_data['date_of_joining']
                salary=fm.cleaned_data['salary']
                reg=Employee_Mst(user=usr,first_name=first_name,last_name=last_name,designationld=designationld,date_of_joining=date_of_joining,salary=salary)
                reg.save()
                messages.success(request,'Data Upload sucsessfully .')
                return HttpResponseRedirect('/')

        else:
            fm=Employeeform
        return render(request,'core/home.html',{'form':fm,'active':'btn-primary'})
    return redirect('/accounts/login')








def Employee_data(request):
    if request.user.is_authenticated:
        data=Employee_Mst.objects.all()
        # print(data)
        # for i in data:
        #     print(i.first_name)
        return render(request,'core/suc.html',{'data':data})
    return redirect('/accounts/login')
    

class update(UpdateView):
    
    template_name='core/edit.html'
    model=Employee_Mst
    fields=['first_name','last_name','designationld','date_of_joining','salary']
    success_url='/suc/'

class delete(DeleteView):
    template_name = 'core/mode_confirm_delete.html'
    model=Employee_Mst
    success_url='/suc/'

class login(LoginView):
    template_name='core/login.html'
    success_url='/'


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')

class customerregistration(View):
    def get(self,request):
        form=userresi()
        return render(request, 'core/registration.html',{'form':form})
    def post(self,request):
        form=userresi(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile details updated.')
            return render(request, 'core/registration.html',{'form':form})
        return render(request, 'core/registration.html',{'form':form})
        