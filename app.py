import sentry_sdk
from sentry_sdk.integrations.logging import LoggingIntegration
import logging
from datetime import datetime as dt
import logging

# All of this is already happening by default!
sentry_logging = LoggingIntegration(
    level=logging.INFO,        # Capture info and above as breadcrumbs
    event_level=logging.ERROR  # Send errors as events
)
sentry_sdk.init(
    dsn="your_sentry_dns",
    integrations=[sentry_logging]
)
"""
https://docs.sentry.io/platforms/python/logging/
"""
def capture_exception():
    try:
        trying = 1/0
    except Exception as e:
        sentry_sdk.capture_exception(Exception(e))

def capture_message():
    sentry_sdk.capture_message("Start logging message ======= ")

def capture_logger_info():
    logging.error(f"Capture logger info {dt.now().strftime('%Y%m%d %H:%M:%S')}========",
                  extra={'event': 'capture',
                         #'date': dt.now().strftime("%Y%m%d %H:%M:%S"),
                         'user': {'email': 'test@test.com'},
                         'tags': {'database': '1.0'},
                })
