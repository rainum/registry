from django.db import models


class BaseModel(models.Model):
    add_date = models.DateTimeField(auto_now_add=True, db_index=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta(object):
        abstract = True
        ordering = ['-add_date']


class Doctor(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)

    monday_start = models.DateTimeField(null=True, blank=True)
    monday_end = models.DateTimeField(null=True, blank=True)
    monday_cabinet = models.CharField(max_length=20, null=True, blank=True)

    tuesday_start = models.DateTimeField(null=True, blank=True)
    tuesday_end = models.DateTimeField(null=True, blank=True)
    tuesday_cabinet = models.CharField(max_length=20, null=True, blank=True)

    wednesday_start = models.DateTimeField(null=True, blank=True)
    wednesday_end = models.DateTimeField(null=True, blank=True)
    wednesday_cabinet = models.CharField(max_length=20, null=True, blank=True)

    thursday_start = models.DateTimeField(null=True, blank=True)
    thursday_end = models.DateTimeField(null=True, blank=True)
    thursday_cabinet = models.CharField(max_length=20, null=True, blank=True)

    friday_start = models.DateTimeField(null=True, blank=True)
    friday_end = models.DateTimeField(null=True, blank=True)
    friday_cabinet = models.CharField(max_length=20, null=True, blank=True)

    saturday_start = models.DateTimeField(null=True, blank=True)
    saturday_end = models.DateTimeField(null=True, blank=True)
    saturday_cabinet = models.CharField(max_length=20, null=True, blank=True)

    sunday_start = models.DateTimeField(null=True, blank=True)
    sunday_end = models.DateTimeField(null=True, blank=True)
    sunday_cabinet = models.CharField(max_length=20, null=True, blank=True)

    duration = models.DurationField(null=True, blank=True)

    specialization = models.CharField(max_length=100)

    def __str__(self):
        parts = []
        if self.first_name:
            parts.append(self.first_name)
        if self.last_name:
            parts.append(self.last_name)
        if self.second_name:
            parts.append(self.second_name)
        return " ".join(parts)


class Address(BaseModel):
    street = models.CharField(max_length=100)
    house = models.CharField(max_length=20)
    doctor = models.ForeignKey(Doctor)


class Talon(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)

    doctor = models.ForeignKey(Doctor)
    address = models.ForeignKey(Address)

    date_of_receipt = models.DateTimeField()

