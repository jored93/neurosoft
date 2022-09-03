from turtle import mode
from djongo import models

class GraphEcg(models.Model):
    _id = models.ObjectIdField()
    filename = models.CharField(max_length=100)
    url = models.CharField(max_length=100)

    class Meta:
        db_table = 'graphECG'
