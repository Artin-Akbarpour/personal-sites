from django.shortcuts import render
from . import models
from resume_app.models import education, experience, skill, Software_skills
from service_app.models import service
from customer_app.models import customer
from contactus_app.models import contact
# Create your views here.
def home(request):
    persons = models.person.objects.first()
    educations = education.objects.all()
    experiences = experience.objects.all()
    skills = skill.objects.all()
    software_skills = Software_skills.objects.all()
    services = service.objects.all()
    customers = customer.objects.all()

    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    subject = request.POST.get('subject')
    message = request.POST.get('message')
    if request.method == 'POST':
        print('skdjflsagjslafgkaslfkgkf')
        contact.objects.create(name=name, email=email, phone=phone, subject=subject, message=message)
    return render(request, 'home_app/index-dark.html', {'persons': persons, 'educations': educations,
                                                        'experiences': experiences, 'skills': skills,
                                                        'software_skills': software_skills,
                                                        'services': services,
                                                        'customers': customers})