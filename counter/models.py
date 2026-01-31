# models.py
from django.db import models

class Counter(models.Model):
    BRANCH_CHOICES = [
        ("mota_varachha", "Mota Varachha"),
        ("hirabaug", "Hirabaug"),
        ("abrama", "Abrama"),
    ]

    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES, unique=True)
    value = models.IntegerField(default=0)

    def __str__(self):
        return self.branch
