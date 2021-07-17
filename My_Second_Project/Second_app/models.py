from django.db import models
from django.urls import reverse

# Create your models here.

class Musician(models.Model):
    #id = models.AutoField(Primary_key =True)
    first_name = models.CharField(max_length=40, blank=True)
    last_name = models.CharField(max_length=40)
    instrument = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name + " " + self.last_name + " " +self.instrument


    def get_absolute_url(self):
        return reverse("Second_app:musician_details", kwargs={'pk':self.pk})


class Album(models.Model):
    #id = models.AutoField(Primary_key =True)
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='album_list')
    name = models.CharField(max_length=50)
    release_date = models.DateField()

    #<select>
    #<option value='1'>Worst</option>
    rating = (
    (1, "Worst"),
    (2, "Bad"),
    (3, "Not Bad"),
    (4, "Good"),
    (5, "Exellent!"),
    )

    num_stars = models.IntegerField(choices=rating)



    def __str__(self):
        return self.name + ", Rating" + str(self.num_stars)
