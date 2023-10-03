import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,
{
    'databaseURL': "https://realtimefaceattendance-3c6e9-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')
data = {
    "20BCD7027":
        {
            "name": "Eyashita Singh",
            "major": "Data Analytics",
            "starting_year": 2020,
            "total_attendance": 10,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "20BCI7028":
        {
            "name": "Rakesh Gupta",
            "major": "Computer Science",
            "starting_year": 2021,
            "total_attendance": 4,
            "standing": "G",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:34:23"
        },
    "20BCN7023":
        {
            "name": "Suhana Sharma",
            "major": "Computer Science with Iot",
            "starting_year": 2023,
            "total_attendance": 2,
            "standing": "G",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:23:02"
        },
    "20BES2093":
        {
            "name": "Elon Musk",
            "major": "Computer Science",
            "starting_year": 2020,
            "total_attendance": 8,
            "standing": "G",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:02:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
