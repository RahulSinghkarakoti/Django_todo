# from django.http import HttpResponse
# from django.shortcuts import render

# def home(request):
#     return render(request,'index.html',context={'h':'hh'})


# def add_todo(request):
#   if request.method == 'POST':
#      name=request.POST.get("todo")
#      return HttpResponse(f"Name: {name}")
#   return render(request,'addtodo.html',context={'h':'hh'})

# def contact(request):
#     return HttpResponse("<h1>Welcome to Chai's Django Project: Contact page</h1>")