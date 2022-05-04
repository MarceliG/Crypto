from django.db import models


class Status(models.Model):
    STATUS = {
        (0, "BUY"),
        (1, "SELL"),
        (2, "EXCHANGE"),
    }
    status = models.PositiveSmallIntegerField(choices=STATUS)


class Wallet(models.Model):
    date = models.DateField(null=True, blank=True)
    status = models.OneToOneField(to=Status, on_delete=models.CASCADE)
    value = models.PositiveSmallIntegerField()

    def status_and_date(self):
        return "{}({})".format(str(self.status), str(self.date))

    def __str__(self):
        return self.status_and_date()
