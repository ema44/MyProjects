from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

class YouthCenter(models.Model):
  WORKED = 'WR'
  DESTROYED = 'DS'
  OUT_OF_SERVICE = 'OS'
  NEWLY_BUILD = 'NB'
  Status_Center_CHOICES = (
  (WORKED, 'worked'),
  (DESTROYED, 'destroyed'),
  (OUT_OF_SERVICE, 'out_of_service'),
  (NEWLY_BUILD, 'newly_build'),)
  center_name=models.CharField(max_length=100)
  place_of_center=models.CharField(max_length=100)
  stsus_of_center=models.CharField(max_length=100,choices=Status_Center_CHOICES,default=WORKED)
  user=models.ForeignKey(User, on_delete=models.CASCADE,related_name='kiros')
  file=models.FileField(default='default.jpg', upload_to='profile_pics')
  center_created=models.DateTimeField(auto_now_add=True)
  description=models.TextField()
  center_total_youth=models.BigIntegerField()



  def __str__(self):
    return self.center_name
  def get_absolute_url(self):
        return reverse('detail-center', kwargs={'pk': self.pk})




class Profile(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.FileField(upload_to = 'pictures')

   class Meta:
      db_table = "profile"