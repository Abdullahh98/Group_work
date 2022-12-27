from django.contrib import admin
from tickets.models import Ticket, Orders , Event,Profile

# Register your models here.
admin.site.register([Event, Ticket,Orders,Profile])