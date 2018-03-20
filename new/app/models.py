from django.contrib.auth.models import Permission, User
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse

COLOR_CHOICES = (
    ('morning','Morning'),
    ('day', 'Day'),
    ('evening','Evening'),
    ('night','Night'),
)

COLOR = (
    ('jan','January'),
    ('feb', 'February'),
    ('mar','March'),
    ('apr','April'),
    ('may','May'),
    ('jun', 'June'),
    ('jul','July'),
    ('aug','August'),
    ('sept','September'),
    ('oct', 'October'),
    ('nov','November'),
    ('dec','Decemeber'),

)


class state(models.Model):
    state_name = models.CharField(max_length=20)
    #description = models.CharField(max_length=500)
    def __str__(self):
        return self.state_name


class city(models.Model):
    state_name = models.ForeignKey(state, on_delete=models.CASCADE)
    city_name = models.CharField(max_length=20)
    #description = models.CharField(max_length=500)
    
    def __str__(self):
        return self.city_name

class place(models.Model):
    city_name = models.ForeignKey(city, on_delete=models.CASCADE)
    place_name = models.CharField(max_length=20)
    description = models.CharField(max_length=5000)
    hotel=models.CharField(max_length=1000, default="")
    addres=models.CharField(max_length=1000, default="")
    phone=models.CharField(max_length=11, default="")
    open=models.CharField(max_length=11, default="")
    close=models.CharField(max_length=11, default="")
    def __str__(self):
        return self.place_name

class rating(models.Model):
    primary = models.AutoField(max_length=500, primary_key=True)
    place_name = models.ForeignKey(place, on_delete=models.CASCADE)
    total=models.PositiveIntegerField(default=1)
    art=models.IntegerField( default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    adventure=models.IntegerField( default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    religious=models.IntegerField( default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    historical=models.IntegerField( default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    romantic=models.IntegerField( default=1, validators=[MaxValueValidator(10), MinValueValidator(1)])
    budget=models.IntegerField(default=300)
    budget_for=models.IntegerField(default=300)
    link=models.CharField(max_length=1000, default="")
    coord=models.CharField(max_length=1000, default="")
    time=models.IntegerField(default=2,validators=[MaxValueValidator(24), MinValueValidator(1)])
    best_time=models.CharField(max_length=8, choices=COLOR_CHOICES, default='day')
    best_month=models.CharField(max_length=12, choices=COLOR, default='jan')
    best_month2=models.CharField(max_length=12, choices=COLOR, default='dec')
    def __str__(self):
        return str(self.place_name) + str('-Ratings')

class support(models.Model):
    question=models.CharField(max_length=1000, default="")
    answer=models.CharField(max_length=1000, default="")