import slash
import sys, time, logging
from slash_step.__init__ import STEP
from menlo_test_lib.common_util.can_utilities import CanUtilities
from menlo_test_lib.utils import verify
from menlo_ui_lib.menlo_interface import Menlo

from tests.stability.stability_base_test import StabilityBaseTest
from tests.stability.stability_base_test import StabilityLoggerDecorator
from tests.stability.stability_test_data import StabilityConstants


class StabilityTestClass(StabilityBaseTest):

    def before(self, stability_logging, launch_menlo, can_bus):
        super(StabilityTestClass, self).before(stability_logging)
        slash.logger.info(
            "Pre-condition: \
                1. NAV routes playing via hip logs on a USB attached to SYNC. \
                2. Two Android phones connected to PC for Bluetooth pairing \
                    (1) PhoneA NEAR_END_PHONE\
                    (2) PhoneB FAR_END_PHONE. \
                3. Pair one phone via Bluetooth to SYNC\
                    (1) PhoneA NEAR_END_PHONE.")

        self.driver = launch_menlo
        self.interface = Menlo(self.driver)
        self.can_utilities = CanUtilities(can_bus)

    @StabilityLoggerDecorator()
    def test_user_based_scenario(self):
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)

        with STEP("Step1. Send ignition OFF and wait for SYNC to shutdown"):
            self.radio_page_menlo = self.interface.radio_page.open()
            verify(self.radio_page_menlo.loaded, "Radio page has not been loaded yet.",
                   "Radio page has been loaded successfully.")

        with STEP("Step2. Send ignition ON and wait for SYNC to boot up"):
            time.sleep(StabilityConstants.WAIT_TEN_SECONDS)

        with STEP("Step3. Verify Bluetooth connection exists on SYNC"):
            time.sleep(StabilityConstants.WAIT_TEN_SECONDS)

        with STEP("Step4. Send text message from Phone B to Phone A"):
            time.sleep(StabilityConstants.WAIT_TEN_SECONDS)

        with STEP("Step5. Receive text message on SYNC and read"):
            time.sleep(StabilityConstants.WAIT_TEN_SECONDS)

        with STEP("Step6. Change audio source to BT audio"):
            time.sleep(StabilityConstants.WAIT_TEN_SECONDS)

        with STEP("Step7. Wait for 2 minutes"):
            time.sleep(StabilityConstants.WAIT_TWO_MIN)

        with STEP("Step8. Change audio source to FM"):
            time.sleep(StabilityConstants.WAIT_TEN_SECONDS)