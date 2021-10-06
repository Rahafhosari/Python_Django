from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.contrib.auth import authenticate, login

def index(request):
    return HttpResponse("Learning Class based views")

#________ Using Django Forms ________#
def indexForm(request):
    form = RegisterForm()
    context = { "regForm": form }
    return render(request, "index.html", context)

def register(request):
    if request.method == "POST":
        bound_form = RegisterForm(request.POST)
        print(bound_form.is_valid()) # True or False, based on the validations that were set!
        print(bound_form.errors) # Any errors in this form as a dictionary
        return redirect('form')

# def register(request):
#     if request.method == "POST":
#         bound_form = RegisterForm(request.POST)
#         if bound_form.is_valid():
#             new_user = bound_form.save(commit = False)
#             print(bound_form.is_valid()) # True or False, based on the validations that were set!
#             new_user.save()
#             print(new_user)
#         print(bound_form.errors) # Any errors in this form as a dictionary
#     return redirect('form')
