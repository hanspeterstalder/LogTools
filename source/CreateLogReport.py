"""
Runs the Report commands for the MIP log files
"""

import sys
import FileProcessor
from Commands import *

commands = [ReportFatalErrorCommand(), ReportErrorErrorCommand(),
            ReportWizardFSMCommand(), ReportAnDIFSMCommand(),
            ReportSpiFSMCommand(), ReportSpiRunFSMCommand(),
            ReportOutOfMemoryCommand(), ReportNewRunCommand(),
            ReportTraceArrayCommand()]

fileProcessor = FileProcessor.FileProcessor(sys.argv[1], commands)
fileProcessor.process()
