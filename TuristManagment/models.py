from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

# Create your models here.

class hotelAdmin(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=30)

class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120,blank=True,null=True)


    def __str__(self):
        return self.email


class contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    message = models.TextField(max_length=500)





class Room(models.Model):

    room_id = models.IntegerField(unique=True)
    room_type = models.CharField(max_length=100)
    room_location = models.TextField()
    room_price = models.IntegerField()
    room_size = models.CharField(max_length=50)
    room_view = models.CharField(max_length=50)
    room_bed = models.CharField(max_length=100)
    room_member = models.IntegerField(blank=True,null=True)
    room_availability = models.IntegerField()
    room_img = models.CharField(max_length=100,blank=True,null=True)

    def __str__(self):
        return self.room_id



class Reservation(models.Model):
    arrival_date = models.DateField()
    departure_date = models.DateField()
    night = models.IntegerField()
    adult = models.IntegerField(null=True)
    children = models.IntegerField(null=True)
    # booking_id = models.IntegerField(null=True,blank=True)



class Booking(models.Model):
    first_name = models.CharField(max_length=30,null=False)
    last_name = models.CharField(max_length=30,null=False)
    address = models.CharField(max_length=200,null=True)
    town = models.CharField(max_length=30,null=True)
    country = models.CharField(max_length=30,null=True)
    email = models.CharField(max_length=30,null=False)
    passport_number = models.IntegerField(null=False)
    phone_number = models.IntegerField(null=False)
    # booking_id = models.IntegerField(auto_created=True)

    #selected_room = models.ForeignKey('TuristManagment.Room', blank=True, null=True)

    def __str__(self):
        return self.first_name


class mainAdmin(models.Model):

    adminName = models.CharField(max_length=50)
    adminPassword = models.CharField(max_length=32)


class Employees(models.Model):
    empID = models.IntegerField()
    empName = models.CharField(max_length=50)
    empEmail = models.CharField(max_length=100,null=True)
    empAddress = models.CharField(max_length=100)
    empCity = models.CharField(max_length=30)
    empCounty = models.CharField(max_length=30)

    deptid = models.ForeignKey("TuristManagment.Department",null=True)


class Department(models.Model):

   # deptID = models.CharField(max_length=30)
    deptName = models.CharField(max_length=30)
    position = models.CharField(max_length=30,blank=True,null=True)























