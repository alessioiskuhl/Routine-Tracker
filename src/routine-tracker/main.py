from pathlib import Path
import json
from datetime import datetime

dt = datetime.now()
file_path = Path(__file__).parent / "Routines" / "monday_routines.json"

with file_path.open(encoding="utf-8") as file:
    monday_routine = json.load(file)
file_path = Path(__file__).parent / "Routines" / "tuesday_routines.json"
with file_path.open(encoding="utf-8") as file:
    tuesday_routine = json.load(file)
file_path = Path(__file__).parent / "Routines" / "wednesday_routines.json"
with file_path.open(encoding="utf-8") as file:
    wednesday_routine = json.load(file)
file_path = Path(__file__).parent / "Routines" / "thursday_routines.json"
with file_path.open(encoding="utf-8") as file:
    thursday_routine = json.load(file)
file_path = Path(__file__).parent / "Routines" / "sunday_routines.json"
with file_path.open(encoding="utf-8") as file:
    sunday_routine = json.load(file)

if dt.isoweekday() == 1:
    print("Monday Routine:", monday_routine)
elif dt.isoweekday() == 2:
    print("Tuesday Routine:", tuesday_routine)
elif dt.isoweekday() == 3:
    print("Wednesday Routine:", wednesday_routine)
elif dt.isoweekday() == 4:
    print("Thursday Routine:", thursday_routine)
elif dt.isoweekday() == 5:
    pass
elif dt.isoweekday() == 6:
    pass
else:
    print("Sunday Routine:", sunday_routine)