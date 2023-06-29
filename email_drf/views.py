from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from email_drf.serializers import EmailSerializer
from email_drf.models import Message
from django.core.mail import send_mail
import logging


logger = logging.getLogger(__name__)


class EmailView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = EmailSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)

        message = response.data
        try:
            send_mail(
                message['subject'],
                message['message'],
                'denibatyzhevcoo@yandex.ru',
                [message['to']],
                fail_silently=False,
            )
            logger.info('Сообщение успешно отправлено')
        except Exception as e:
            Message.objects.last().delete()
            logger.error(f'Ошибка при отправке сообщения: {str(e)}')
            return Response(status=status.HTTP_400_BAD_REQUEST)

        return response
