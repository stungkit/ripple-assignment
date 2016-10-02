from __future__ import unicode_literals

from django.db import models

# Create your models here.
class UserIP(models.Model):
	ip_address = models.CharField(max_length=200)
	datetime = models.DateTimeField()
	frequency = models.PositiveIntegerField()

	class Meta:
		db_table = "user_ip"
		