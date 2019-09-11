from DKClasses.Decorator_Logger_timer import my_logger, my_timer
import time

@my_logger
@my_timer
def display_info(name, age, sleepSeconds):
    time.sleep(sleepSeconds)
    print('display_info ran with argument ({}, {}, {})'.format(name, age, sleepSeconds))

#display_info('Dave',23, 1)
display_info('GreatWell',24, 3)