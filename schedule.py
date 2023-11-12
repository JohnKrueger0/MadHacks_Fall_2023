from session import Session
class Schedule:
    busyTimes = []
    classInfo = []
    addedSessions = []  # To store added sessions

    def __init__(self, busyTimes, classInfo):
        self.busyTimes = busyTimes
        self.classInfo = classInfo

    def AddSession(self, session):
        for day in range(len(self.busyTimes)):
            session_times = session.times[day]
            session_locs = session.locs[day]
            session_nums = session.nums[day]

            for i, time in enumerate(session_times):
                if not time:  # If there is no session for this day
                    continue

                for busy_time in self.busyTimes[day]:
                    if self.timeConflict(time, busy_time):
                        # Conflict found, return False with the conflicting loc and num
                        return False, session_locs[i], session_nums[i]

                # If no conflict, add session time, loc, and num to the schedule
                self.busyTimes[day].append(time)
                self.classInfo.append((session.title, session.prof, session_locs[i], session_nums[i]))

        self.addedSessions.append(session)  # Add the session to the list of added sessions
        return True, None, None

    def timeConflict(self, time1, time2):
        # Check for time overlap
        return not (time1[1] <= time2[0] or time1[0] >= time2[1])

    def printSchedule(self):
        for session in self.addedSessions:
            print(f"Title: {session.title}, Professor: {session.prof}")
            for day, times, locs, nums in zip(range(len(session.times)), session.times, session.locs, session.nums):
                for time, loc, num in zip(times, locs, nums):
                    if time:
                        print(f"Day {day+1}: Time {time}, Location {loc}, Number {num}")



busy_times = [
    [(800, 900), (1000, 1100)],  # Monday
    [(830, 930), (1030, 1130)],  # Tuesday
    [(845, 945), (1045, 1145)],  # Wednesday
    [(845, 945), (1045, 1145)],  # Thursday
    [(845, 945), (1045, 1145)],  # Friday
    [(845, 945), (1045, 1145)]   # Saturday
]

my_schedule = Schedule(busy_times, [])

session_info = Session('Title', 'LKSDJF', 'MWF 2:00am - 3:50am', 'Helen C White', 'LEC 069', 'MF 3:30pm - 4:20pm', 'E-Hall', 'DIS 001', '', '', '')
print(session_info.times)
print(session_info.locs)
print(session_info.nums)

result, conflict_loc, conflict_num = my_schedule.AddSession(session_info)
if result:
    print("Session added successfully.")
    my_schedule.printSchedule()

else:
    print(f"Session conflicts with the existing schedule. Location: {conflict_loc}, Number: {conflict_num}")
