from rest_framework import permissions, viewsets, mixins
from .serializers import SurveySerializer, RatingSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Rating, Survey

class RatingViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
        
class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all().order_by("-id")
    serializer_class = SurveySerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
