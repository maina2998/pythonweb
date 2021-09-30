from django.db import models

class Trainer(models.Model):
    first_name = models.CharField(max_length=12,null=True)
    last_name = models.CharField(max_length=12,null=True)
    age = models.PositiveSmallIntegerField(null=True)
    phone_number = models.PositiveIntegerField(null=True)
    email =models.EmailField(null=True)
    profile_photo = models.ImageField(upload_to ="images/")
  
    LANGUAGE_CHOICES=(
        (u"ki", u"Kinyarwanda"),
        (u"E", u"English"),
        (u"K", u"kiswahili"),

        )

    languages =models.CharField(max_length=6,choices=LANGUAGE_CHOICES, null=True)

    GENDER_CHOICES=(
        (u"F", u"Female"),
        (u"M",u"Male"),
        (u"O",u"Others")
    )
    
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    training_day = models.CharField(max_length=12,null=True)
    date_joined = models.DateField(null=True)
    bio = models.TextField(null=True)
    contract = models.FileField(null=True)
    date_hired = models.DateField(null=True)


    def full_name(self):
        return f"{self.first_name} {self.last_name}"
 

