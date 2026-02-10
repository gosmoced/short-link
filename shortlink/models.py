from django.db import models
from django.contrib.auth.models import User

class Link(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=20, unique=True)
    url = models.URLField()
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Click(models.Model):
    link = models.ForeignKey(Link, on_delete=models.CASCADE, related_name='click_history')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.CharField(max_length=500, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Клик по {self.link.title} с {self.ip_address}"
