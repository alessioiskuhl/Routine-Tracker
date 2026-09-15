"""A simple routine tracker that allows you to track and time your daily routines."""


from itertools import islice
import time
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
from datetime import datetime, timedelta
dt = datetime.now()
current_day = dt.isoweekday()
current_date = datetime.today().strftime('%Y-%m-%d')
current_week = datetime.date(datetime.today()).isocalendar()[1]
current_month = datetime.today().month
yesterday_date = (datetime.today() - timedelta(days=1)).strftime('%Y-%m-%d')
last_week = current_week - 1 if current_week > 1 else 52
last_month = current_month - 1 if current_month > 1 else 12
last_year = datetime.today().year - 1

script_dir = Path(__file__).resolve().parent
statistics_folder = script_dir / "Statistics"
statistics_folder.mkdir(parents=True, exist_ok=True)
routines_folder = script_dir / "Routines"
routines_folder.mkdir(parents=True, exist_ok=True)
file_path = routines_folder / "monday_routines.json"
try:
    with open(file_path, "x", encoding="utf-8") as file:
        file.write(json.dumps({
            "routines": [],
            f"progress{current_date}" : []
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
            "routines": [],
            f"progress{current_date}" : []
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
            "routines": [],
            f"progress{current_date}" : []
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
            "routines": [],
            f"progress{current_date}" : []
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
            "routines": [],
            f"progress{current_date}" : []
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
            "routines": [],
            f"progress{current_date}" : []
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
            "routines": [],
            f"progress{current_date}" : []
        }))
    print(f"{bcolor.OKGREEN}sunday_routines.json didn't exist. Successfully created and wrote data.{bcolor.ENDC}")
except FileExistsError:
    pass
except Exception as e:
    print(f"{bcolor.FAIL}An error occurred while creating or writing to sunday_routines.json: {e}{bcolor.ENDC}")
file_path = statistics_folder / "statistics.json"
try:
    with open(file_path, "x", encoding="utf-8") as file:
        file.write(json.dumps({
            "statistics": [{
                f"completion rate today ({current_date})" : 0,
                f"completion rate this week ({current_week})" : 0,
                f"completion rate this month ({current_month})" : 0,
                f"completion rate this year ({datetime.today().year})" : 0,
                f"completion rate yesterday ({yesterday_date})" : 0,
                f"completion rate last week ({last_week})" : 0,
                f"completion rate last month ({last_month})" : 0,
                f"completion rate last year ({last_year})" : 0,
                "completion rate all time" : 0,
                f"completed routines today ({current_date})" : 0,
                f"remaining routines today ({current_date})" : 0,
                "total completions" : 0,
                
            }]
        }, indent=4))
    print(f"{bcolor.OKGREEN}statistics.json didn't exist. Successfully created and wrote data.{bcolor.ENDC}")
except FileExistsError:
    pass
except Exception as e:
    print(f"{bcolor.FAIL}An error occurred while creating or writing to statistics.json: {e}{bcolor.ENDC}")

DAY_FILES = {
    "monday": "monday_routines.json",
    "tuesday": "tuesday_routines.json",
    "wednesday": "wednesday_routines.json",
    "thursday": "thursday_routines.json",
    "friday": "friday_routines.json",
    "saturday": "saturday_routines.json",
    "sunday": "sunday_routines.json",
}
DAY_NUMBERS = {
    1: "monday",
    2: "tuesday",
    3: "wednesday",
    4: "thursday",
    5: "friday",
    6: "saturday",
    7: "sunday",
}

def _normalize_day(day):
    if isinstance(day, int):
            return DAY_NUMBERS[day]
    return str(day).lower()


path = routines_folder / f"{_normalize_day(current_day)}_routines.json"
with path.open(encoding="utf-8") as file:
    data = json.load(file)
