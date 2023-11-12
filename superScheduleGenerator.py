import pymongo
from pymongo import MongoClient
from session import Session
from schedule import Schedule
import copy

classOptions = [['MATH 320', 'MATH 340', 'MATH 341', 'MATH 234'], ['PHYSICS 202', 'PHYSICS 201', 'E M A 201', 'E M A 202'], ['COMP SCI 220', 'E C E 252', 'COMP SCI 200'], ['HISTORY 120', 'HISTORY 101', 'HISTORY 329']]
wGpa = 0
wMorning = 1
wEvening = 0


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

def sortSchedules(schedules):
    client = MongoClient('mongodb+srv://asanthanakri:dumbass@cluster0.9esju.mongodb.net/?retryWrites=true&w=majority')
    db = client['NewDatabase']
    collection = db['NewCollection']

    classCache = {}

    scheduleScores = []

    #schedules[i].paintSchedule()

    for schedule in schedules:
        classList = schedule.getClasses()
        gpaList = []
        for cl in classList:
            if not cl in classCache:
                classCache[cl] = collection.find_one({'Class Title': cl})['GPA']
            gpaList.append(classCache[cl])

        scheduleScores.append(schedule.getScore(gpaList, wGpa, wMorning, wEvening))

    sorted_schedules = [x for _, x in sorted(zip(scheduleScores, schedules), key=lambda pair: pair[0])]

    
    sorted_schedules.reverse()
    return sorted_schedules[0]


#sortSchedules(getSchedules()).paintSchedule()

from flask import Flask, render_template
from io import BytesIO
from PIL import Image
import base64

app = Flask(__name__)

@app.route('/')
def index():
    # Create a sample image with PIL (you may already have an image)
    # Replace this with your image creation logic
    width, height = 300, 200
    img = Image.new('RGB', (width, height), color='red')

    # Convert the PIL image to a base64 encoded string
    buffered = BytesIO()
    img.save(buffered, format="JPEG")
    img_str = base64.b64encode(buffered.getvalue()).decode('utf-8')

    img_data = "data:image/jpeg;base64," + img_str

    return render_template('index.html', img_data=img_data)

if __name__ == '__main__':
    app.run(debug=True)
