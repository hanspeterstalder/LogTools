class Statistic:
    def __init__(self):
       self.data = {}

    def addValue(self, value):
        if value in self.data:
            self.data[value] += 1
        else:
            self.data[value] = 1

    def printStatistic(self):
        keyList = list(self.data.keys())
        keyList.sort()
        for key in keyList:
          print(key, self.data[key])

