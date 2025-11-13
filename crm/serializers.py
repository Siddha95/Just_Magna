from .models import Survey, Rating
from rest_framework import serializers

class SurveySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Survey
        fields = ['user', 'feedback']

class RatingSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Rating
        fields = ['survey', 'course', 'vote', 'dish']

