from django.shortcuts import render, redirect

from apps.pages.forms import ContactForm


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
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.result = 1313
            form.save()
            return redirect('pages:contact')
        else:
            errors = []
            for key, value in form.errors.items():
                for error in value:
                    errors.append(error)
            context = {
                "errors": errors
            }
            return render(request, 'pages/contact.html', context)

    else:
        return render(request, 'pages/contact.html')