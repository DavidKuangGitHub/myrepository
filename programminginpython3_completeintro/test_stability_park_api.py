import time
import slash
import logging
import sys
from tests.stability.stability_base_test import StabilityBaseTest
from tests.stability.stability_base_test import StabilityLoggerDecorator
from tests.stability.stability_test_data import StabilityConstants
from menlo_ui_lib import Menlo
from menlo_test_lib.common_util.can_utilities import CanUtilities
from slash_step import STEP
from menlo_test_lib.utils import verify
from tests.media_player.media_test_data import usb1_name

class StabilityTestClass(StabilityBaseTest):
    def before(self,stability_logging,launch_menlo,can_bus):
        super(StabilityTestClass,self).before(stability_logging)
        slash.logger.info("Setup for each test from this class")
        
        self.driver=launch_menlo
        self.interface=Menlo(self.driver)
        self.can_utilities=CanUtilities(can_bus)
        slash.config.root.audio.directly_connected_media=usb1_name
        
     @StabilityLoggerDecorator()
     def test_stability_park_api(self):
        print("Running THIS test")
        
        logging.basicConfig(stream=sys.stdout,level=logging.DEBUG)
        
        with STEP("This is to be displayed as StepName"):
             self.can_utilities.ignition_off()
