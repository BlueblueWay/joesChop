from pathlib import Path
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.conf import settings
from joesChops.forms import BillingRedirect, CreateCustomerForm, CreateVehicleForm, CreatePlanForm, QuestionForm, ServiceRedirect

from .models import Customer, Employee, Item, Vehicle, Plan,ItemPlan
from .models import Item, ItemizedBilling, ItemCost,LaberCost
from .models import QuestionPhotoService, Photo, Question

def index(request):
    return render(request, "joesChops/home.html", {})

#display customer information
def customization_plan(request, id):
    plan = Plan.objects.get(id=id)
    cid = plan.Customer.id
    vid = plan.Vehicle.id
    eid = plan.Employee.id
    c = Customer.objects.get(id=cid)
    v = Vehicle.objects.get(id=vid)
    e = Employee.objects.get(id=eid)
    url = str(Path(__file__).resolve().parent.parent)

    return render(request, "joesChops/customiaztionPlan.html", {"customer": c, "plan": plan, "vehicle": v, "employee": e, "url": url})

#customer web site page
def customer_web_site(request, id):

    plan = Plan.objects.get(id=id)
    c = plan.Customer
    s = QuestionPhotoService.objects.get(Plan_id=plan.id)
    q = Question.objects.filter(Service_id=s.id)
    p = Photo.objects.filter(Service_id=s.id)
    

    form_Question = QuestionForm()   

    return render(request, "joesChops/customerWebSite.html", {"customer": c,"photo": p, "service": s, "question": q,"form_Question":form_Question})

def question(request, id):

    q = Question.objects.get(id=id)
    s = q.Service_id
    pid = s.Plan_id.id
    if request.method == "POST":
        form_Question = QuestionForm(request.POST)

        if form_Question.is_valid():
            ans = form_Question.cleaned_data["Answer"]
            q.Answer = ans
            q.save()
            print("in question function")
            return HttpResponseRedirect("/customerWebSite/%i" %pid)
    else:
        form_Question = QuestionForm()

    return render(request, "joesChops/question.html", {"question":q, "form_Question":form_Question})

    

  
 





#customer billing page
def customer_billing(request, id):
    
    plan = Plan.objects.get(id=id)
    c = plan.Customer
    v = plan.Vehicle
    ib = ItemizedBilling.objects.get(Plan_id=plan.id)
    lc = LaberCost.objects.get(Billing_id=ib.id)
    e = lc.Employee_id
    ic = ItemCost.objects.filter(Billing_id=ib.id)

    
    tic = 0
    for i in ic:
       tic += (i.Item_id.Price * i.Quantity)
    
    total = tic + lc.Cost

    #

    return render(request, "joesChops/billing.html", {"customer": c, "vehicle": v,"laborCost": lc,
                                                     "employee": e, "itemCost": ic,
                                                     "totalItemCost": tic, "total": total, "ItemBilling": ib})

def service_redirect(request):

    if request.method == "POST":
        form_Server = ServiceRedirect(request.POST)

        if form_Server.is_valid():
            s = form_Server.cleaned_data["sid"]
            return HttpResponseRedirect("/customerWebSite/%i" %s)
    else:
        form_Server = ServiceRedirect()

    return render(request, "joesChops/serviceRedirect.html", {"form_Server":form_Server})

def billing_redirect(request):
    if request.method == "POST":
        form_Billing = BillingRedirect(request.POST)

        if form_Billing.is_valid():
            s = form_Billing.cleaned_data["sid"]
            return HttpResponseRedirect("/customerBilling/%i" %s)
    else:
        form_Billing = ServiceRedirect()

    return render(request, "joesChops/billingRedirect.html", {"form_Server":form_Billing})
#insert in Customization plan/Customer/Vehicle
def create(request):
    if request.method == "POST":
        form_Customer = CreateCustomerForm(request.POST)
        form_Vehicle = CreateVehicleForm(request.POST)
        form_Plan = CreatePlanForm(request.POST)

        if form_Customer.is_valid() and form_Vehicle.is_valid() and form_Plan.is_valid():
            ln = form_Customer.cleaned_data["last_name"]
            fn = form_Customer.cleaned_data["first_name"]
            add = form_Customer.cleaned_data["Address"]
            city = form_Customer.cleaned_data["City"]
            state = form_Customer.cleaned_data["State"]
            zipcode = form_Customer.cleaned_data["ZIPCode"]
            phone = form_Customer.cleaned_data["Phone"]
            email = form_Customer.cleaned_data["Email"]
            
            t1 = Customer(
                Last_Name = ln,
                First_Name= fn,
                Address = add,
                City = city,
                State = state,
                ZIPCode = zipcode,
                Phone = phone,
                Email = email,
                )
            t1.save()

            make = form_Vehicle.cleaned_data["Make"]
            model = form_Vehicle.cleaned_data["Model"]
            year = form_Vehicle.cleaned_data["Year"]
            engine = form_Vehicle.cleaned_data["Engine"]
            trim = form_Vehicle.cleaned_data["Trim"]
            interior = form_Vehicle.cleaned_data["Interior"]
            exterior = form_Vehicle.cleaned_data["Exterior"]
            bc = form_Vehicle.cleaned_data["Body_Condition"]
            fc = form_Vehicle.cleaned_data["Frame_Condition"]
            ec = form_Vehicle.cleaned_data["Engine_Condition"]

            t2 = Vehicle(
                Make = make,
                Model= model,
                Year = year,
                Engine = engine,
                Trim = trim,
                Interior = interior,
                Exterior = exterior,
                Body_Condition = bc,
                Frame_Condition = fc,
                Engine_Condition = ec,
                )
            t2.save()

            employee = form_Plan.cleaned_data["Employee_id"]
            ep = form_Plan.cleaned_data["Estimated_Price"]
            deposit = form_Plan.cleaned_data["Deposit"]
            sd = form_Plan.cleaned_data["Start_date"]
            ed = form_Plan.cleaned_data["Estimated_Date"]


            t3 = Plan(
                Employee = employee,
                Customer = t1,
                Vehicle = t2,
                Estimated_Price = ep,
                Deposit = deposit,
                Start_date = sd,
                Estimated_Date = ed,
                )
            t3.save()    

        return HttpResponseRedirect("/customizationPlan/%i" %t1.id)
    else:
        form_Customer = CreateCustomerForm()
        form_Vehicle = CreateVehicleForm()
        form_Plan = CreatePlanForm()
        
    return render(request, "joesChops/planCreate.html", {"form_Customer":form_Customer, "form_Vehicle":form_Vehicle, "form_Plan":form_Plan})