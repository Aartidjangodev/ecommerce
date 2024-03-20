from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages
# Create your views here.
def adminLogin(request):
     return render(request, "adminLogin.html")
def userLogin(request):
    if request.method == 'POST':
        vuname = request.POST.get('uname')
        vpwd = request.POST.get('pwd')
        # it verify the username and passwrd are same or not
        myuser = auth.authenticate(username=vuname, password=vpwd)

        if myuser is not None:  # it check texbox field they are not empty or duplicate
            auth.login(request, myuser)  # login is predefined django function
            return redirect('/dashboard')
        else:
            messages.success(request, 'Invalid username and password')
            return redirect('/adminLogin')
    else:
        return render(request, 'adminLogin.html')


def userLogout(request):
    auth.logout(request)
    return redirect('/adminLogin')

def dashboard(request):
    return render(request, "dashboard.html")



# def loadRegister(request):
#     if(request.method=='POST'):
#         vfname=request.POST.get('fname') # get the values from the text
#         vlname = request.POST.get('lname')
#         vemail = request.POST.get('email')
#         vuname=request.POST.get('uname')
#         vpwd=request.POST.get('pwd')
#         vcpwd = request.POST.get('cpwd')
#
#
#         # insert the textbox data in auth table
#         if(vpwd==vcpwd):
#             if(User.objects.filter(username=vuname)):
#                 messages.success(request,'Username already exist...!!')
#                 return redirect('/loadRegister')
#             elif(User.objects.filter(email=vemail)):
#                 messages.success(request,'email already exist...!!')
#                 return redirect('/loadRegister')
#             else:
#                 newUser=User.objects.create_user(first_name=vfname,last_name=vlname,email=vemail,username=vuname,password=vpwd)
#                 newUser.save()
#                 messages.success(request,'Register Succesfully')
#                 return redirect('/loadRegister')
#         else:
#            messages.success(request, 'Password did not match!!!')
#
#         return redirect('/loadRegister')
#     else:
#
#
#        return render(request,'register.html')