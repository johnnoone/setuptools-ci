import sys
import setuptools
from distutils import log
from distutils.errors import DistutilsSetupError

class ContinuousIntegrationCommand(setuptools.Command):
    description = "disables sys.exit()"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        def exit(msg=None):
            log.info("sys.exit disabled")
            if msg:
                log.info("sys.exit disabled")

        exit, sys.exit = sys.exit, exit

        self.run_command("sloccount")
        self.run_command("clonedigger")
        self.run_command("lint")
        self.run_command("flakes")
        self.run_command("nosetests")

        exit, sys.exit = sys.exit, exit
