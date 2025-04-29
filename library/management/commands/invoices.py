from django.core.management import BaseCommand
from django.utils import timezone
from datetime import timedelta
from library.models import Rental, FakeInvoice, Notification