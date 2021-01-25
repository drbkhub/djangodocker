from django.db import models

# Create your models here.


class HistoryDeals(models.Model):
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.id}. {self.date}'



class Deal(models.Model):
    deal = models.ForeignKey(HistoryDeals, on_delete=models.CASCADE)

    customer = models.CharField(max_length=20)
    item = models.CharField(max_length=20)
    total = models.IntegerField()
    quantity = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self):
        return f'{self.customer} - deal {self.deal.id}'
