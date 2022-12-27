
# Create your views here.
from rest_framework.generics import ListAPIView, UpdateAPIView, CreateAPIView, DestroyAPIView
from tickets.serializers import EventsListSerializer,CreateEventSerializer,UpdateEventSerializer,DeleteEventSerializer
from tickets.serializers import TicketListSerializer , CraeteTicketSerializer , UpdateTicketSerializer , DeleteTicketSerializer
from tickets.serializers import OrdersListSerializer , CraeteOrderSerializer 
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from tickets.models import Event,Ticket,Orders
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK,HTTP_400_BAD_REQUEST
from .serializers import RegistrationSerializer,LoginSerializer
from .forms import UserRegister, UserLogin
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

# Create your views here.

class RegistrationAPIView(CreateAPIView):
    serializer_class = RegistrationSerializer

class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self,request):
        my_data = request.data
        serializer = LoginSerializer(data=my_data)
        if serializer.is_valid(raise_exception=True):
            valid_data = serializer.data
            return Response(valid_data, status=HTTP_200_OK)
        return Response(serializer.errors, HTTP_400_BAD_REQUEST)
      



# ------------- Event VIEWS -------------

class EventListView(ListAPIView):
    serializer_class = EventsListSerializer
    def get_queryset(self):
        queryset = Event.objects.all()
        
        return queryset
    permission_classes=[AllowAny]

class EventCreateView(CreateAPIView):
    serializer_class = CreateEventSerializer
    def perform_create(self, serializer):
        serializer.save()
        permission_classes=[IsAdminUser]

class EventUpdateView(UpdateAPIView):
    queryset = Event.objects.all()
    serializer_class = UpdateEventSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'
    permission_classes = [IsAdminUser]

class EventDeleteView(DestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = DeleteEventSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'event_id'
    permission_classes = [IsAdminUser]

# ------------- Ticket VIEWS -------------

class TicketListView(ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketListSerializer
    permission_classes=[AllowAny]

class TicketCreateView(CreateAPIView):
    serializer_class = CraeteTicketSerializer
    def perform_create(self, serializer):
        serializer.save()
    permission_classes=[IsAuthenticated,IsAdminUser]

class TicketUpdateView(UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = UpdateTicketSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'ticket_id'
    permission_classes=[IsAuthenticated,IsAdminUser]

class TicketDeleteView(DestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = DeleteTicketSerializer
    lookup_field = 'id'
    lookup_url_kwarg = 'ticket_id'
    permission_classes=[IsAuthenticated,IsAdminUser]

# ------------- Order VIEWS -------------

class OrderListView(ListAPIView):
    queryset = Orders.objects.all()
    serializer_class = OrdersListSerializer
    permission_classes=[AllowAny]

class OrdertCreateView(CreateAPIView):
    serializer_class = CraeteOrderSerializer
    def perform_create(self, serializer):
        serializer.save()
    permission_classes=[IsAuthenticated]


# ------------- Templates VIEWS ------------
def user_register(request):
    form = UserRegister()
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(user.password)
            user.save()

            login(request, user)
            # Where you want to go after a successful signup
            return redirect("index")
    context = {
        "form": form,
    }
    return render(request, "register.html", context)

def user_login(request):
    form = UserLogin()
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            auth_user = authenticate(username=username, password=password)
            if auth_user is not None:
                login(request, auth_user)
                # Where you want to go after a successful login
                return redirect("index")

    context = {
        "form": form,
    }
    return render(request, "login.html", context)

def logout_view(request):
    logout(request)
    return redirect("index")