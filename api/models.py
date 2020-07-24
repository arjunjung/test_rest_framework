from django.db import models

class ToyModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=50,default='Something',blank=False)
    description = models.TextField(max_length=255,default='Something',blank=False)
    category = models.CharField(max_length=50, default='Something',blank=False)
    price = models.PositiveIntegerField(default=100,blank=False)
    was_included_in_home = models.BooleanField(default=False)

    class Meta:
        ordering = ('name',)
