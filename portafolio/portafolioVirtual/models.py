from django.db import models

class Company(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Ratio(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Date1(models.Model) :
    name =  models.DateTimeField()

    def __str__(self) :
        return self.name


class Historic(models.Model):
    date = models.ForeignKey(Date1, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits =20, decimal_places = 4,  null=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)




    def __str__(self) :
        return self.name
