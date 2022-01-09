from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import *
from .forms import *
from .filters import *
from django.urls import reverse
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import *


@unauthenticated_user
def index(request):

        if request.method == "POST":   
            username = request.POST.get("username")
            password = request.POST.get("password")
            
            user = authenticate(request, username = username, password = password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("dataentry",))
            else:
                messages.info(request, "Username or password incorrect")
        context = {}
        return render(request, "inspection/index.html", context)

def logoutuser(request):
    logout(request)
    return HttpResponseRedirect(reverse("index",))


@login_required(login_url='index')
def dataentry(request):
    form = InspectionForm()
    form2 = VehicleForm()
    if request.method == "POST":
        vehicle_entry = VehicleForm(request.POST)
        inspection_entry = InspectionForm(request.POST)
        print(request.user)
        if vehicle_entry.is_valid() and inspection_entry.is_valid():
            vehicle_entry.save()
            inspection_entry.save(commit = False)

            vehicle_instance = Vehicle.objects.latest('id')
            inspection_entry.instance.vehicle = vehicle_instance
            inspection_entry.instance.user = request.user
            inspection_entry.save()
            return HttpResponseRedirect(reverse("dbsearch",))
    context = {"form" : form, "form2": form2}


    return render(request, "inspection/dataentry.html",context)
  

@login_required(login_url='index')  
def dbsearch(request):
    # inspections = request.user.inspections.all()
    inspections = Inspection.objects.filter(user = request.user).order_by('-id')
    insp_filter = InspectionFilter(request.GET, queryset = inspections)
    inspections = insp_filter.qs
    contex  = { "inspections" : inspections, "insp_filter" : insp_filter}
    return render(request, "inspection/dbsearch.html", contex)


 


@login_required(login_url='index')
def edit(request, pk):
    inspection_inst = Inspection.objects.get(id=pk)
    vehicle_inst = Vehicle.objects.get(id = inspection_inst.vehicle_id)

    form = InspectionForm(instance= inspection_inst)
    form2 = VehicleForm(instance= vehicle_inst)

    if request.method == "POST":
        vehicle_entry = VehicleForm(request.POST, instance = vehicle_inst)
        inspection_entry = InspectionForm(request.POST, instance = inspection_inst)
 
        if vehicle_entry.is_valid() and inspection_entry.is_valid():
            vehicle_entry.save()
            inspection_entry.save(commit = False)

            inspection_entry.instance.vehicle = vehicle_inst
            inspection_entry.save()
            return HttpResponseRedirect(reverse("dbsearch",))
        else:

            return HttpResponseRedirect(reverse("dataentry",)) 


    context = {"form" : form, "form2": form2}
    return render(request, "inspection/dataentry.html",context)



