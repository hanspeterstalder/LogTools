"""
Simple Tools for the MIP log files
"""
import sys
from Commands import BaseCommand, StatisticCommand, FilterCommad
from FileProcessor import FileProcessor

CmdStatistic = "-S"
CmdFilter = "-F"
CmdPrint = "-P"

def usage():
  """
  Prints the usage of the script
  """
  print("Usage: MipLogTool.py logFileName [-F|-S]")
  print("-S generates statistic of the log file")
  print("-F \"pattern\" get the records were the pattern matches")

def evaluateCommand(args):
  """
  Evaluates the command who should be executed.
  """
  if len(args) < 2:
    usage()
    exit()
  elif len(args) == 2:
    return BaseCommand()
  elif args[2] == CmdFilter:
    if len(args) < 4:
      usage()
      exit()
    return FilterCommad(args[3])
  elif args[2] == CmdPrint:
    return BaseCommand()
  elif args[2] == CmdStatistic:
    return StatisticCommand()
  else:
    usage()
    exit()

fileProcessor = FileProcessor(sys.argv[1], [evaluateCommand(sys.argv)])
fileProcessor.process()

