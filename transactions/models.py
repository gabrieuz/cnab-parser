from django.db import models


class Transaction(models.Model):
    type = models.IntegerField()
    date = models.DateField()
    time = models.TimeField()
    value = models.DecimalField(max_digits=10, decimal_places=2)
    cpf = models.CharField(max_length=11)
    card = models.CharField(max_length=12)
    owner = models.CharField(max_length=14)
    store = models.CharField(max_length=19)

    def __repr__(self) -> str:
        return f"{self.type} {self.date} {self.value} {self.cpf} {self.card} {self.time} {self.owner} {self.store}"
    