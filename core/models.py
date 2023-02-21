from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.

class Agency(models.Model):
    """Model Agency"""
    id = models.AutoField(primary_key=True, verbose_name="id")
    name = models.CharField(max_length=255, verbose_name="Name")
    location = models.TextField(verbose_name="Location")

    class Meta:
        ordering = ['-name']
        verbose_name = 'Agency'
        verbose_name_plural = 'Agencies'
    
    def __str__(self):
        return self.name

class Officer(models.Model):
    """Model Officer"""
    id = models.AutoField(primary_key=True, verbose_name="id")
    agency = models.ForeignKey(Agency, on_delete=models.DO_NOTHING, verbose_name="Agency", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="User")
    
    class Meta:
        ordering = ['-user']
        verbose_name = 'officer'
        verbose_name_plural = 'Officers'
    
    def __str__(self):
        return self.user.first_name + ' ' + self.user.last_name

class Citation(models.Model):
    """Model Citation"""

    # General info citation
    id = models.AutoField(primary_key=True, verbose_name="id")
    no_citation = models.CharField(max_length=255, verbose_name="No. Citation")
    violation_date = models.DateField(verbose_name="Violation Date")
    vilation_time = models.TimeField(verbose_name="Violation Time")
    route = models.CharField(max_length=255, verbose_name="Route")
    county = models.CharField(max_length=255, verbose_name="County")
    city = models.CharField(max_length=255, verbose_name="City")

    # Contact passenger
    vehicle_type_passenger = models.CharField(max_length=100, verbose_name="Vehicle Type Passenger")
    oln_state_passenger = models.CharField(max_length=100, verbose_name="OLN State Passenger")
    oln_passenger = models.CharField(max_length=100, verbose_name="OLN Passenger")
    class_oln_passenger = models.CharField(max_length=100, verbose_name="Class OLN Passenger")
    cdl_passenger = models.CharField(max_length=100, verbose_name="CDL Passenger")
    name_passenger = models.CharField(max_length=100, verbose_name="Name Passenger")
    gender_passenger = models.CharField(max_length=100, verbose_name="Gender Passenger")
    hair_passenger = models.CharField(max_length=100, verbose_name="Hair Passenger")
    eyes_passenger = models.CharField(max_length=100, verbose_name="Eyes Passenger")
    height_passenger = models.DecimalField(max_digits=8, decimal_places=2, verbose_name="Height Passenger")
    address_passenger = models.TextField(verbose_name="Address Passenger")
    city_passenger = models.CharField(max_length=150, verbose_name="City Passenger")
    state_passenger = models.CharField(max_length=150, verbose_name="State Passenger")
    phone_passenger = models.CharField(max_length=150, verbose_name="Phone Passenger")
    email_passenger = models.EmailField(max_length=254, verbose_name="Email Passenger")

    # Vehicle Type: Passenger car
    vin_car = models.CharField(max_length=255, verbose_name="Vin Car")
    color_car = models.CharField(max_length=255, verbose_name="Color Car")
    year_car = models.CharField(max_length=255, verbose_name="Year Car")
    make_car = models.CharField(max_length=255, verbose_name="Make Car")
    model_car = models.CharField(max_length=255, verbose_name="Model Car")

    # Factors
    crash = models.BooleanField(verbose_name="Crash")
    passenger = models.BooleanField(verbose_name="Passenger")
    spanish_speaker = models.BooleanField(verbose_name="Spanish Speaker")
    in_car_video = models.BooleanField(verbose_name="In Car Video")
    body_camera = models.BooleanField(verbose_name="Body Camera")
    school_zone = models.BooleanField(verbose_name="School Zone")
    cosntruction_zone = models.BooleanField(verbose_name="Cosntruction Zone")
    workers_present = models.BooleanField(verbose_name="Workers Present")

    # violations
    issued_by = models.ForeignKey(Officer, on_delete=models.DO_NOTHING, verbose_name="Issued by")
    issued_date = models.DateField(verbose_name="Issued Date")
    badge = models.CharField(max_length=100, verbose_name="Badge")
    issued_time = models.TimeField(verbose_name="Issued Time")

    class Meta:
        ordering = ['-issued_date']
        verbose_name = 'Citation'
        verbose_name_plural = 'Citations'
    
    def __str__(self):
        return self.no_citation + ' ' + self.name_passenger

# Signals 

@receiver(post_save, sender=User)
def ensure_officer_exist(sender, instance, **kwargs):
    """
    Signal that allows you to automate the creation of an officer profile as soon as a user is created.
    """
    if kwargs.get('created', False):
        Officer.objects.get_or_create(user=instance)
        print("A user and his official link profile have just been created.")
