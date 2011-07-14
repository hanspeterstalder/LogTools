import glob
import os
from LogFileReader import LogFileReader

MERGED_LOG = "merged.log"

def mergeRecords(readers):
  """
  Merge MIP log-Files by using of the LogFileReader class
  """
  currentRecords = [reader.GetNextRecord() for reader in readers]
  while 1:

    minIndex = min(range(len(readers)), key=lambda index: currentRecords[index])

    yield currentRecords[minIndex]

    newRecord = readers[minIndex].GetNextRecord()
    if not newRecord:
      # There are no more records on current log-file
      del currentRecords[minIndex]
      del readers[minIndex]
    else:
      currentRecords[minIndex] = newRecord

    if len(readers) <= 0:
      # There are no more active log files
      raise StopIteration


if __name__ == '__main__':
  if os.path.exists(MERGED_LOG):
    os.remove(MERGED_LOG)

  logFiles = glob.glob('*.log*')
  print(logFiles)

  readers = []

  for file in logFiles:
    readers.append(LogFileReader(file))

  target = open(MERGED_LOG, mode='w')
  target.write("Date:135|Thread:62|Level:62|Logger:300|Message[EOL]\n")

  for record in mergeRecords(readers):
    target.write(record)

