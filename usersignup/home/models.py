from django.db import models

class email(models.Model):
    email_text = models.CharField(max_length= 100)
    username_text = models.CharField(max_length=100)

    def __str__(self):
        return self.email_text
        


class psw(models.Model):
    email = models.ForeignKey(email,on_delete=models.CASCADE)
    password = models.CharField(max_length=5)

    def __str__(self):
        return self.password




