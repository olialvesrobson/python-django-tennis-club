# app/testPosts.py

from django.test import TestCase
from members.models import Member


class MembersTestCase(TestCase):
    def testPost(self):
        testing = Member(firstname="My Title", lastname="Blurb", phone=1234567890, joined_date="2020-01-01", active=True)
        self.assertEqual(testing.firstname, "My Title")
        self.assertEqual(testing.lastname, "Blurb")
        self.assertEqual(testing.phone, 1234567890)
        self.assertEqual(testing.joined_date, "2020-01-01")
        self.assertEqual(testing.active, True)