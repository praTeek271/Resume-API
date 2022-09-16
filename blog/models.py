from django.db import models

# Create your models here.
state_options = ((('Uttar Pradesh', 'uttar pradesh'), ('Delhi', 'delhi'), ('Himachal Pradesh', 'himachal pradesh'),))
gender_options = ((('Male', 'Male'), ('Female', 'Female'),))


class user_data(models.Model):
    username = models.CharField(max_length=255, unique=True)
    DOB = models.DateField(auto_now=False, auto_now_add=False)
    email = models.EmailField(max_length=254)
    state = models.CharField(choices=state_options, max_length=225)
    gender = models.CharField(choices=gender_options, max_length=255)
    resume = models.FileField(upload_to="resumes", blank=True)
    selected = models.BooleanField(default=False)

    def __str__(self):
        return self.username
