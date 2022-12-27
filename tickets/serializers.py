from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework import serializers
from tickets.models import Event, Ticket, Orders
# ............Events...........
class EventsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ['title', 'city', 'country','image','venue','startDate','startDate','endDate']

class CreateEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['title', 'city', 'country','image','venue','startDate','startDate','endDate']

class UpdateEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['title', 'city', 'country','image','venue','startDate','startDate','endDate']     

class DeleteEventSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Event
        fields = ['title', 'city', 'country','image','venue','startDate','startDate','endDate']        

# ............Tickets...........

class TicketListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['owner', 'ticketdetails', 'event','price','available','image']

class CraeteTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['owner', 'ticketdetails', 'event','price','available','image']

class UpdateTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['owner', 'ticketdetails', 'event','price','available','image']        

class DeleteTicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['owner', 'ticketdetails', 'event','price','available','image'] 

# ............Orders...........

class OrdersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['buyer', 'ticket','date_created','date_modified']

class CraeteOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orders
        fields = ['buyer', 'ticket','date_created','date_modified']

# class UpdateOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Orders
#         fields = ['seller', 'buyer', 'ticket','date_created','date_modified']        

# class DeleteOrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Orders
#         fields = ['seller', 'buyer', 'ticket','date_created','date_modified']         



User = get_user_model()

class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)
 
    class Meta:
        model = User
        fields = ["username", "password", "token"]

        def create(self, validated_data):
            username = validated_data ["username"]
            password = validated_data ["password"]
            print("under password")
            new_user = User(username = username)
            print("under new_user")
            new_user.set_password(password)
            new_user.save()

            payload = RefreshToken.for_user(new_user)
            token = str(payload.access_token)

            validated_data["token"] = token
            return validated_data

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)
    token = serializers.CharField(allow_blank=True, read_only=True)
    
    def validate(self, data):
        my_username = data.get("username")
        my_password = data.get("password")      
        
        try:
            user_obj = User.objects.get(username=my_username)
        except User.DoesNotExist:
            raise serializers.ValidationError("username does not exist")
       
        if not user_obj.check_password(my_password):
            raise serializers.ValidationError("Incorrect password")

        payload = RefreshToken.for_user(user_obj)
        token = str(payload.access_token)
        
        data["token"] = token
        return data 

    
    
    