from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Skill, Project, ContactMessage
from .utils import send_telegram_notification



def home(request):
    return render(request, 'core/index.html')



def contact_submit(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        if name and email and message_text:
            ContactMessage.objects.create(name=name, email=email, message=message_text)
            send_telegram_notification(name, email, message_text)
            messages.success(request, "Your message has been sent successfully!")
        
        
        return redirect(request.META.get('HTTP_REFERER', 'home'))
    return redirect('home')



def projects(request):
    projects_list = Project.objects.all()
    return render(request, 'core/projects.html', {'projects': projects_list})



def skills(request):
    skills_list = Skill.objects.all()
    return render(request, 'core/skills.html', {'skills': skills_list})



def links(request):
    return render(request, 'core/links.html')