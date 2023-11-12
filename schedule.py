class Schedule:
    busyTimes = []
    classInfo = []

    def __init__(self, busyTimes, classInfo):
        self.busyTimes = busyTimes
        self.classInfo = classInfo


    def AddSession(self, SessionFullInfo):
        dumbTimes = SessionFullInfo.times

        for day, busy_day_times in enumerate(self.busyTimes):

            for busy_time in busy_day_times:
                busy_start, busy_end = busy_time
                session_start, session_end = dumbTimes

                if session_start <= busy_end and session_end >= busy_start:
                    return False  

        return True  

            
busy_times = [
    [(800, 900), (1000, 1100)],  # Monday
    [(830, 930), (1030, 1130)],  # Tuesday
    [(845, 945), (1045, 1145)]   # Wednesday
    [(845, 945), (1045, 1145)]   # Thursday
    [(845, 945), (1045, 1145)]   # Friday
    [(845, 945), (1045, 1145)]   # Saturday
]

my_schedule = Schedule(busy_times, [])

session_info = {
    "times": (915, 1030)  
}


result = my_schedule.AddSession(session_info)
print(result)
if result:
    print("Session added successfully.")
else:
    print("Session conflicts with existing schedule.")

session_info = {
    "times": (930, 1000)  # Wednesday session doesn't overlap with busy times
}

result = my_schedule.AddSession(session_info)
if result:
    print("Session added successfully.")
else:
    print("Session conflicts with existing schedule.")
