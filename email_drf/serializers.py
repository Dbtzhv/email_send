from rest_framework.serializers import ModelSerializer
from email_drf.models import Message


class EmailSerializer(ModelSerializer):
    class Meta:
        model = Message
        queryset = model.objects.all()
        fields = "__all__"
