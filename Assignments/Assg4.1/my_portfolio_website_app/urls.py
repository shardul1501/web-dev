#<--- My Portfolio Website - Imported Packages List ----

#------Django Internal Packages-----
from django.contrib import admin
from django.urls import path
#/------Django Internal Packages-----

#<-------- importing view from my_portfolio_website_app -------------
from my_portfolio_website_app import views
#</-------- importing view from my_portfolio_website_app -------------

#</--- My Portfolio Website - Imported Packages List ----

#App Name in the project
app_name='my_portfolio_website_app'



#<------------------------ Project URLS --------------------------------------

urlpatterns = [

#<------ Authentication URLS--------------------

    #Url for user_login view
    path('login',views.user_login,name='login'),

    #Urls for register view
    path('register',views.register,name='register'),

    #Url for logout view
    path('logout',views.log_out,name='logout'),

#<------ Authentication URLS--------------------


    #Url for about view 
    path('',views.about,name='about'),

    #Url for portflio view
    path('portfolio',views.portfolio,name='portfolio'),

    #Url for contact view
    path('contact',views.contact,name='contact'),

    #Url for Contcat form submit view
    path('contact_form_submit',views.contact_form_submit,name='contact_form_submit'),

    #Url for all_data view
    path('all_data',views.all_data,name='all_data'),

    #Url for users view
    path('users',views.users,name='users'),

#</------------------------ Project URLS -------------------------------------

]