if not len(list(data.keys())) > 1:
    data[f"progress{current_date}"] = []
    for routine in data["routines"]:
            data[f"progress{current_date}"].append({f"routine_{routine["name"]}_completed": False})
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
elif list(data.keys())[1] != f"progress{current_date}":
    del data[list(data.keys())[1]]
    data[f"progress{current_date}"] = []
    for routine in data["routines"]:
        data[f"progress{current_date}"].append({f"routine_{routine['name']}_completed": False})
    with path.open("w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)


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

class routine_progress:
    DAY_FILES = {
        "monday": "monday_routines.json",
        "tuesday": "tuesday_routines.json",
        "wednesday": "wednesday_routines.json",
        "thursday": "thursday_routines.json",
        "friday": "friday_routines.json",
        "saturday": "saturday_routines.json",
        "sunday": "sunday_routines.json",
    }
    DAY_NUMBERS = {
        1: "monday",
        2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday",
        6: "saturday",
        7: "sunday",
    }
    
    @classmethod
    def _normalize_day(cls, day):
        if isinstance(day, int):
                return cls.DAY_NUMBERS[day]
        return str(day).lower()
    
    def __init__(self):
        self.today = current_day
        current_routines = self.get_current_routines()
        self.current_date = datetime.today().strftime('%Y-%m-%d')

    def get_current_routines(self):
        day_name = self._normalize_day(self.today)
        path = routines_folder / f"{day_name}_routines.json"
        with path.open(encoding="utf-8") as file:
            data = json.load(file)
        return data["routines"]

    def complete(self, routine_name):
        print(f"completing {routine_name}")
        day_name = self._normalize_day(self.today)
        path = routines_folder / f"{day_name}_routines.json"
        with path.open(encoding="utf-8") as file:
            data = json.load(file)
            print(f"data loaded: {data}")

        for routine in data["routines"]:
            print(f"checking routine: {routine['name']}")
            if routine["name"] == routine_name:
                print(f"marking routine {routine_name} as complete")
                data[f"progress{self.current_date}"].append({f"routine_{routine_name}_completed": True})
                break
        else:
            raise ValueError(f"No routine found with name: {routine_name}")

        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    
class routine_adder:
    DAY_FILES = {
        "monday": "monday_routines.json",
        "tuesday": "tuesday_routines.json",
        "wednesday": "wednesday_routines.json",
        "thursday": "thursday_routines.json",
        "friday": "friday_routines.json",
        "saturday": "saturday_routines.json",
        "sunday": "sunday_routines.json",
    }
    DAY_NUMBERS = {
        1: "monday",
        2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday",
        6: "saturday",
        7: "sunday",
    }

    @classmethod
    def _normalize_day(cls, day):
        if isinstance(day, int):
            return cls.DAY_NUMBERS[day]
        return str(day).lower()

    @classmethod
    def _load_data(cls, day):
        day_name = cls._normalize_day(day)
        path = routines_folder / f"{day_name}_routines.json"
        with path.open(encoding="utf-8") as file:
            return path, json.load(file)

    @staticmethod
    def _save_data(path, data):
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def _set_field(self, day, name, field, value):
        day_name = self._normalize_day(day)
        path, data = self._load_data(day_name)

        for routine in data["routines"]:
            if routine["name"] == name:
                if routine.get(field) is not None:
                    raise AssertionError(f"{bcolor.FAIL}There is already a {field} for the routine {name} in your {day_name} routines{bcolor.ENDC}")
                routine[field] = value
                self._save_data(path, data)
                return f"{bcolor.OKGREEN}Successfully added {field} to the routine {name} in your {day_name} routines{bcolor.ENDC}"

        raise AssertionError(f"{bcolor.FAIL}There is no routine with the name {name} in your {day_name} routines{bcolor.ENDC}")


    def routine(self, day, name, time, duration, subdurations):
        day_name = self._normalize_day(day)
        path, data = self._load_data(day_name)

        new_routine = {
            "name": name,
            "time": time,
            "duration": duration,
            "subdurations": subdurations
        }

        for existing in data["routines"]:
            if existing["name"] == new_routine["name"]:
                raise Exception(f"{bcolor.FAIL}There is already a routine with the name {new_routine['name']} in your {day_name} routines{bcolor.ENDC}")

        data["routines"].append(new_routine)
        self._save_data(path, data)
        return f"{bcolor.OKGREEN}Successfully added routine {name} to your {day_name} routines{bcolor.ENDC}"

    def time(self, day, name, time):
        return self._set_field(day, name, "time", time)

    def duration(self, day, name, duration):
        return self._set_field(day, name, "duration", duration)

    def subdurations(self, day, name, subdurations):
        return self._set_field(day, name, "subdurations", subdurations)


class routine_clearer:
    DAY_FILES = {
        "monday": "monday_routines.json",
        "tuesday": "tuesday_routines.json",
        "wednesday": "wednesday_routines.json",
        "thursday": "thursday_routines.json",
        "friday": "friday_routines.json",
        "saturday": "saturday_routines.json",
        "sunday": "sunday_routines.json",
    }
    DAY_NUMBERS = {
        1: "monday",
        2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday",
        6: "saturday",
        7: "sunday",
    }
    
    @classmethod
    def _normalize_day(cls, day):
        if isinstance(day, int):
            return cls.DAY_NUMBERS[day]
        return str(day).lower()
    
    @classmethod
    def _load_data(cls, day):
        day_name = cls._normalize_day(day)
        path = routines_folder / f"{day_name}_routines.json"
        with path.open(encoding="utf-8") as file:
            return path, json.load(file)
    
    @staticmethod
    def _save_data(path, data):
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def _clear_day(self, day):
        day_name = self._normalize_day(day)
        path, data = self._load_data(day_name)

        if not data["routines"]:
            raise AssertionError(f"{bcolor.FAIL}There are no routines in your {day_name} routines to clear{bcolor.ENDC}")

        data["routines"] = []
        self._save_data(path, data)
        return f"{bcolor.OKGREEN}Successfully cleared all routines from your {day_name} routines{bcolor.ENDC}"

    def _clear_routine(self, day, name):
        day_name = self._normalize_day(day)
        path, data = self._load_data(day_name)

        for i, routine in enumerate(data["routines"]):
            if routine["name"] == name:
                del data["routines"][i]
                self._save_data(path, data)
                return f"{bcolor.OKGREEN}Successfully cleared the routine {name} from your {day_name} routines{bcolor.ENDC}"

        raise AssertionError(f"{bcolor.FAIL}There is no routine with the name {name} in your {day_name} routines{bcolor.ENDC}")
    
    def _clear_field(self, day, name, field):
        day_name = self._normalize_day(day)
        path, data = self._load_data(day_name)

        for routine in data["routines"]:
            if routine["name"] == name:
                if routine.get(field) is None:
                    raise AssertionError(f"{bcolor.FAIL}There is already no value in {field} for the routine {name} in your {day_name} routines{bcolor.ENDC}")
                routine[field] = None
                self._save_data(path, data)
                return f"{bcolor.OKGREEN}Successfully cleared {field} from the routine {name} in your {day_name} routines{bcolor.ENDC}"

        raise AssertionError(f"{bcolor.FAIL}There is no routine with the name {name} in your {day_name} routines{bcolor.ENDC}")


    def day(self, day):
        return self._clear_day(day)

    def routine(self, day, name):
        return self._clear_routine(day, name)

    def time(self, day, name):
        return self._clear_field(day, name, "time")

    def duration(self, day, name):
        return self._clear_field(day, name, "duration")

    def subdurations(self, day, name):
        return self._clear_field(day, name, "subdurations")

class routine_edit:
    DAY_FILES = {
        "monday": "monday_routines.json",
        "tuesday": "tuesday_routines.json",
        "wednesday": "wednesday_routines.json",
        "thursday": "thursday_routines.json",
        "friday": "friday_routines.json",
        "saturday": "saturday_routines.json",
        "sunday": "sunday_routines.json",
    }
    DAY_NUMBERS = {
        1: "monday",
        2: "tuesday",
        3: "wednesday",
        4: "thursday",
        5: "friday",
        6: "saturday",
        7: "sunday",
    }
        
    @classmethod
    def _normalize_day(cls, day):
        if isinstance(day, int):
            return cls.DAY_NUMBERS[day]
        return str(day).lower()
        
    @classmethod
    def _load_data(cls, day):
        day_name = cls._normalize_day(day)
        path = routines_folder / f"{day_name}_routines.json"
        with path.open(encoding="utf-8") as file:
            return path, json.load(file)
        
    @staticmethod
    def _save_data(path, data):
        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
   
    
    def _edit_name(self, day, name, new_name):
        day_name = self._normalize_day(day)
        path, data = self._load_data(day_name)

        for i, routine in enumerate(data["routines"]):
            if routine["name"] == name:
                data["routines"][i]["name"] = new_name
                self._save_data(path, data)
                return f"{bcolor.OKGREEN}Successfully edited the routine {name} in your {day_name} routines{bcolor.ENDC}"

        raise AssertionError(f"{bcolor.FAIL}There is no routine with the name {name} in your {day_name} routines{bcolor.ENDC}")
        
    def _edit_field(self, day, name, field, new_value):
        day_name = self._normalize_day(day)
        path, data = self._load_data(day_name)

        for routine in data["routines"]:
            if routine["name"] == name:
                if routine.get(field) is None:
                    raise AssertionError(f"{bcolor.FAIL}There is no value in {field} for the routine {name} in your {day_name} routines, please add a value to {field} first using the add option{bcolor.ENDC}")
                routine[field] = new_value
                self._save_data(path, data)
                return f"{bcolor.OKGREEN}Successfully edited {field} for the routine {name} in your {day_name} routines{bcolor.ENDC}"

        raise AssertionError(f"{bcolor.FAIL}There is no routine with the name {name} in your {day_name} routines{bcolor.ENDC}")
    
    def name(self, day, name, new_name):
        return self._edit_name(day, name, new_name)

    def time(self, day, name, time):
        return self._edit_field(day, name, "time", time)

    def duration(self, day, name, duration):
        return self._edit_field(day, name, "duration", duration)

    def subdurations(self, day, name, subdurations):
        return self._edit_field(day, name, "subdurations", subdurations)

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
                print(f"{bcolor.WARNING}NOTE: Choose option 1 to add a routine {bcolor.ENDC}")
                return "No routine today!"
        elif day == 2:
            if tuesday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(tuesday_routines["routines"])):
                    print(f"{i + 1}. {tuesday_routines["routines"][i]["name"]}", end = " ") if tuesday_routines["routines"][i]["name"] is not None else None
                    print(f"for {tuesday_routines["routines"][i]["duration"]} minutes", end = " ") if tuesday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {tuesday_routines["routines"][i]["time"]}") if tuesday_routines["routines"][i]["time"] is not None else None
            else:
                print(f"{bcolor.WARNING}NOTE: Choose option 1 to add a routine {bcolor.ENDC}")
                return "No routine today!"
        elif day == 3:
            if wednesday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(wednesday_routines["routines"])):
                    print(f"{i + 1}. {wednesday_routines["routines"][i]["name"]}", end = " ") if wednesday_routines["routines"][i]["name"] is not None else None
                    print(f"for {wednesday_routines["routines"][i]["duration"]} minutes", end = " ") if wednesday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {wednesday_routines["routines"][i]["time"]}") if wednesday_routines["routines"][i]["time"] is not None else None
            else:
                print(f"{bcolor.WARNING}NOTE: Choose option 1 to add a routine {bcolor.ENDC}")
                return "No routine today!"
        elif day == 4:
            if thursday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(thursday_routines["routines"])):
                    print(f"{i + 1}. {thursday_routines["routines"][i]["name"]}", end = " ") if thursday_routines["routines"][i]["name"] is not None else None
                    print(f"for {thursday_routines["routines"][i]["duration"]} minutes", end = " ") if thursday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {thursday_routines["routines"][i]["time"]}") if thursday_routines["routines"][i]["time"] is not None else None
            else:
                print(f"{bcolor.WARNING}NOTE: Choose option 1 to add a routine {bcolor.ENDC}")
                return "No routine today!"
        elif day == 5:
            if friday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(friday_routines["routines"])):
                    print(f"{i + 1}. {friday_routines["routines"][i]["name"]}", end = " ") if friday_routines["routines"][i]["name"] is not None else None
                    print(f"for {friday_routines["routines"][i]["duration"]} minutes", end = " ") if friday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {friday_routines["routines"][i]["time"]}") if friday_routines["routines"][i]["time"] is not None else None
            else:
                print(f"{bcolor.WARNING}NOTE: Choose option 1 to add a routine {bcolor.ENDC}")
                return "No routine today!"
        elif day == 6:
            if saturday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(saturday_routines["routines"])):
                    print(f"{i + 1}. {saturday_routines["routines"][i]["name"]}", end = " ") if saturday_routines["routines"][i]["name"] is not None else None
                    print(f"for {saturday_routines["routines"][i]["duration"]} minutes", end = " ") if saturday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {saturday_routines["routines"][i]["time"]}") if saturday_routines["routines"][i]["time"] is not None else None
            else:
                print(f"{bcolor.WARNING}NOTE: Choose option 1 to add a routine {bcolor.ENDC}")
                return "No routine today!"
        else:
            if sunday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(sunday_routines["routines"])):
                    print(f"{i + 1}. {sunday_routines["routines"][i]["name"]}", end = " ") if sunday_routines["routines"][i]["name"] is not None else None
                    print(f"for {sunday_routines["routines"][i]["duration"]} minutes", end = " ") if sunday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {sunday_routines["routines"][i]["time"]}") if sunday_routines["routines"][i]["time"] is not None else None
            else:
                print(f"{bcolor.WARNING}NOTE: Choose option 1 to add a routine {bcolor.ENDC}")
                return "No routine today!"

    def completion_status(self):
        day_name = _normalize_day(current_day)
        path = routines_folder / f"{day_name}_routines.json"
        with path.open(encoding="utf-8") as file:
            data = json.load(file)

        progress_key = f"progress{current_date}"
        if progress_key not in data:
            print(f"{bcolor.WARNING}No progress data found for {day_name} routines on {current_date}.{bcolor.ENDC}")
            return

        print(f"Completion Status for {day_name.capitalize()} Routines on {current_date}:")
        if not data["routines"]:
            raise AssertionError(f"{bcolor.FAIL}No routines found for {day_name} routines. Please add routines to track completion status!{bcolor.ENDC}")
            return
        for routine in data["routines"]:
            routine_name = routine["name"]
            completed = any(progress.get(f"routine_{routine_name}_completed", False) for progress in data[progress_key])
            status = "Completed" if completed else "Not Completed"
            print(f"- {routine_name}: {status}")

