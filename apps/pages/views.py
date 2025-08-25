from django.shortcuts import render

def home_page_view(request):
    return render(request, 'home.html')

def n404_view(request):
    return render(request, 'pages/404.html')

def about_view(request):
    return render(request, 'pages/about.html')

def coming_soon_view(request):
    return render(request, 'pages/coming-soon.html')

def faq_view(request):
    return render(request, 'pages/faq.html')

def contact_view(request):
    return render(request, 'pages/contact.html')