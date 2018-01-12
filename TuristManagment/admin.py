from django.contrib import admin

# Register your models here.
from .models import SignUp,Reservation,Booking,mainAdmin,Employees,Department,Room
from .form import signUpForm


# class SignUpAdmin(admin.ModelAdmin):
#     list_display = ["__str__","email","full_name"]
#
#     form = signUpForm
   # class Meta:
   #     model = SignUp


admin.site.register(Reservation)
admin.site.register(Booking)
admin.site.register(mainAdmin)
admin.site.register(Employees)
admin.site.register(Room)
