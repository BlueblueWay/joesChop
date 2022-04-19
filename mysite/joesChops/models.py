from django.db import models
from django.db.models.fields import IntegerField
import datetime

from django.db.models.fields.related import ForeignKey

# Create your models here.

class Customer(models.Model):
    Last_Name = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)
    Address = models.CharField(max_length=300)
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    ZIPCode = models.IntegerField()
    Phone =  models.CharField(max_length=20)
    Email =  models.CharField(max_length=200)

    def __str__(self):
        return "customer: " + str(self.id) + " " + self.Last_Name + " " + self.First_Name

#pre-create content in admin site
class Employee(models.Model):
    Last_Name = models.CharField(max_length=50)
    First_Name = models.CharField(max_length=50)
    Title = models.CharField(max_length=200)
    Phone =  models.CharField(max_length=20)
    Email =  models.CharField(max_length=200)

    def __str__(self):
        return "employee: " + str(self.id) + " " + self.Last_Name + " " + self.First_Name 

class Vehicle(models.Model):
    Make = models.CharField(max_length=200)
    Model = models.CharField(max_length=200)
    Year = models.CharField(max_length=200)
    Engine = models.CharField(max_length=200)
    Trim = models.CharField(max_length=200)
    Interior = models.CharField(max_length=200)
    Exterior = models.CharField(max_length=200)
    Body_Condition = models.CharField(max_length=200)
    Frame_Condition = models.CharField(max_length=200)
    Engine_Condition = models.CharField(max_length=200)

    def __str__(self):
        return "vehicle id: " + str(self.id) + " " + self.Make + " " + self.Model

class Plan(models.Model):
    Employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    Vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    Estimated_Price = models.IntegerField()
    Deposit = models.FloatField()
    Start_date = models.DateTimeField()
    Estimated_Date = models.DateTimeField()

    def __str__(self):
        return "plan id: " + str(self.id) + " " + self.Customer.Last_Name + " " + self.Customer.First_Name

#pre-create in adim site
class Item(models.Model):
    Item = models.CharField(max_length=200)
    Description = models.CharField(max_length=200)
    Parts = models.CharField(max_length=200)
    Price = models.FloatField()
    def __str__(self):
        return "item id:" + str(self.id) + " " + self.Item

class ItemPlan(models.Model):
     Plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
     Item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
     Days = models.CharField(max_length=20)

     def __str__(self):
         return "item_plan id:" +str(self.id)



#Item billing form
class ItemizedBilling(models.Model):
    Plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
    Finish_date = models.DateTimeField()

    def __str__(self):
        return "Billing id:" + str(self.id) + " " + str(self.Plan_id)

class ItemCost(models.Model):
    Billing_id = models.ForeignKey(ItemizedBilling, on_delete=models.CASCADE)
    Item_id = models.ForeignKey(Item, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Stage = models.CharField(max_length=200)

    def __str__(self):
        return "ItemCost id:" + str(self.id)

class LaberCost(models.Model):
    Billing_id = models.ForeignKey(ItemizedBilling, on_delete=models.CASCADE)
    Employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Stage = models.CharField(max_length=200)
    Time = models.IntegerField()
    Cost = models.FloatField()
    Task = models.CharField(max_length=200)

    def __str__(self):
        return "LaberCost id:" + str(self.id)
    
#Question service
class QuestionPhotoService(models.Model):
    Plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)

    def __str__(self):
        return "(Question Photo Service id:" + str(self.id) + ") for " + str(self.Plan_id)

class Photo(models.Model):
    Service_id = models.ForeignKey(QuestionPhotoService, on_delete=models.CASCADE)
    Image = models.ImageField(null=True, blank=True, upload_to="images/")
    Photo_day = models.DateTimeField()

    def __str__(self):
        return "photo id:" + str(self.id) + str(self.id) + " ("  + str(self.Service_id) + ")"

class Question(models.Model):
    Service_id = models.ForeignKey(QuestionPhotoService, on_delete=models.CASCADE)
    Employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    Date = models.DateTimeField()
    Question = models.CharField(max_length=200)
    Answer = models.CharField(max_length=200,null=True, blank=True)

    def __str__(self):
        return "Question id:" + str(self.id) + " ("  + str(self.Service_id) + ")"