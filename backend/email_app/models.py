from django.db import models

# Create your models here.
class ResetPassword(models.Model):
    email = models.CharField(max_length=200, null=True)
    token = models.CharField(max_length=255, null=True)
    slug = models.SlugField(max_length=255)

    def __str__(self):
        return self.token
    #creates users personalized link, that they visit and have a enter new password view in Front-End.
    def get_absolute_url(self):
        return f'/{self.token}/'