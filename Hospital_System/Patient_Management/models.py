from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PhysicalAppointment(models.Model):
    SERVICE_CHOICES = [
        ('Dentist', 'Dentist'),
        ('Surgery', 'Surgery'),
        ('Consultation', 'Consultation'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone_no = models.CharField(max_length=15)
    service_needed = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    appointment_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.service_needed} on {self.appointment_date}"

class EmergencyCare(models.Model):
    patient_name = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    condition_description = models.TextField()
    priority_level = models.CharField(max_length=255,choices = [

        ('High', 'High'),
        ('Medium', 'Medium'),
        ('Low', 'Low'),
    ])
    location = models.CharField(max_length=25, default='')
    timestamp = models.DateTimeField(auto_now_add=True)  # Automatically record the time of entry

    def __str__(self):
        return f"{self.patient_name} - {self.condition_description} - {self.location}"
    
class online_doctor(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    service_type = models.CharField(max_length=30,choices=[
                ('gaenocology','gaenocology'),
                ('consultation','consultation'),
                ('patient_review','patient_review'),

    ])
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return super().__str__()

class Blog(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='blog_images/')  # Stores images in /media/blog_images/

    def __str__(self):
        return self.title
    


class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment_type = models.CharField(max_length=100)
    appointment_time = models.DateTimeField()
    booked_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.user.username} - {self.appointment_type} - {self.appointment_time}"