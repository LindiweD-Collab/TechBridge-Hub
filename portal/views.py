
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm, CommunicationForm 
from .models import Client 
from .models import Project
from django.shortcuts import render, redirect, get_object_or_404

def home(request):
   
    context = {}
    return render(request, 'portal/home.html', context)

def services(request):
    """
    This view handles the logic for the services page.
    """
    service_list = [
         {
            'name': 'Expert IT Support', 
            'desc': 'Responsive remote IT support, troubleshooting, maintenance, and user assistance for SMEs. Keep your systems running smoothly.'
        },
        {
            'name': 'Cybersecurity Training', 
            'desc': 'Practical training for employees to identify threats, protect data, and adhere to best practices (including POPIA awareness).'
        },
        {
            'name': 'Cloud Migration Strategy', 
            'desc': 'Expert guidance on planning and executing your move to cloud platforms like AWS, Azure, or Google Cloud for scalability and flexibility.'
        },
        {
            'name': 'Robotic Process Automation (RPA)', 
            'desc': 'Automate repetitive tasks, boost efficiency, and reduce errors with custom RPA solutions and training. Free up your team for higher-value work.'
        },
        {
            'name': 'Digital Marketing',
            'desc': 'Comprehensive digital marketing strategies including SEO, content marketing, and social media management to grow your online presence and attract new customers.'
        },
        {
            'name': 'Affiliate Marketing',
            'desc': 'Launch and manage a powerful affiliate program to drive revenue through strategic partnerships and performance-based marketing.'
        },
    ]
    context = {'services': service_list}
    return render(request, 'portal/services.html', context)

@login_required
def dashboard(request):
    projects = []
    if request.user.client:
        projects = Project.objects.filter(client=request.user.client)

    context = {
        'projects': projects
    }
    return render(request, 'portal/dashboard.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            company_name = form.cleaned_data['company_name']
            client, created = Client.objects.get_or_create(name=company_name)
            user.client = client
            user.save()

            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()

   

    context = {'form': form}
    return render(request, 'registration/signup.html', context)

@login_required
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.user.client != project.client:
        from django.http import Http404
        raise Http404

    if request.method == 'POST':
        form = CommunicationForm(request.POST)
        if form.is_valid():
            new_communication = form.save(commit=False)
            new_communication.project = project
            new_communication.author = request.user
            new_communication.save()

            return redirect('project_detail', pk=project.pk)
    else:
  
        form = CommunicationForm()


    context = {
        'project': project,
        'form': form, 
    }
    return render(request, 'portal/project_detail.html', context)