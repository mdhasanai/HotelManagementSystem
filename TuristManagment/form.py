from django import forms
from bootstrap3_datetime.widgets import DateTimePicker
from .models import SignUp


class contactForm(forms.Form):
    full_name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Write Name...'}
    ))
    email = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Write Email...'}
    ))
    message = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Write Your Message...'}
    ))


class signUpForm(forms.ModelForm):
    class Meta:
        model = SignUp
        fields = ['full_name','email']

        def clear_email(self):
            email = self.cleaned_data.get('email')

            if not "edu" in email:
                raise forms.ValidationError("Please use a valid email")
            return email

class reservationForm(forms.Form):

    arrival_date = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'awe-calendar awe-input', 'placeholder': 'Arrival...'}  ))
    departure_date = forms.DateField(widget=forms.TextInput(
        attrs={'class': 'awe-calendar awe-input', 'placeholder': 'Arrival...'}))
    night = forms.IntegerField(max_value=6, min_value=0)
    adult = forms.IntegerField(max_value=4, min_value=0,required=True)
    children = forms.IntegerField(max_value=4, min_value=0)

class userbookingForm(forms.ModelForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    # town = forms.CharField(required=True)
    # country = forms.CharField(required=True)
    # email = forms.EmailField(required=True)
    # passport_number = forms.IntegerField(required=True)
    # phone_number = forms.IntegerField(required=True)

class bookingForm2(forms.Form):
    # arrival_date = forms.DateField(widget=forms.TextInput(
    #     attrs={'type': 'date'}))
    # departure_date = forms.DateField(widget=forms.TextInput(
    #     attrs={'type': 'date'}))
    # night = forms.IntegerField(max_value=6, min_value=0)
    # adult = forms.IntegerField(max_value=4, min_value=0, required=True)
    # children = forms.IntegerField(max_value=4, min_value=0)


    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    address = forms.CharField(required=True)
    email = forms.EmailField()
    town = forms.CharField(required=True)
    country = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    passport_number = forms.IntegerField(required=True)
    phone_number = forms.IntegerField(required=True)
    message = forms.CharField(widget=forms.Textarea)





