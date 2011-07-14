"""
The different commands running with the FileProcessor class
"""

from Statistic import Statistic

class BaseCommand:
  def execute(self, record):
    print(record)

  def printResult(self):
    return


class StatisticCommand(BaseCommand):
  def __init__(self):
    self.levelStatistic = Statistic()
    self.threadStatistic = Statistic()
    self.loggerStatistic = Statistic()
    self.timeStatistic = Statistic()
    self.entries = 0
    super().__init__()

  def execute(self, record):
    self.levelStatistic.addValue(record[2])
    self.threadStatistic.addValue(record[1])
    self.loggerStatistic.addValue(record[3])
    self.processTime(record)
    self.entries += 1

  def printResult(self):
    print("logfile has", self.entries, "entries\n")

    print("\nLog level\n---------")
    self.levelStatistic.printStatistic()
    print("\nThreads\n-------")
    self.threadStatistic.printStatistic()
    print("\nLogger\n------")
    self.loggerStatistic.printStatistic()
    print("\nTime\n----")
    self.timeStatistic.printStatistic()

  def processTime(self, record):
    time = record[0][0:16]
    self.timeStatistic.addValue(time)


class FilterCommad(BaseCommand):
  def __init__(self, pattern):
    self.pattern = pattern
    super().__init__()

  def execute(self, record):
    found = False
    for s in record:
      if s.find(self.pattern) != -1:
        found = True
        break
    if found == True:
        print(record)

  def printResult(self):
    super().printResult()


class ReportFatalErrorCommand(BaseCommand):
  def __init__(self):
    super().__init__()

  def execute(self, record):
    if record[2] == "FATAL":
      print("{0}: Fatal Error from {1} occurred: {2}".format(record[0], record[3], record[4]).strip())

class ReportErrorErrorCommand(BaseCommand):
  def __init__(self):
    super().__init__()

  def execute(self, record):
    if record[2] == "ERROR":
      print("{0}: Error from {1} received: {2}".format(record[0], record[3], record[4]).strip())

class ReportOutOfMemoryCommand(BaseCommand):
  def __init__(self):
    super().__init__()

  def execute(self, record):
    if "OutOfMemory" in record[4]:
      print("{0}: OutOfMemory Occurred".format(record[0]).strip())

class ReportTraceArrayCommand(BaseCommand):
  def __init__(self):
    super().__init__()

  def execute(self, record):
    if "TraceArray_" in record[4]:
      print("{0}: {1}".format(record[0], record[4][78:]).strip())

class ReportWizardFSMCommand(BaseCommand):
  def __init__(self):
    super().__init__()

  def execute(self, record):
    if record[4].startswith("[Wizard FSM] Performed"):
      print("{0}: Wizard event processing: {1}".format(record[0], record[4]).strip())

class ReportAnDIFSMCommand(BaseCommand):
  def __init__(self):
    super().__init__()

  def execute(self, record):
    if record[4].startswith("[AnDI FSM] Performed"):
      print("{0}: Z480 event processing: {1}".format(record[0], record[4]).strip())

class ReportSpiFSMCommand(BaseCommand):
  def __init__(self):
    super().__init__()

  def execute(self, record):
    if record[4].startswith("[SPI FSM] Performed"):
      print("{0}: X480 event processing: {1}".format(record[0], record[4]).strip())

class ReportSpiRunFSMCommand(BaseCommand):
  def __init__(self):
    super().__init__()

  def execute(self, record):
    if record[4].startswith("[SPI run FSM] Performed"):
      print("{0}: X480RUN event processing: {1}".format(record[0], record[4]).strip())

class ReportNewRunCommand(BaseCommand):
  def __init__(self):
    super().__init__()

  def execute(self, record):
    if record[4].startswith("Run created; orderId:"):
      print("{0}: New Run Created: {1}".format(record[0], record[4]).strip())

class ReportApplicationLoaderCommand(BaseCommand):
  def __init__(self):
    super().__init__()

  def execute(self, record):
    if record[3] == "Roche.Mip.Loader.ApplicationLoader":
      print("{0}: Application Loader: {1}".format(record[0], record[4]).strip())
