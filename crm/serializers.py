from .models import Survey, Rating
from rest_framework import serializers

class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ['user', 'feedback']

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = ['survey', 'course', 'vote', 'dish']

