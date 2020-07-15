"""my_portfolio_website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

#<--- My Portfolio Website - Imported Packages List ----
from django.contrib import admin
from django.urls import path,include
#</--- My Portfolio Website - Imported Packages List ----



#Admin Site Header Name
admin.site.site_header = "My Portfolio Admin"
#Admin site Title
admin.site.site_title = "My Portfolio Admin Portal"
#Admin site Index title
admin.site.index_title = "Welcome to My Portfolio Portal"





#---My Portfolio Website Admin and Data Management URL List ---
urlpatterns = [
    #Url for Admin Site
    path('admin/', admin.site.urls),

    #Url for my_portfolio_website_app configuration
    path('', include('my_portfolio_website_app.urls')),
]

#/---My Portfolio Website Admin and Data Management URL List ---
