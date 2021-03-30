from .pus_001_request_verification import RequestVerification
from .pus_003_housekeeping import Housekeeping
from .pus_005_event_reporting import EventReporting
from .pus_008_function_management import FunctionManagement
from .pus_017_test import Test

# Aliases
PusService1 = RequestVerification
PusService3 = Housekeeping
PusService5 = EventReporting
PusService8 = FunctionManagement
PusService17 = Test
