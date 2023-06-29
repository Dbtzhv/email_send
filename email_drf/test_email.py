import pytest
from django.test.client import Client
from email_drf.models import Message



@pytest.mark.django_db
@pytest.mark.parametrize('email_data, expected_status', [
    ({'to': 'recipient@example.com', 'subject': 'Test Subject',
     'message': 'Test Message'}, 201),
    ({'to': 'invalid_email', 'subject': 'Test Subject', 'message': 'Test Message'}, 400),
    ({'subject': 'Test Subject', 'message': 'Test Message'}, 400),
    ({'to': 'recipient@example.com', 'message': 'Test Message'}, 400),
    ({'to': 'recipient@example.com', 'subject': 'Test Subject'}, 400),
])
def test_email_creation(email_data, expected_status):
    client = Client()
    response = client.post(
        "/send_email/",
        content_type="application/json",
        data=email_data
    )
    assert response.status_code == expected_status
    if expected_status == 201:
        message = Message.objects.last()
        assert message.to == email_data['to']
        assert message.subject == email_data['subject']
        assert message.message == email_data['message']
        message.delete()
