from django.db import models

class Client(models.Model):
    firstname = models.CharField(max_length=40)
    lastname = models.CharField(max_length=30)
    address = models.CharField(max_length=50)

    def __str__(self):
        return f"\nfirstname: {self.firstname} \nlastname: {self.lastname} \naddress: {self.address}"

class Account(models.Model):
    code = models.IntegerField(primary_key=True)
    balance = models.FloatField(default=0.0)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='accounts')

    def __str__(self):
        return f"\ncode:{self.code} \nbalance:{self.balance} \n    client:{self.client}"



