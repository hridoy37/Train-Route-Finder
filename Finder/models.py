from django.db import models

class Train(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Station(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
class TrainRoute(models.Model):
    train = models.ForeignKey(Train, on_delete=models.CASCADE)
    from_station = models.ForeignKey(Station, related_name='from_station', on_delete=models.CASCADE)
    to_station = models.ForeignKey(Station, related_name='to_station', on_delete=models.CASCADE)
    fare = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.train.name






