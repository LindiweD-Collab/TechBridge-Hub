# portal/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser




class Client(models.Model):
    """
    Represents a client business or organization.
    Each client can have multiple users (contacts) and multiple projects.
    """
    name = models.CharField(max_length=255, help_text="The official name of the client organization.")
    contact_person_name = models.CharField(max_length=255, blank=True)
    contact_email = models.EmailField(max_length=255, unique=True, help_text="Primary email for the client.")
    contact_phone = models.CharField(max_length=20, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class User(AbstractUser):
    """
    Custom User Model
    Represents both internal team members and client users.
    """
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True, blank=True, related_name='users')
    pass

class Project(models.Model):
    """
    Represents a single project for a client.
    """
    STATUS_CHOICES = [
        ('PLANNING', 'Planning'),
        ('IN_PROGRESS', 'In Progress'),
        ('COMPLETED', 'Completed'),
        ('ON_HOLD', 'On Hold'),
    ]

    title = models.CharField(max_length=255, help_text="The title of the project.")
    description = models.TextField(blank=True, help_text="A detailed description of the project scope.")
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='projects')
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PLANNING')
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    assigned_to = models.ManyToManyField(User, related_name='projects', blank=True)

    def __str__(self):
        return f"{self.title} ({self.client.name})"

    class Meta:
        ordering = ['-start_date']

class Task(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['is_completed', 'due_date']


class Communication(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='communications')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages')
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message by {self.author.username} on {self.timestamp.strftime('%Y-%m-%d')}"

    class Meta:
        ordering = ['-timestamp']