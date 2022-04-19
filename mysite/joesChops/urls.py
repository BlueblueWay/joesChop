from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
# Routing paths with html forms
urlpatterns = [
    
    path("", views.index, name="index"),
    path("customizationPlan/<int:id>/", views.customization_plan, name="customization plan"),
    path("customizationPlan/create/", views.create, name="create"),
    path("customerWebSite/<int:id>/", views.customer_web_site, name="Customer Web Site"),
    path("customerWebSite/", views.service_redirect, name="Customer Web Site"),
    path("customerBilling/", views.billing_redirect, name="Billing Redirect"),
    path("customerBilling/<int:id>/", views.customer_billing, name="Billing"),
    path("replayQuestion/<int:id>/", views.question, name="Question")
]