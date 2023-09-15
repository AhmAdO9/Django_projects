from rest_framework import serializers
from .models import CreateQuiz, Participate


class CreateQuizSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateQuiz
        fields = '__all__'

class ParticipateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participate
        fields = '__all__'
   