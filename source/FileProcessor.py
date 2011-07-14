from datetime import time, datetime

MipLog4NetDateTimeFormat = "%Y-%m-%d %H:%M:%S,%f"

class FileProcessor:
    def __init__(self, filename, commands):
      self.filename = filename
      self.commands = commands

    def getRecord(self, entry):
      return entry.split("|")

    def ParseDateTime(self, timeString):
      return datetime.strptime(timeString, MipLog4NetDateTimeFormat)

    def process(self):
      entry = ""
      firstLine = True

      file = open(self.filename)

      for line in file:
        if firstLine:
          firstLine = False
          continue
        if line.endswith("[EOL]\n"):
          entry = entry + line
          record = self.getRecord(entry)

          recordTimeStamp = self.ParseDateTime(record[0])

          for command in self.commands:
            command.execute(record)

          entry = ''
        else:
          entry = entry + line

      for command in self.commands:
        command.printResult()