class routine_player:
    def play_routine(self):
        progress_tracker = routine_progress()
        if current_day == 1:
            routines = monday_routines["routines"]
        elif current_day == 2:
            routines = tuesday_routines["routines"]
        elif current_day == 3:
            routines = wednesday_routines["routines"]
        elif current_day == 4:
            routines = thursday_routines["routines"]
        elif current_day == 5:
            routines = friday_routines["routines"]
        elif current_day == 6:
            routines = saturday_routines["routines"]
        else:
            routines = sunday_routines["routines"]

        for routine in routines:
            print(f"Starting routine: {routine['name']}")
            if routine.get("duration") not in ("None", None):
                if routine.get("subdurations") not in ("None", None, [], ""):
                    subdurations = routine["subdurations"]
                    if isinstance(subdurations, str):
                        subdurations = list(map(int, subdurations.split(',')))
                    for i, subduration in enumerate(subdurations):
                        print(f"Starting subduration {i + 1} of {len(subdurations)}: {subduration} minutes")
                        start = time.time()
                        while time.time() - start < int(subduration) * 60:
                            print(f"Time remaining: {int(int(subduration) * 60 - (time.time() - start))} seconds", end="\r")
                            pass
                        print(f"{bcolor.OKGREEN}Finished subduration {i + 1} of {len(subdurations)}: {subduration} minutes{bcolor.ENDC}")
                    if i == len(subdurations) - 1:
                        print(f"{bcolor.OKGREEN}Finished routine: {routine['name']}{bcolor.ENDC}")
                        progress_tracker.complete(routine["name"])
                        next = input("Would you like to continue to the next routine? (y/n): ")
                        if next.lower() != "y":
                            break

                else:
                    duration = int(routine["duration"])
                    print(f"Duration: {duration} minutes")
                    start = time.time()
                    while time.time() - start < duration * 60:
                        print(f"Time remaining: {int(duration * 60 - (time.time() - start))} seconds", end="\r")
                        pass
                    print(f"{bcolor.OKGREEN}Finished routine: {routine['name']}{bcolor.ENDC}")
                    progress_tracker.complete(routine["name"])
                    next = input("Would you like to continue to the next routine? (y/n): ")
                    if next.lower() != "y":
                        break
            else:
                print(f"No duration specified for routine: {routine['name']}. Skipping.")
            
        print(f"{bcolor.OKGREEN}All routines for today have been completed!{bcolor.ENDC}")
