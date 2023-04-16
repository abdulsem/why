from rest_framework import serializers
from .models import MyUser,posts

class Seruse(serializers.ModelSerializer):
    class Meta:
        model = MyUser
        fields = '__all__'
class postseralizer(serializers.ModelSerializer):
    class Meta:
        model = posts
        fields = '__all__'