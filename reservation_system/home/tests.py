from django.test import TestCase, Client
from django.urls import reverse
import json


# Create your tests here.
class ReservationModelTests(TestCase):

    def test_get_reservation_data(self):

        client = Client()

        response = client.get(reverse("home"))

        response_json = json.loads(str(response.content, encoding='utf8'))

        self.assertEquals(response.status_code, 200)
        self.assertJSONEqual(json.dumps(response_json[4]), {'id': 5, 'rental': 'Rental-2', 'checkin': '2022-01-20', 'checkout': '2022-02-11', 'prev_reservation_id': 4})
        