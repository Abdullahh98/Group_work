"""django_ticket URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from tickets.views import  RegistrationAPIView, LoginAPIView, EventListView, EventCreateView, EventDeleteView, EventUpdateView,TicketListView,TicketCreateView,TicketUpdateView,TicketDeleteView,OrderListView,OrdertCreateView
from django.conf import settings
from django.conf.urls.static import static 

from .views import index
from tickets import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # ----- Authentications URLs -----
    path("register/", RegistrationAPIView.as_view(), name="register"),
    path("login/", LoginAPIView.as_view(), name="login"),

    # ----- Event URLs -----
    path('events/', EventListView.as_view() , name="events-list"),
    path('events/add/', EventCreateView.as_view() , name="event-add"),
    path('events/<int:event_id>/edit/', EventUpdateView.as_view() , name="events-edit"),
    path('events/<int:event_id>/delete/', EventDeleteView.as_view() , name="events-delete"),
        # ----- Ticket URLs -----
    path('tickets/<int:event_id>/', TicketListView.as_view() , name="tickets-list"),
    path('tickets/', TicketListView.as_view() , name="tickets-list"),
    path('tickets/add/', TicketCreateView.as_view() , name="ticket-add"),
    path('tickets/<int:ticket_id>/edit/', TicketUpdateView.as_view() , name="ticket-edit"),
    path('tickets/<int:ticket_id>/delete/', TicketDeleteView.as_view() , name="ticket-delete"),
   # ----- Order URLs -----
    path('Orders/', OrderListView .as_view() , name="Orders-list"),
    path('Orders/add/', OrdertCreateView.as_view() , name="Orders-add"),
    # ----- Template URLs ---- 
    path('', index, name='index'),
    path('sign_up/', views.user_register, name='sign_up'),
    path('log_in/', views.user_login, name='log_in'),
    path('log_out/', views.logout_view, name='log_out'),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    
    