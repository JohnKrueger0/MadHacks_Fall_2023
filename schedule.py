from PIL import Image, ImageDraw

from session import Session
class Schedule:
    times = []
    nums = []
    locs = []
    titles = []
    profs = []
    #busyTimes = []
    #classInfo = []
    #addedSessions = []  # To store added sessions

    def __init__(self):
        self.times = self.getEmptyWeek()
        self.nums = self.getEmptyWeek()
        self.locs = self.getEmptyWeek()
        self.titles = self.getEmptyWeek()
        self.profs = self.getEmptyWeek()

    def getEmptyWeek(self):
        empty = []
        for i in range(6):
            empty.append([])
        return empty

    def AddSession(self, session):
        session_times = session.times
        session_locs = session.locs
        session_nums = session.nums
        session_titles = session.titles
        session_profs = session.profs
        for day in range(len(self.times)):

            if session_times[day] == []:
                pass
            elif self.times[day] == [] and session_times[day] != []:
                self.times[day] = session_times[day]
                self.locs[day] = session_locs[day]
                self.nums[day] = session_nums[day]
                self.titles[day] = session_titles[day]
                self.profs[day] = session_profs[day]
            else:
                for t1 in self.times[day]:
                    for t2 in session_times[day]:
                        if self.timeConflict(t1, t2):
                            return False

                self.times[day] = self.times[day] + session_times[day]
                self.locs[day] = self.locs[day] + session_locs[day]
                self.nums[day] = self.nums[day] + session_nums[day]
                self.titles[day] = self.titles[day] + session_titles[day]
                self.profs[day] = self.profs[day] + session_profs[day]

        #     for i, time in enumerate(session_times):
        #         if not time:  # If there is no session for this day
        #             continue

        #         for busy_time in self.busyTimes[day]:
        #             if self.timeConflict(time, busy_time):
        #                 # Conflict found, return False with the conflicting loc and num
        #                 return False, session_locs[i], session_nums[i]

        #         # If no conflict, add session time, loc, and num to the schedule
        #         self.busyTimes[day].append(time)
        #         self.classInfo.append((session.title, session.prof, session_locs[i], session_nums[i]))

        # self.addedSessions.append(session)  # Add the session to the list of added sessions
        return True

    def timeConflict(self, time1, time2):
        # Check for time overlap
        return not (time1[1] <= time2[0] or time1[0] >= time2[1])

    # def printSchedule(self):
    #     for session in self.addedSessions:
    #         print(f"Title: {session.title}, Professor: {session.prof}")
    #         for day, times, locs, nums in zip(range(len(session.times)), session.times, session.locs, session.nums):
    #             for time, loc, num in zip(times, locs, nums):
    #                 if time:
    #                     print(f"Day {day+1}: Time {time}, Location {loc}, Number {num}")

    def paintSchedule(self):
        rawTimes = []
        for day in self.times:
            for sess in day:
                rawTimes.append(sess[0])
                rawTimes.append(sess[1])
        
        minTimes = round(min(rawTimes), -2)-100
        maxTimes = round(max(rawTimes), -2)
        print(minTimes, maxTimes)

        img = Image.new('RGB', (1920, 1080), color = (255,255,255))
        draw = ImageDraw.Draw(img)  
        

        v_start = 200
        v_end = 900
        v_inc = (v_end - v_start) / (maxTimes - minTimes) * 100
        print(v_inc)
        for i in range(int((maxTimes-minTimes)/100)):
            draw.line(((250, v_start + i * v_inc), (1800, v_start + i * v_inc)), fill=256)
        img.show()
        #print(times_1d)

# [[(1100, 1150), (1530, 1620)], [], [(1100, 1150)], [], [(1100, 1150), (1530, 1620)], []]
# [['Helen C White', 'E-Hall'], [], ['Helen C White'], [], ['Helen C White', 'E-Hall'], []]
# [['LEC 069', 'DIS 001'], [], ['LEC 069'], [], ['LEC 069', 'DIS 001'], []]

#times = [[(1100, 1150), (1530, 1620)], [], [(1100, 1150)], [], [(1100, 1150), (1530, 1620)], []]

#times_1d  = [item for sub_list in times for item in sub_list]
#print(times_1d)
#startTime = min(times))

#print(startTime)

# busy_times = [
#     [(800, 900), (1000, 1100)],  # Monday
#     [(830, 930), (1030, 1130)],  # Tuesday
#     [(845, 945), (1045, 1145)],  # Wednesday
#     [(845, 945), (1045, 1145)],  # Thursday
#     [(845, 945), (1045, 1145)],  # Friday
#     [(845, 945), (1045, 1145)]   # Saturday
# ]

my_schedule = Schedule()

session_info = Session('Title', 'LKSDJF', 'MWF 11:00am - 11:50am', 'Helen C White', 'LEC 069', 'MF 3:30pm - 4:20pm', 'E-Hall', 'DIS 001', '', '', '')
print(session_info.times)
print(session_info.locs)
print(session_info.nums)

result = my_schedule.AddSession(session_info)
if result:
    print("Session added successfully.")
    #my_schedule.printSchedule()
    my_schedule.paintSchedule()

else:
    print(f"Session conflicts with the existing schedule. Location: {conflict_loc}, Number: {conflict_num}")
