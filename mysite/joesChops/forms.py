from django import forms
import datetime
from .models import Customer, Employee, Item, Vehicle, Plan,ItemPlan
from .models import Item, ItemizedBilling, ItemCost,LaberCost
from .models import QuestionPhotoService, Photo, Question

#form for HTML
class CreateCustomerForm(forms.Form):
    #Customer table
    last_name = forms.CharField(label="Last Name", max_length=50)
    first_name = forms.CharField(label="First Name", max_length=50)
    Address = forms.CharField( max_length=300)
    City = forms.CharField(max_length=20)
    State = forms.CharField(max_length=20)
    ZIPCode = forms.IntegerField()
    Phone =  forms.CharField(max_length=20)
    Email =  forms.CharField(max_length=200)

class CreateVehicleForm(forms.Form):
    #Vehicle table
    Make = forms.CharField(max_length=200)
    Model = forms.CharField(max_length=200)
    Year = forms.CharField(max_length=200)
    Engine = forms.CharField(max_length=200)
    Trim = forms.CharField(max_length=200)
    Interior = forms.CharField(max_length=200)
    Exterior = forms.CharField(max_length=200)
    Body_Condition = forms.CharField(max_length=200)
    Frame_Condition = forms.CharField(max_length=200)
    Engine_Condition = forms.CharField(max_length=200)

class CreatePlanForm(forms.Form):
    #Employee table
    Employee_id = forms.ModelChoiceField(queryset=Employee.objects.all())
    Estimated_Price = forms.IntegerField()
    Deposit = forms.IntegerField()
    Start_date = forms.DateTimeField()
    Estimated_Date = forms.DateTimeField()

class CreateQuestionPhotoForm(forms.Form):
    #Question Photo Service table
    Plan_id = forms.ModelChoiceField(queryset=Plan.objects.all())
    Item_id = forms.ModelChoiceField(queryset=Item.objects.all())

class QuestionForm(forms.Form):
    #answer Question
    Answer = forms.CharField(max_length=200,widget=forms.Textarea,label=False)

class ServiceRedirect(forms.Form):
    sid = forms.IntegerField()

class BillingRedirect(forms.Form):
    sid = forms.IntegerField()