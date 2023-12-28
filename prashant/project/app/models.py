from django.db import models

class User(models.Model):
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=50)  # Note: In a real-world scenario, you should use Django's built-in User model and its password hashing mechanism

    def __str__(self):
        return self.username

class LoginAttempt(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    success = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.username} - {'Successful' if self.success else 'Failed'}"
