from pathlib import Path
import json
class bcolor:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
from datetime import datetime
dt = datetime.now()
current_day = dt.isoweekday()

script_dir = Path(__file__).resolve().parent
routines_folder = script_dir / "Routines"
routines_folder.mkdir(parents=True, exist_ok=True)
file_path = routines_folder / "monday_routines.json"
try:
    with open(file_path, "x", encoding="utf-8") as file:
        file.write(json.dumps({
            "routines": []
        }))
    print(f"{bcolor.OKGREEN}monday_routines.json didn't exist. Successfully created and wrote data.{bcolor.ENDC}")
except FileExistsError:
    pass
except Exception as e:
    print(f"{bcolor.FAIL}An error occurred while creating or writing to monday_routines.json: {e}{bcolor.ENDC}")
file_path = routines_folder / "tuesday_routines.json"
try:
    with open(file_path, "x", encoding="utf-8") as file:
        file.write(json.dumps({
            "routines": []
        }))
    print(f"{bcolor.OKGREEN}tuesday_routines.json didn't exist. Successfully created and wrote data.{bcolor.ENDC}")
except FileExistsError:
    pass
except Exception as e:
    print(f"{bcolor.FAIL}An error occurred while creating or writing to tuesday_routines.json: {e}{bcolor.ENDC}")
file_path = routines_folder / "wednesday_routines.json"
try:
    with open(file_path, "x", encoding="utf-8") as file:
        file.write(json.dumps({
            "routines": []
        }))
    print(f"{bcolor.OKGREEN}wednesday_routines.json didn't exist. Successfully created and wrote data.{bcolor.ENDC}")
except FileExistsError:
    pass
except Exception as e:
    print(f"{bcolor.FAIL}An error occurred while creating or writing to wednesday_routines.json: {e}{bcolor.ENDC}")
file_path = routines_folder / "thursday_routines.json"
try:
    with open(file_path, "x", encoding="utf-8") as file:
        file.write(json.dumps({
            "routines": []
        }))
    print(f"{bcolor.OKGREEN}thursday_routines.json didn't exist. Successfully created and wrote data.{bcolor.ENDC}")
except FileExistsError:
    pass
except Exception as e:
    print(f"{bcolor.FAIL}An error occurred while creating or writing to thursday_routines.json: {e}{bcolor.ENDC}")
file_path = routines_folder / "friday_routines.json"
try:
    with open(file_path, "x", encoding="utf-8") as file:
        file.write(json.dumps({
            "routines": []
        }))
    print(f"{bcolor.OKGREEN}friday_routines.json didn't exist. Successfully created and wrote data.{bcolor.ENDC}")
except FileExistsError:
    pass
except Exception as e:
    print(f"{bcolor.FAIL}An error occurred while creating or writing to friday_routines.json: {e}{bcolor.ENDC}")
file_path = routines_folder / "saturday_routines.json"
try:
    with open(file_path, "x", encoding="utf-8") as file:
        file.write(json.dumps({
            "routines": []
        }))
    print(f"{bcolor.OKGREEN}saturday_routines.json didn't exist. Successfully created and wrote data.{bcolor.ENDC}")
except FileExistsError:
    pass
except Exception as e:
    print(f"{bcolor.FAIL}An error occurred while creating or writing to saturday_routines.json: {e}{bcolor.ENDC}")
file_path = routines_folder / "sunday_routines.json"
try:
    with open(file_path, "x", encoding="utf-8") as file:
        file.write(json.dumps({
            "routines": []
        }))
    print(f"{bcolor.OKGREEN}sunday_routines.json didn't exist. Successfully created and wrote data.{bcolor.ENDC}")
except FileExistsError:
    pass
except Exception as e:
    print(f"{bcolor.FAIL}An error occurred while creating or writing to sunday_routines.json: {e}{bcolor.ENDC}")


file_path = routines_folder / "monday_routines.json"
with file_path.open(encoding="utf-8") as file:
    monday_routines = json.load(file)
file_path = routines_folder / "tuesday_routines.json"
with file_path.open(encoding="utf-8") as file:
    tuesday_routines = json.load(file)
file_path = routines_folder / "wednesday_routines.json"
with file_path.open(encoding="utf-8") as file:
    wednesday_routines = json.load(file)
file_path = routines_folder / "thursday_routines.json"
with file_path.open(encoding="utf-8") as file:
    thursday_routines = json.load(file)
file_path = routines_folder / "friday_routines.json"
with file_path.open(encoding="utf-8") as file:
    friday_routines = json.load(file)
file_path = routines_folder / "saturday_routines.json"
with file_path.open(encoding="utf-8") as file:
    saturday_routines = json.load(file)
file_path = routines_folder / "sunday_routines.json"
with file_path.open(encoding="utf-8") as file:
    sunday_routines = json.load(file)


