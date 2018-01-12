from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
from .form import signUpForm, contactForm, reservationForm,userbookingForm,bookingForm2
from TuristManagment.models import Room, Reservation,Booking,contact
from datetime import datetime
import time
# Create your views here.

def index(request):

    title = "Welcome"


    # if request.user.is_authenticated():
    #     title = "My Title %s" %(request.user)
    # add form

    # if request.method == "POST":
    #     print(request.POST)

    form = signUpForm(request.POST)

    contex = {
        "title": title,
        "form": form
    }

    posts = Room.objects.all()

    contex2 = {
        'posts': posts

    }

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        print(instance.full_name)

        contex = {
            "title": "Thank you"

        }

    return render(request, 'Home.html', contex2)


def contact(request):

    form = contactForm(request.POST or None)

    if form.is_valid():
        email = form.cleaned_data.get("email")
        full_name = form.cleaned_data.get("full_name")
        message = form.cleaned_data.get("message")
        #instance = contact(name=full_name,email=email,message=message)
        #instance.save()
        print(form.cleaned_data,email)



        subject = "contact site"
        from_email = settings.EMAIL_HOST_USER
        to_email = [from_email,'yourotheremail@gmail.com']
        conact_mwssage = "%s: %s via %s "%(
            full_name,
            message,
            email)


        send_mail(
            subject,
            conact_mwssage,
            from_email,
            to_email,
            fail_silently=True,
        )



    context = {
        "form":form,

    }


    return render(request,"contact.html", context)

def reservation(request):

    form = reservationForm(request.POST or None)
    posts = {}

    if form.is_valid():
        arrival_date = form.cleaned_data.get("arrival_date")
        departure_date = form.cleaned_data.get("departure_date")
        night = form.cleaned_data.get("night")
        children = form.cleaned_data.get("children")
        adult = form.cleaned_data.get("adult")
        print(form.cleaned_data,arrival_date)
        # instance = Reservation(arrival_date=arrival_date,departure_date=departure_date,night=night,children=children,adult=adult,booking_id=None)
        # instance.save()

        posts = Room.objects.all()

    contex = {
        "form": form,
        'posts': posts
    }

    return render(request,'Reservation.html',contex)

def room(request):
    posts = Room.objects.all()

    contex2 = {
        'posts': posts
    }

    return render(request, 'Room.html', contex2)


def room_details(request,pk):
    post = Room.objects.get(pk=pk)

    return render(request, 'RoomDetails.html', {'post': post})

def todo(request):
    form = contactForm(request.POST or None)

    context = {
        "form": form
    }

    return render(request,'Booking.html',context)


def booking(request):
    #form1 = reservationForm(request.POST or None)
    form2 = bookingForm2(request.POST or None)



    # if form1.is_valid():
    #     arrival_date = form1.cleaned_data.get("arrival_date")
    #     departure_date = form1.cleaned_data.get("departure_date")
    #     night = form1.cleaned_data.get("night")
    #     children = form1.cleaned_data.get("children")
    #     adult = form1.cleaned_data.get("adult")
    #     print(form1.cleaned_data, arrival_date)





    if form2.is_valid()  :
        # arrival_date = form2.cleaned_data.get("arrival_date")
        # departure_date = form2.cleaned_data.get("departure_date")
        # night = form2.cleaned_data.get("night")
        # children = form2.cleaned_data.get("children")
        # adult = form2.cleaned_data.get("adult")
        # print(form2.cleaned_data, arrival_date)

        first_name = form2.cleaned_data.get("first_name")
        last_name = form2.cleaned_data.get("last_name")
        address = form2.cleaned_data.get("address")
        town = form2.cleaned_data.get("town")
        country = form2.cleaned_data.get("country")
        email = form2.cleaned_data.get("email")
        passport_number = form2.cleaned_data.get("passport_number")
        phone_number = form2.cleaned_data.get("phone_number")
        message = form2.cleaned_data.get("message")
        print(form2.cleaned_data)
        print(form2.cleaned_data)
        instance = Booking(first_name=first_name, last_name=last_name, address=address, town=town, country=country,
                           email=email, passport_number=passport_number, phone_number=phone_number)
        instance.save()








        return render(request,'congress.html',{})




    context = {
        "form2": form2
    }

    return render(request,'Booking.html',context)


def about(request):






    return render(request,'About.html',{})










