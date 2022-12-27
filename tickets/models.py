from django.db import models
from django.db import models
from django.contrib.auth.models import User

from tickets.valedator import validate_price

 
class Event(models.Model):
    title = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image = models.ImageField(help_text='Product Image', upload_to='events', blank=True,)  
    venue = models.CharField(max_length=50)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()
   
    def __str__(self):
        return f'{self.title}'
   
 
class Ticket(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owned_tickets")
    ticketdetails= models.TextField()
    event = models.ForeignKey(Event, on_delete=models.CASCADE, related_name="ticket_event")
    price = models.FloatField(validators=[validate_price])
    available = models.BooleanField()
    image = models.ImageField(help_text='Product Image', upload_to='tickets', blank=True)  


    def __str__(self):
        return f'Ticket: {self.id} - Seller: {self.owner.id}'




class Orders(models.Model):
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="buyer")
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name="order")
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified =models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'Ticket: {self.ticket.id} - Buyer: {self.buyer.id}'
    

class Profile(models.Model):
    user_name =models.OneToOneField(User,on_delete=models.CASCADE,primary_key="True")
    civilid = models.PositiveIntegerField()    
