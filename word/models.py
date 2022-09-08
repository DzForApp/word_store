from django.contrib import admin
from django.db import models

# Create your models here.
class Kalima(models.Model):
    kalima_text = models.CharField(max_length=200)
    ar_description = models.TextField(default="شرح عربية")
    kalima_Fr = models.CharField(max_length=200)
    fr_description = models.TextField(default="Description Française")
    kalima_En = models.CharField(max_length=200)
    en_description = models.TextField(default="English description")
    publishe_date = models.DateField('Date Published')

    def __str__(self) -> str:
        return self.kalima_text

class kalimaModel(admin.ModelAdmin):
    list_display = ('kalima_text','kalima_Fr','kalima_En')
    search_fields=('kalima_text','kalima_Fr','kalima_En')
    action = None
    pass
 