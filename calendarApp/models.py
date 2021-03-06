from django.db import models

# Create your models here.


class AppUser(models.Model):
    id = models.AutoField(primary_key=True, db_column='ID')
    login = models.CharField(max_length=50, db_column='LOGIN')
    password = models.CharField(max_length=50, db_column='PASSWORD')
    email = models.CharField(max_length=50, db_column='EMAIL')

    objects: models.Manager

    def __str__(self):
        return self.login

    class Meta:
        app_label = "calendarApp"
        db_table = "USER"
