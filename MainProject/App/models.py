from django.db import models

# Create your models here.
class Reports(models.Model):
    
    area = models.IntegerField(default=0,blank=False, null=False)
    area_name = models.CharField(max_length=100,blank=False, null=False)
    crime_type = models.IntegerField(default=0,blank=False, null=False)
    crime_type_name = models.CharField(max_length=100,blank=False, null=False)
    victim_sex = models.IntegerField(default=0,blank=False, null=False)
    victim_sex_label = models.CharField(max_length=100,blank=False, null=False)
    victim_descent = models.IntegerField(default=0,blank=False, null=False)
    victim_descent_label = models.CharField(max_length=100,blank=False, null=False)
    weapon_used = models.IntegerField(default=0,blank=False, null=False)
    weapon_used_label = models.CharField(max_length=100,blank=False, null=False)
    time_of_crime = models.IntegerField(default=0,blank=False, null=False)
    reported_delay = models.IntegerField(default=0,blank=False, null=False)
    days_after_reported = models.IntegerField(default=0,blank=False, null=False)
    prediction = models.IntegerField(default=0,blank=False, null=False)
    confidence = models.FloatField(default=0,blank=False, null=False)

    class Meta :
        managed = True
        db_table = 'reports'
    def __str__(self):
        return str(self.id)