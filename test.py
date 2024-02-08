import logging
import pytz
import datetime

# Set the logging level to DEBUG
logging.basicConfig(level=logging.INFO, filename="log.log",filemode="w")

# Log messages
logging.debug("debugg")
logging.info("info")
print("teststst")
# utc_now = datetime.utcnow()
# print("uuu", utc_now)
# Get the current timezone
current_timezone = pytz.timezone('GMT')
print("zzzzz", 
datetime.utcnow().astimezone().tzinfo)
# Localize the UTC time to the current timezone
# local_time = current_timezone.localize(utc_now)
# print("loccclcl", local_time)
# Get the timezone name
timezone_name = local_time.tzinfo.zone
print("BNNNNN", timezone_name)