# from django.shortcuts import render
# #render() is a shortcut function that combines a template (HTML) with data and returns the final web page to the user's browser.
# #shortcuts → A module inside Django that provides helper functions.

# from django.http import HttpResponse
# #HttpResponse is used to send a response directly from the Django view to the user's browser.

# # Create your views here.
# # Django views are Python functions that take http requests and return http response, like HTML documents.


# def members(request):
#     return HttpResponse("Hello, I am a member of this project.")
# # This is a simple example on how to send a response back to the browser.




from django.shortcuts import render

def home(request):
    return render(request,'employees/home.html')
