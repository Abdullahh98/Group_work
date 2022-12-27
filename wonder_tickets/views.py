from django.shortcuts import render,redirect
from tickets.models import Event, Ticket
def index(request):
    user = request.user
    events = Event.objects.all()
    tickets = Ticket.objects.all()
    context = {"user":user,
               "events":events,
               "tickets": tickets
            }
    print(tickets)
    if not user.is_active:
        return redirect('log_in')
    return render(request, 'index.html', context)