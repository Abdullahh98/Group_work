from django import forms
from django.contrib.auth import get_user_model

# from tickets.models import Ticket, Event, Orders
# from django.core.exceptions import ValidationError 

# from tickets.valedator import validate_price

User = get_user_model()

    
    
# class CreateTicketForm(forms.ModelForm):    
    
#     price = forms.FloatField(validators=[validate_price])


#     class Meta:
#         model = Ticket
#         fields = ['ticketdetails','event','price','available','image']

        
        
    
    
    
            
       
        
        
        
# class CreateEventForm(forms.ModelForm):
#     class Meta:
#         model = Event
#         fields = '__all__'
        
        
# class CreateOrdersForm(forms.ModelForm):
#     class Meta:
#         model = Orders
#         fields = '__all__'
        
        
        
class UserRegister(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password"]
        tailwind_css = '''
        w-[50%]
        m-auto
        mb-3
        rounded-md
        '''
        widgets = {
            'username':forms.TextInput(attrs={
                'class':tailwind_css,
                'placeholder':"Username"
                }),
            'first_name':forms.TextInput(attrs={
                'class':tailwind_css,
                                'placeholder':"First Name"
}),
            'last_name':forms.TextInput(attrs={
                'class':tailwind_css,
                                'placeholder':"Last Name"
}),
            'email':forms.EmailInput(attrs={
                'class':tailwind_css,
                                'placeholder':"Email"
}),
            "password": forms.PasswordInput(attrs={
                'class':tailwind_css,
                                'placeholder':"Password"
}),
        }
    
    
class UserLogin(forms.Form):
    
    tailwind_css = '''
    w-[50%]
    m-auto
    mb-3
    rounded-md
    '''
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={
        'class': tailwind_css,
        'placeholder':"Username"

    }))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={
        'class': tailwind_css,
        "placeholder":"Password"

    }))