class Session:
    times = []
    nums = []
    locs = []
    titles = []
    profs = []

    def __init__(self, title, prof, lecTime, lecLoc, lecNum, disTime, disLoc, disNum, labTime, labLoc, labNum):
        self.title = title
        self.prof = prof
        self.times, self.locs, self.nums, self.profs, self.titles = self.timesToBusyTimes(lecTime, lecLoc, lecNum)
        self.addBusyTime(self.timesToBusyTimes(disTime, disLoc, disNum))
        self.addBusyTime(self.timesToBusyTimes(labTime, labLoc, labNum))

    def timesToBusyTimes(self, _time, _loc, _num):
        _times = []
        _locs = []
        _nums = []
        _profs = []
        _titles = []
        index = _time.find(' ')
        days = _time[:index]
        hours = _time[index+1:]
        for i in range(6):
            update = False
            if i == 0 and days.find('M') >= 0:
                update = True #_times.append([self.toMilitaryTuple(hours)])
            elif i == 1 and days.find('T') >= 0:
                update = True #_times.append([self.toMilitaryTuple(hours)])
            elif i == 2 and days.find('W') >= 0:
                update = True #_times.append([self.toMilitaryTuple(hours)])
            elif i == 3 and days.find('R') >= 0:
                update = True #_times.append([self.toMilitaryTuple(hours)])
            elif i == 4 and days.find('F') >= 0:
                update = True #_times.append([self.toMilitaryTuple(hours)])
            elif i == 5 and days.find('S') >= 0:
               update = True # _times.append([self.toMilitaryTuple(hours)])
            
            if update:
                _times.append([self.toMilitaryTuple(hours)])
                _locs.append([_loc])
                _nums.append([_num])
                _profs.append([self.prof])
                _titles.append([self.title])

            else:
                _times.append([])
                _locs.append([])
                _nums.append([])
                _profs.append([])
                _titles.append([])

        return (_times, _locs, _nums, _profs, _titles)

    def toMilitaryTuple(self, _time):
        _times = _time.split(' - ')
        start = _times[0]
        end = _times[1]

        startHour = start.split(':')[0]
        startMin = start.split(':')[1][:-2]
        startAm = start[-2:] == 'am'
        endHour = end.split(':')[0] 
        endMin = end.split(':')[1][:-2]
        endAm = end[-2:] == 'am'

        startMil = str(int(startHour) + (0 if startAm else 12)) + startMin
        endMil = str(int(endHour) + (0 if endAm else 12)) + endMin

        return (int(startMil), int(endMil))
    
    def addBusyTime(self, newBusy):
        newBusyTime, newBusyLoc, newBusyNum, newBusyProf, newBusyTitle = newBusy[0], newBusy[1], newBusy[2], newBusy[3], newBusy[4]
        for day in range(len(self.times)):
            if newBusyTime[day] == []:
                pass
            elif self.times[day] == [] and newBusyTime[day] != []:
                self.times[day] = newBusyTime[day]
                self.locs[day] = newBusyLoc[day]
                self.nums[day] = newBusyNum[day]
                self.profs[day] = newBusyProf[day]
                self.titles[day] = newBusyTitle[day]
            else:
                self.times[day] = self.times[day] + newBusyTime[day]
                self.locs[day] = self.locs[day] + newBusyLoc[day]
                self.nums[day] = self.nums[day] + newBusyNum[day]
                self.profs[day] = self.profs[day] + newBusyProf[day]
                self.titles[day] = self.titles[day] + newBusyTitle[day]
