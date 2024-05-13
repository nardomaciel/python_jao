from payament_times.in_time import *
import config
from payament_times.months12 import twelve_months
from payament_times.months3 import three_months
from payament_times.months6 import six_months
from payament_times.months9 import nine_months

def credit_payament(desired_car, time_option):
    if(time_option == 1):
        return (in_time(desired_car))
    elif (time_option == 2):
        return (three_months(desired_car))
    elif (time_option == 3):
        return (six_months(desired_car))
    elif (time_option == 4):
        return (nine_months(desired_car))
    elif (time_option == 5):
        return (twelve_months(desired_car))
    