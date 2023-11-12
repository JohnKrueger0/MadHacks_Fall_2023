import pymongo
from pymongo import MongoClient
from session import Session
from schedule import Schedule
import copy

classOptions = [['MATH 234', 'MATH 320', 'MATH 340'], ['M E 231', 'ME 201'], ['E C E 252', 'COMP SCI 200', 'COMP SCI 220'], ['HISTORY 101', 'HISTORY 102', 'HISTORY 151']]

def getSchedules():
    client = MongoClient('mongodb+srv://asanthanakri:dumbass@cluster0.9esju.mongodb.net/?retryWrites=true&w=majority')

    #Searching for each of these classes
    db = client['myDatabase']
    collection = db['CourseInfo']

    classSessions = []
    for cat in range(len(classOptions)):
        categorySessions = []
        for cl in range(len(classOptions[cat])):
            foundSessions = list(collection.find({"Class Title": classOptions[cat][cl]}))
            for foundSess in foundSessions:
                categorySessions.append(Session(dict(foundSess)))
        classSessions.append(categorySessions)

    validSchedules = []
    for cat1 in range(len(classSessions[0])):
        sched1 = Schedule()
        sched1.AddSession(classSessions[0][cat1])
        
        for cat2  in range(len(classSessions[1])):
            sched2 = copy.deepcopy(sched1)
            added = sched2.AddSession(classSessions[1][cat2])
            if not added:
                break

            for cat3  in range(len(classSessions[2])):
                sched3 = copy.deepcopy(sched2)
                added = sched3.AddSession(classSessions[2][cat3])
                if not added:
                    break
                
                for cat4  in range(len(classSessions[3])):
                    sched4 = copy.deepcopy(sched3)
                    added = sched4.AddSession(classSessions[3][cat4])
                    if not added:
                        break

                    validSchedules.append(sched4)

    print('Valid Scheudle #', len(validSchedules))    

    return validSchedules

print(getSchedules()[2].paintSchedule())