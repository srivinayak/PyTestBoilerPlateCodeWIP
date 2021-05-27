# pylint: disable=no-member
# pylint: disable=no-self-use
from datetime import timedelta, datetime

from faker import Faker
import logging

logger = logging.getLogger(__name__)


class DataUtils:
    def __init__(self):
        self._faker = Faker()

    def get_random_datetime(self, days=0, hours=1):
        logger.info("Generating random date time")
        current_datetime = datetime.utcnow() \
                               .replace(minute=0, second=0, microsecond=0) + timedelta(days=days, hours=hours)
        next_datetime_displayed = current_datetime.strftime('Today' + ' ' + '%b %-d %-I:%M %p')
        logger.info("Generated random date time is: ", next_datetime_displayed)
        return next_datetime_displayed

    def get_random_incomplete_password(self, length=7):
        logger.info("Generating random incomplete password")
        return self._faker.password(length)
