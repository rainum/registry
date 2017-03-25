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

    monday_start = models.DateTimeField()
    monday_end = models.DateTimeField()
    monday_cabinet = models.CharField(max_length=20)

    tuesday_start = models.DateTimeField()
    tuesday_end = models.DateTimeField()
    tuesday_cabinet = models.CharField(max_length=20)

    wednesday_start = models.DateTimeField()
    wednesday_end = models.DateTimeField()
    wednesday_cabinet = models.CharField(max_length=20)

    thursday_start = models.DateTimeField()
    thursday_end = models.DateTimeField()
    thursday_cabinet = models.CharField(max_length=20)

    friday_start = models.DateTimeField()
    friday_end = models.DateTimeField()
    friday_cabinet = models.CharField(max_length=20)

    saturday_start = models.DateTimeField()
    saturday_end = models.DateTimeField()
    saturday_cabinet = models.CharField(max_length=20)

    sunday_start = models.DateTimeField()
    sunday_end = models.DateTimeField()
    sunday_cabinet = models.CharField(max_length=20)

    duration = models.DurationField()

    specialization = models.CharField(max_length=100)


class Patient(BaseModel):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)

    doctor = models.ForeignKey(Doctor)

    date_of_receipt = models.DateTimeField()