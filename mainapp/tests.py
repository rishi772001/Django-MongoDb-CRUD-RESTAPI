from django.test import TestCase
from .models import StudentDetails


# Model Tests
class ModelTests(TestCase):
    def test(self):
        StudentDetails(name="swathy", mark1="100", mark2="100", mark3="100", total="300").save()
        swathy = StudentDetails.objects.get(name="swathy")
        self.assertEqual(swathy.name, "swathy")
        self.assertEqual(swathy.mark1, "100")
        self.assertEqual(swathy.total, "300")
