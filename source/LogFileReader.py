class LogFileReader:
  def __init__(self, fileName):
    self.file = open(fileName)
    self.firstLine = True

  def GetNextRecord(self):
    entry = ""

    while 1:
      line = self.file.readline()

      if not line:
        return None
        break

      if self.firstLine:
        self.firstLine = False
        continue
      if line.endswith("[EOL]\n"):
        entry = entry + line
        return entry
      else:
        entry = entry + line