class routine_adder:
    def routine(self, day, name, time, duration, subdurations):
        if day == "monday" or day == 1:
            monday_routine = {
                "name": name,
                "time": time,
                "duration": duration,
                "subdurations": subdurations
                }

            

        elif day == "tuesday" or day == 2:
            tuesday_routine = {
                "name": name,
                "time": time,
                "duration": duration,
                "subdurations": subdurations
            }

        elif day == "wednesday" or day == 3:
            wednesday_routine = {
                "name": name,
                "time": time,
                "duration": duration,
                "subdurations": subdurations
            }

        elif day == "thursday" or day == 4:
            thursday_routine = {
                "name": name,
                "time": time,
                "duration": duration,
                "subdurations": subdurations
            }

        elif day == "friday" or day == 5:
            friday_routine = {
                "name": name,
                "time": time,
                "duration": duration,
                "subdurations": subdurations
            }

        elif day == "saturday" or day == 6:
            saturday_routine = {
                "name": name,
                "time": time,
                "duration": duration,
                "subdurations": subdurations
            }

        elif day == "sunday" or day == 7:
            sunday_routine = {
                "name": name,
                "time": time,
                "duration": duration,
                "subdurations": subdurations
            }

    def time(self, day, name, time):
        pass

    def duration(self, day, name, duration):
        pass

    def subdurations(self, day, name, subdurations):
        pass


class routine_clearer:
    def day(self, day):
        pass

    def routine(self, day, name):
        pass

    def time(self, day, name):
        pass

    def duration(self, day, name):
        pass

    def subdurations(self, day, name):
        pass

class routine_edit:
    def day(self, day):
        pass

    def routine(self, day, name):
        pass

    def time(self, day, name, time):
        pass

    def duration(self, day, name, duration):
        pass

    def subdurations(self, day, name, subdurations):
        pass

class routine_reader:
    def routine(self, day):
        if day == 1:
            if monday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(monday_routines["routines"])):
                    print(f"{i + 1}. {monday_routines["routines"][i]["name"]}", end = " ") if monday_routines["routines"][i]["name"] is not None else None
                    print(f"for {monday_routines["routines"][i]["duration"]} minutes", end = " ") if monday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {monday_routines["routines"][i]["time"]}") if monday_routines["routines"][i]["time"] is not None else None
            else:
                print("No routine today!")
        elif day == 2:
            if tuesday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(tuesday_routines["routines"])):
                    print(f"{i + 1}. {tuesday_routines["routines"][i]["name"]}", end = " ") if tuesday_routines["routines"][i]["name"] is not None else None
                    print(f"for {tuesday_routines["routines"][i]["duration"]} minutes", end = " ") if tuesday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {tuesday_routines["routines"][i]["time"]}") if tuesday_routines["routines"][i]["time"] is not None else None
            else:
                print("No routine today!")
        elif day == 3:
            if wednesday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(wednesday_routines["routines"])):
                    print(f"{i + 1}. {wednesday_routines["routines"][i]["name"]}", end = " ") if wednesday_routines["routines"][i]["name"] is not None else None
                    print(f"for {wednesday_routines["routines"][i]["duration"]} minutes", end = " ") if wednesday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {wednesday_routines["routines"][i]["time"]}") if wednesday_routines["routines"][i]["time"] is not None else None
            else:
                print("No routine today!")
        elif day == 4:
            if thursday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(thursday_routines["routines"])):
                    print(f"{i + 1}. {thursday_routines["routines"][i]["name"]}", end = " ") if thursday_routines["routines"][i]["name"] is not None else None
                    print(f"for {thursday_routines["routines"][i]["duration"]} minutes", end = " ") if thursday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {thursday_routines["routines"][i]["time"]}") if thursday_routines["routines"][i]["time"] is not None else None
            else:
                print("No routine today!")
        elif day == 5:
            if friday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(friday_routines["routines"])):
                    print(f"{i + 1}. {friday_routines["routines"][i]["name"]}", end = " ") if friday_routines["routines"][i]["name"] is not None else None
                    print(f"for {friday_routines["routines"][i]["duration"]} minutes", end = " ") if friday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {friday_routines["routines"][i]["time"]}") if friday_routines["routines"][i]["time"] is not None else None
            else:
                print("No routine today!")
        elif day == 6:
            if saturday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(saturday_routines["routines"])):
                    print(f"{i + 1}. {saturday_routines["routines"][i]["name"]}", end = " ") if saturday_routines["routines"][i]["name"] is not None else None
                    print(f"for {saturday_routines["routines"][i]["duration"]} minutes", end = " ") if saturday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {saturday_routines["routines"][i]["time"]}") if saturday_routines["routines"][i]["time"] is not None else None
            else:
                print("No routine today!")
        else:
            if sunday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(sunday_routines["routines"])):
                    print(f"{i + 1}. {sunday_routines["routines"][i]["name"]}", end = " ") if sunday_routines["routines"][i]["name"] is not None else None
                    print(f"for {sunday_routines["routines"][i]["duration"]} minutes", end = " ") if sunday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {sunday_routines["routines"][i]["time"]}") if sunday_routines["routines"][i]["time"] is not None else None
            else:
                print("No routine today!")

class routine_editor:
    def __init__(self):
        self.add = routine_adder()
        self.clear = routine_clearer()
        self.edit = routine_edit()
        self.read = routine_reader()
routine = routine_editor()


action = int(input("What routine tool would you like to use?\n1. Routine adder (for adding routines or information to routines)\n2. Routine clearer (for removing a routine a whole day or infos from a routine)\n3. Routine editor (for editing various information about a routine)\n4. Routine reader (for printing todays routines)"))
if action == 1:
    adder_option = int(input("What would you like to add?\n1. A routine\n2. A time to a routine without time\n3. A duration to a routine with no duration\n4. A subduration to a routine with a duration"))
    if adder_option == 1:



