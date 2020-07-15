#<--- My Portfolio Website - Imported Packages List ----


#<------Django Internal Packages-----
from django.shortcuts import render,HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
#</------Django Internal Packages-----

#<------ External Installed Packages -----

#</------ External Installed Packages -----


#<------ My Portfolio Website Internal Project Packages -----
from my_portfolio_website_app.models import ContactForm,CustomUser
#</------ My Portfolio Website Internal Project Packages -----


#</--- My Portfolio Website - Imported Packages List ----


#Create your views here.

#<---------------------- Authentication Views --------------------------------------

#User Login View 
def user_login(request):
    """Logs in a user if the credentials are valid and the user is active,
    else redirects to the same page and displays an error message."""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('my_portfolio_website_app:all_data'))
        else:
            return render(request,'my_portfolio_website_app/registration/login.html',{'error_message': 'Username or Password Incorrect!'})
    else:
        return render(request,'my_portfolio_website_app/registration/login.html')



#User Register view
def register(request):
    """Registers a user"""
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password != confirm_password:
            return render(request,'my_portfolio_website_app/registration/register.html',{'error_message':'Password Not Match!'})
        if CustomUser.objects.filter(username=username).exists():
            return render(request,'my_portfolio_website_app/registration/register.html',{'error_message':'Username already exist!'})
        else:
            user = CustomUser.objects.create(username=username, password= make_password(password),role=2)
            login(request,user)
            return HttpResponseRedirect(reverse('my_portfolio_website_app:all_data'))
    else:
        return render(request,'my_portfolio_website_app/registration/register.html')


#Logout View
def log_out(request):
    """User get logout from the session"""
    logout(request)
    return HttpResponseRedirect(reverse('my_portfolio_website_app:login'))


#</---------------------- Authentication Views --------------------------------------


#<-------------------------- Page Render view --------------------------------------

#about page view
def about(request):
    """This view render about.html page
    parameters: HttpRequest
    return: nothing  """
    return render(request,'my_portfolio_website_app/about.html')


#Portfolio Page view
def portfolio(request):
    """This view render portfolio.html page
    parameters: HttpRequest
    return: nothing  """
    return render(request,'my_portfolio_website_app/portfolio.html')


#Contact Page View
def contact(request):
    """This view render contact.html page
    parameters: HttpRequest
    return: nothing  """
    return render(request,'my_portfolio_website_app/contact.html')

#Contact Form Data Submit form view
def contact_form_submit(request):
    """This view take post method and submit form details 
        by creating ContactForm Model object
    parameters: HttpRequest
    return: if form data submit successfully then 
            HttpResponseRedirect to page contact.html  """
    if request.method == "POST":
        full_name = request.POST['full_name']
        email_id = request.POST['email_id']
        contact_number = request.POST['contact_number']
        message = request.POST['message']
        ContactForm.objects.create(full_name=full_name,
                                   email_id=email_id,
                                   contact_number=contact_number,
                                   message=message
                                   )
    return HttpResponseRedirect(reverse('my_portfolio_website_app:contact'))



#All Data View
@login_required(login_url='/login')
def all_data(request):
    """This view render all_data.html page
    parameters: HttpRequest
    return: contact_data  """
    contact_data = ContactForm.objects.all()
    data = {'contact_data':contact_data}
    return render(request,'my_portfolio_website_app/all_data.html',data)


#User Data View
@login_required(login_url='/login')
def users(request):
    """This view render users.html page
    parameters: HttpRequest
    return: users  """
    users = CustomUser.objects.all()
    data = {'users':users}
    return render(request,'my_portfolio_website_app/users.html',data)

#</-------------------------- Page Render view --------------------------------------
