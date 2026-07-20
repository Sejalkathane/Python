# from django.contrib import admin
# # django.contrib.admin is Django's built-in Admin Panel.
# # admin lets you access the Django admin website
# from django.urls import include, path
# # path → Used to create URL routes.
# # include → Used to include URLs from another file.

# # Think of include() as saying:

# # "Instead of writing all URLs here, go and look in another urls.py file."

# urlpatterns = [
#     path('', include('members.urls')),
#     path('admin/', admin.site.urls),  #If someone visits: http://127.0.0.1:8000/admin/ Django opens the built-in Admin Panel.
# ]
# # urlpatterns is a special list where Django stores all the URL routes for the project.
# # '' (empty string) means the root URL (home page).


# # When someone visits the home page, Django says:
# # "Go to members/urls.py and check the URL patterns there."
# # The include('members.urls') tells Django to load the URLs from:

# # members/
# # │
# ├── urls.py




# from django.urls import path
# from . import views

# urlpatterns = [
#     path('', views.home, name='home'),
# ]


from django.contrib import admin
from django.urls import path, include

urlpatterns = [

path('admin/', admin.site.urls),

path('', include('employees.urls')),

]