class routine_editor:
    def __init__(self):
        self.add = routine_adder()
        self.clear = routine_clearer()
        self.edit = routine_edit()
        self.read = routine_reader()
        self.play = routine_player()
        self.progress = routine_progress()
routine = routine_editor()

try:
    action = int(input("What routine tool would you like to use?\n1. Routine adder (for adding routines or information to routines)\n2. Routine clearer (for removing a routine a whole day or infos from a routine)\n3. Routine editor (for editing various information about a routine)\n4. Routine reader (for printing todays routines)\n5. View statistics\n6. Exit\n"))
    if action == 1:
        adder_option = int(input("What would you like to add?\n1. A routine\n2. A time to a routine without time\n3. A duration to a routine with no duration\n4. A subduration to a routine with a duration\n"))
        if adder_option == 1:
                adder_option_1_day = int(input("To what day would you like to add a routine (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
                adder_option_1_name = str(input("Please enter the name of your routine: "))
                adder_option_1_time = input("Please enter the time (None for no specific time): ")
                if adder_option_1_time == "None" or adder_option_1_time == "none":
                    adder_option_1_time = None
                adder_option_1_duration = input("Please enter you duration in minutes (None for no specific duration): ")
                if adder_option_1_duration == "None" or adder_option_1_duration == "none":
                    adder_option_1_duration = None
                if adder_option_1_duration:
                    adder_option_1_subdurations_notlist = input("Please enter your subdurations in minutes with a comma and a space between the numbers (None for no subduration): ")
                    if adder_option_1_subdurations_notlist != "None" and adder_option_1_subdurations_notlist != "none":
                        adder_option_1_subdurations = list(map(int, adder_option_1_subdurations_notlist.split(',')))
                        if int(sum(adder_option_1_subdurations)) != int(adder_option_1_duration):
                            raise AssertionError(f"{bcolor.FAIL}Please enter subdurations adding up to you duration. Sum is: {sum(adder_option_1_subdurations)}, but duration is: {adder_option_1_duration}{bcolor.ENDC}")
                    else:
                        adder_option_1_subdurations = None
                else:
                    adder_option_1_duration = None
                    adder_option_1_subdurations = None
                print(routine.add.routine(adder_option_1_day, adder_option_1_name, adder_option_1_time, int(adder_option_1_duration), adder_option_1_subdurations_notlist))
        elif adder_option == 2:
            adder_option_2_day = int(input("To what day would you like to add a time (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            adder_option_2_name = str(input("Please enter the name of your routine: "))
            adder_option_2_time = input("Please enter the time you would like to add: ")
            print(routine.add.time(adder_option_2_day, adder_option_2_name, adder_option_2_time))

        elif adder_option == 3:
            adder_option_3_day = int(input("To what day would you like to add a duration (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            adder_option_3_name = str(input("Please enter the name of your routine: "))
            adder_option_3_duration = int(input("Please enter the duration you would like to add in minutes: "))
            print(routine.add.duration(adder_option_3_day, adder_option_3_name, adder_option_3_duration))

        elif adder_option == 4:
            adder_option_4_day = int(input("To what day would you like to add subdurations (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            adder_option_4_name = str(input("Please enter the name of your routine: "))
            adder_option_4_subdurations_notlist = input("Please enter your subdurations in minutes with a comma and a space between the numbers: ")
            print(routine.add.subdurations(adder_option_4_day, adder_option_4_name, adder_option_4_subdurations_notlist))

        else:
            print(f"{bcolor.FAIL}Please only enter a number between 1 and 4!{bcolor.ENDC}")
    elif action == 2:
        clearer_option = int(input("What would you like to clear?\n1. A whole day\n2. A routine\n3. A time from a routine\n4. A duration from a routine\n5. Subdurations from a routine\n"))
        if clearer_option == 1:
            clearer_option_1_day = int(input("What day would you like to clear (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            print(routine.clear.day(clearer_option_1_day))
        elif clearer_option == 2:
            clearer_option_2_day = int(input("From what day would you like to clear a routine (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            clearer_option_2_name = str(input("Please enter the name of your routine: "))
            print(routine.clear.routine(clearer_option_2_day, clearer_option_2_name))
        elif clearer_option == 3:
            clearer_option_3_day = int(input("From what day would you like to clear a time (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            clearer_option_3_name = str(input("Please enter the name of your routine: "))
            print(routine.clear.time(clearer_option_3_day, clearer_option_3_name))
        elif clearer_option == 4:
            clearer_option_4_day = int(input("From what day would you like to clear a duration (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            clearer_option_4_name = str(input("Please enter the name of your routine: "))
            print(routine.clear.duration(clearer_option_4_day, clearer_option_4_name))
        elif clearer_option == 5:
            clearer_option_5_day = int(input("From what day would you like to clear subdurations (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            clearer_option_5_name = str(input("Please enter the name of your routine: "))
            print(routine.clear.subdurations(clearer_option_5_day, clearer_option_5_name))

        else:
            print(f"{bcolor.FAIL}Please only enter a number between 1 and 5!{bcolor.ENDC}")

    elif action == 3:
        editor_option = int(input("What would you like to edit?\n1. The name of a routine\n2. A time from a routine\n3. A duration from a routine\n4. Subdurations from a routine\n"))
        if editor_option == 1:
            editor_option_1_day = int(input("From what day would you like to edit the name of a routine (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            editor_option_1_name = str(input("Please enter the name of your routine: "))
            editor_option_1_new_name = str(input("Please enter the new name of your routine: "))
            print(routine.edit.name(editor_option_1_day, editor_option_1_name, editor_option_1_new_name))
        elif editor_option == 2:
            editor_option_2_day = int(input("From what day would you like to edit a time (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            editor_option_2_name = str(input("Please enter the name of your routine: "))
            editor_option_2_time = input("Please enter the new time you would like to change it to: ")
            print(routine.edit.time(editor_option_2_day, editor_option_2_name, editor_option_2_time))
        elif editor_option == 3:
            editor_option_3_day = int(input("From what day would you like to edit a duration (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            editor_option_3_name = str(input("Please enter the name of your routine: "))
            editor_option_3_duration = input("Please enter the new duration you would like to change it to in minutes: ")
            print(routine.edit.duration(editor_option_3_day, editor_option_3_name, editor_option_3_duration))
        elif editor_option == 4:
            print(f"{bcolor.FAIL}NOTE: All previously added subdurations will be deleted if you add new subdurations!{bcolor.ENDC}")
            editor_option_4_day = int(input("From what day would you like to edit subdurations (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            editor_option_4_name = str(input("Please enter the name of your routine: "))
            editor_option_4_subdurations_notlist = input("Please enter your new subdurations in minutes with a comma and a space between the numbers: ")
            print(routine.edit.subdurations(editor_option_4_day, editor_option_4_name, list(map(int, editor_option_4_subdurations_notlist.split(',')))))
        else:
            print(f"{bcolor.FAIL}Please only enter a number between 1 and 4!{bcolor.ENDC}")

    elif action == 4:
        option_4 = input("What would you like to view?\n1. Today's routine\n2. A specific day's routine\n3. The completion status of today's routines\n")
        if option_4 == "1":
            if routine.read.routine(current_day) != "No routine today!":
                play_choice = input("\nWould you like to play your routine? (y/n): ")
                if play_choice.lower() == "y":
                    print(f"{bcolor.OKGREEN}Starting your routine!{bcolor.ENDC}")
                    routine.play.play_routine()
                elif play_choice.lower() == "n":
                    print(f"{bcolor.WARNING}You chose not to play your routine. Exiting the program.{bcolor.ENDC}")
            else:
                print(f"{bcolor.WARNING}You have no routine today. Exiting the program.{bcolor.ENDC}")
        elif option_4 == "2":
            specific_day = int(input("Please enter the day you would like to view (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            if routine.read.routine(specific_day) != "No routine today!":
                play_choice = input("\nWould you like to play your routine? (y/n): ")
                if play_choice.lower() == "y":
                    print(f"{bcolor.OKGREEN}Starting your routine!{bcolor.ENDC}")
                    routine.play.play_routine()
                elif play_choice.lower() == "n":
                    print(f"{bcolor.WARNING}You chose not to play your routine. Exiting the program.{bcolor.ENDC}")
            else:
                print(f"{bcolor.WARNING}You have no routine for {_normalize_day(specific_day)}. Exiting the program.{bcolor.ENDC}")
        elif option_4 == "3":
            routine.read.completion_status()

    elif action == 6:
        print(f"{bcolor.FAIL}Exiting the programm...{bcolor.ENDC}")
        exit()

    else:
        print(f"{bcolor.FAIL}Please only enter a number between 1 and 5!{bcolor.ENDC}")

            
except ValueError as e:
    print(f"{bcolor.FAIL}Please only enter valid formats! {e}{bcolor.ENDC}")
except TypeError as e:
    print(f"{bcolor.FAIL}Please make sure you followed the instructions for the format! The following error occured: {e}{bcolor.ENDC}")
except Exception as e:
    print(f"{bcolor.FAIL}Ending script with error: {e}{bcolor.ENDC}")

