"""All functions for the main python file are in this file"""

from datetime import datetime, timedelta
import time
from pathlib import Path
import json
class Bcolor:
    """Defining colors for text"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

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
routines_folder = script_dir / "Routines"

class initialize:
    def __init__(self):
        statistics_folder.mkdir(parents=True, exist_ok=True)
        routines_folder.mkdir(parents=True, exist_ok=True)
        file_path = routines_folder / "monday_routines.json"
        try:
            with open(file_path, "x", encoding="utf-8") as file:
                file.write(json.dumps({
                    "routines": [],
                    f"progress{current_date}" : []
                }))
            print(f"{Bcolor.OKGREEN}monday_routines.json didn't exist. Successfully created and wrote data.{Bcolor.ENDC}")
        except FileExistsError:
            pass
        except Exception as e:
            print(f"{Bcolor.FAIL}An error occurred while creating or writing to monday_routines.json: {e}{Bcolor.ENDC}")
        file_path = routines_folder / "tuesday_routines.json"
        try:
            with open(file_path, "x", encoding="utf-8") as file:
                file.write(json.dumps({
                    "routines": [],
                    f"progress{current_date}" : []
                }))
            print(f"{Bcolor.OKGREEN}tuesday_routines.json didn't exist. Successfully created and wrote data.{Bcolor.ENDC}")
        except FileExistsError:
            pass
        except Exception as e:
            print(f"{Bcolor.FAIL}An error occurred while creating or writing to tuesday_routines.json: {e}{Bcolor.ENDC}")
        file_path = routines_folder / "wednesday_routines.json"
        try:
            with open(file_path, "x", encoding="utf-8") as file:
                file.write(json.dumps({
                    "routines": [],
                    f"progress{current_date}" : []
                }))
            print(f"{Bcolor.OKGREEN}wednesday_routines.json didn't exist. Successfully created and wrote data.{Bcolor.ENDC}")
        except FileExistsError:
            pass
        except Exception as e:
            print(f"{Bcolor.FAIL}An error occurred while creating or writing to wednesday_routines.json: {e}{Bcolor.ENDC}")
        file_path = routines_folder / "thursday_routines.json"
        try:
            with open(file_path, "x", encoding="utf-8") as file:
                file.write(json.dumps({
                    "routines": [],
                    f"progress{current_date}" : []
                }))
            print(f"{Bcolor.OKGREEN}thursday_routines.json didn't exist. Successfully created and wrote data.{Bcolor.ENDC}")
        except FileExistsError:
            pass
        except Exception as e:
            print(f"{Bcolor.FAIL}An error occurred while creating or writing to thursday_routines.json: {e}{Bcolor.ENDC}")
        file_path = routines_folder / "friday_routines.json"
        try:
            with open(file_path, "x", encoding="utf-8") as file:
                file.write(json.dumps({
                    "routines": [],
                    f"progress{current_date}" : []
                }))
            print(f"{Bcolor.OKGREEN}friday_routines.json didn't exist. Successfully created and wrote data.{Bcolor.ENDC}")
        except FileExistsError:
            pass
        except Exception as e:
            print(f"{Bcolor.FAIL}An error occurred while creating or writing to friday_routines.json: {e}{Bcolor.ENDC}")
        file_path = routines_folder / "saturday_routines.json"
        try:
            with open(file_path, "x", encoding="utf-8") as file:
                file.write(json.dumps({
                    "routines": [],
                    f"progress{current_date}" : []
                }))
            print(f"{Bcolor.OKGREEN}saturday_routines.json didn't exist. Successfully created and wrote data.{Bcolor.ENDC}")
        except FileExistsError:
            pass
        except Exception as e:
            print(f"{Bcolor.FAIL}An error occurred while creating or writing to saturday_routines.json: {e}{Bcolor.ENDC}")
        file_path = routines_folder / "sunday_routines.json"
        try:
            with open(file_path, "x", encoding="utf-8") as file:
                file.write(json.dumps({
                    "routines": [],
                    f"progress{current_date}" : []
                }))
            print(f"{Bcolor.OKGREEN}sunday_routines.json didn't exist. Successfully created and wrote data.{Bcolor.ENDC}")
        except FileExistsError:
            pass
        except Exception as e:
            print(f"{Bcolor.FAIL}An error occurred while creating or writing to sunday_routines.json: {e}{Bcolor.ENDC}")
        file_path = statistics_folder / "statistics.json"
        try:
            with open(file_path, "x", encoding="utf-8") as file:
                file.write(json.dumps({
                    "statistics": [{
                        f"completions today ({current_date})" : 0,
                        f"completions this week ({current_week})" : 0,
                        f"completions this month ({current_month})" : 0,
                        f"completions this year ({datetime.today().year})" : 0,
                        f"completions yesterday ({yesterday_date})" : 0,
                        f"completions last week ({last_week})" : 0,
                        f"completions last month ({last_month})" : 0,
                        f"completions last year ({last_year})" : 0,
                        "completions all time" : 0,
                        f"Current Streak ({current_date})" : 0,
                        f"Longest Streak ({current_date})" : 0,
                        f"Current streak status ({current_date})" : "None",
                    }]
                }, indent=4))
            print(f"{Bcolor.OKGREEN}statistics.json didn't exist. Successfully created and wrote data.{Bcolor.ENDC}")

        except FileExistsError:
            pass
        except Exception as e:
            print(f"{Bcolor.FAIL}An error occurred while creating or writing to statistics.json: {e}{Bcolor.ENDC}")

        with open(statistics_folder / "statistics.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            statistics = data["statistics"][0]
            today_key = next((key for key in statistics if key.startswith("completions today (")), None)

            period_definitions = {
                "week": ("completions this week (", current_week, "completions last week ("),
                "month": ("completions this month (", current_month, "completions last month ("),
                "year": ("completions this year (", datetime.today().year, "completions last year ("),
            }
            replacements = {}
            day_changed = today_key is None or current_date not in today_key
            day_changed_yesterday = today_key is yesterday_date

            if day_changed:
                yesterday_completions = statistics.get(today_key, 0)
                replacements[today_key] = (f"completions today ({current_date})", 0)
                yesterday_key = next((key for key in statistics if key.startswith("completions yesterday (")), None)
                if yesterday_key is not None:
                    replacements[yesterday_key] = (f"completions yesterday ({yesterday_date})", yesterday_completions)
                replacements.update({
                    key: value for key, value in (
                        (next((key for key in statistics if key.startswith(prefix)), None), replacement)
                        for prefix, replacement in {
                            "remaining routines today (": (f"remaining routines today ({current_date})", 0),
                            "Current streak status (": (f"Current streak status ({current_date})", "unactive") if day_changed_yesterday else (f"Current streak status ({current_date})", "None"),
                        }.items()
                    ) if key is not None
                })

            for current_prefix, period_number, last_prefix in period_definitions.values():
                current_key = next((key for key in statistics if key.startswith(current_prefix)), None)
                if current_key is None or f"({period_number})" in current_key:
                    continue

                old_value = statistics[current_key]
                old_number = current_key.removeprefix(current_prefix).removesuffix(")")
                replacements[current_key] = (f"{current_prefix}{period_number})", 0)
                last_key = next((key for key in statistics if key.startswith(last_prefix)), None)
                if last_key is not None:
                    replacements[last_key] = (f"{last_prefix}{old_number})", old_value)

            if replacements:
                updated_statistics = {}
                for key, value in statistics.items():
                    replacement = replacements.get(key)
                    if replacement is None:
                        updated_statistics[key] = value
                    else:
                        updated_statistics[replacement[0]] = replacement[1]
                statistics = updated_statistics
                data["statistics"][0] = statistics
                file.seek(0)
                json.dump(data, file, indent=4)
                file.truncate()

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

initialize()

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
        day_name = self._normalize_day(self.today)
        path = routines_folder / f"{day_name}_routines.json"
        with path.open(encoding="utf-8") as file:
            data = json.load(file)

        for routine in data["routines"]:
            if routine["name"] == routine_name:
                data[f"progress{self.current_date}"].append({f"routine_{routine_name}_completed": True})
                break
        else:
            raise ValueError(f"No routine found with name: {routine_name}")

        with path.open("w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        path = statistics_folder / "statistics.json"
        with path.open(encoding="utf-8") as file:
            stats_data = json.load(file)
            stats = stats_data["statistics"][0]

        stats[f"completions today ({self.current_date})"] += 1
        stats[f"completions this week ({current_week})"] += 1
        stats[f"completions this month ({current_month})"] += 1
        stats[f"completions this year ({datetime.today().year})"] += 1
        stats["completions all time"] += 1
        if f"Current streak status ({current_date})" in stats:
            if stats[f"Current streak status ({current_date})"] == "None":
                stats[f"Current streak status ({current_date})"] = "active"
                if f"Current Streak ({current_date})" in stats:
                    stats[f"Current Streak ({current_date})"] += 1
                elif f"Current Streak ({yesterday_date})" in stats:
                    stats[f"Current Streak ({current_date})"] = stats[f"Current Streak ({yesterday_date})"] + 1
                else:
                    stats[f"Current Streak ({current_date})"] = 1
                if f"Longest Streak ({current_date})" in stats:
                    if stats[f"Current Streak ({current_date})"] > stats[f"Longest Streak ({current_date})"]:
                        stats[f"Longest Streak ({current_date})"] = stats[f"Current Streak ({current_date})"]
                elif f"Longest Streak ({yesterday_date})" in stats:
                    if stats[f"Current Streak ({current_date})"] > stats[f"Longest Streak ({yesterday_date})"]:
                        stats[f"Longest Streak ({current_date})"] = stats[f"Current Streak ({current_date})"]
                else:
                    for key in list(stats):
                        if key.startswith("Longest Streak ("):
                            stats[f"Longest Streak ({current_date})"] = stats[key].pop()
                            if stats[f"Current Streak ({current_date})"] > stats[f"Longest Streak ({current_date})"]:
                                stats[f"Longest Streak ({current_date})"] = stats[f"Current Streak ({current_date})"]
                    stats[f"Longest Streak ({current_date})"] = stats[f"Current Streak ({current_date})"]
        elif f"Current streak status ({yesterday_date})" in stats:
            stats[f"Current streak status ({current_date})"] = stats[f"Current streak status ({yesterday_date})"].pop()
            if stats[f"Current streak status ({current_date})"] == "unactive" or stats[f"Current streak status ({current_date})"] == "active":
                stats[f"Current streak status ({current_date})"] = "active"
                stats[f"Current Streak ({current_date})"] += 1
                if stats[f"Current Streak ({current_date})"] > stats[f"Longest Streak ({current_date})"]:
                    stats[f"Longest Streak ({current_date})"] = stats[f"Current Streak ({current_date})"]
        else:
            for key in list(stats):
                if key.startswith("Current streak status ("):
                    stats[f"Current streak status ({current_date})"] = stats[key].pop()
                    stats[f"Current streak status ({current_date})"] = "active"
                elif key.startswith("Current Streak ("):
                    stats[f"Current Streak ({current_date})"] = stats[key].pop()
                    stats[f"Current Streak ({current_date})"] = 1
                    for key1 in list(stats):
                        if key1.startswith("Longest Streak ("):
                            stats[f"Longest Streak ({current_date})"] = stats[key1].pop()
                            if stats[f"Longest Streak ({current_date})"] < stats[f"Current Streak ({current_date})"]:
                                stats[f"Longest Streak ({current_date})"] = stats[f"Current Streak ({current_date})"]


        with path.open("w", encoding="utf-8") as file:
            json.dump(stats_data, file, indent = 4)

        

    
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

        if field == "subdurations" and not isinstance(value, list):
            try:
                value = list(map(int, value.split(',')))
            except ValueError:
                raise ValueError("Please only enter numbers as subdurations. Don't do something like \"2 min, 4 min, 3 min\" as the tracker already expects the numbers to be in minutes.")
        if field == "subdurations":
            for routine in data["routines"]:
                if routine["name"] == name:
                    if sum(value) != routine["duration"]:
                        raise ValueError(f"Your subdurations don't add up to the duration. They must add up to {routine["duration"]}")

        for routine in data["routines"]:
            if routine["name"] == name:
                if routine.get(field) is not None:
                    raise AssertionError(f"There is already a {field} for the routine {name} in your {day_name} routines. The current {field} is {routine[field]}.")
                routine[field] = value
                self._save_data(path, data)
                return f"Successfully added {field} to the routine {name} in your {day_name} routines"

        raise AssertionError(f"There is no routine with the name {name} in your {day_name} routines. Please check for spelling mistakes or create a new routine.")


    def routine(self, day, name, time, duration, subdurations: list):
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
                raise Exception(f"There is already a routine with the name {new_routine['name']} in your {day_name} routines")

        data["routines"].append(new_routine)
        self._save_data(path, data)
        return f"Successfully added routine {name} to your {day_name} routines"

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
            raise AssertionError(f"{Bcolor.FAIL}There are no routines in your {day_name} routines to clear{Bcolor.ENDC}")

        data["routines"] = []
        self._save_data(path, data)
        return f"{Bcolor.OKGREEN}Successfully cleared all routines from your {day_name} routines{Bcolor.ENDC}"

    def _clear_routine(self, day, name):
        day_name = self._normalize_day(day)
        path, data = self._load_data(day_name)

        for i, routine in enumerate(data["routines"]):
            if routine["name"] == name:
                del data["routines"][i]
                self._save_data(path, data)
                return f"{Bcolor.OKGREEN}Successfully cleared the routine {name} from your {day_name} routines{Bcolor.ENDC}"

        raise AssertionError(f"{Bcolor.FAIL}There is no routine with the name {name} in your {day_name} routines{Bcolor.ENDC}")
    
    def _clear_field(self, day, name, field):
        day_name = self._normalize_day(day)
        path, data = self._load_data(day_name)

        for routine in data["routines"]:
            if routine["name"] == name:
                if routine.get(field) is None:
                    raise AssertionError(f"{Bcolor.FAIL}There is already no value in {field} for the routine {name} in your {day_name} routines{Bcolor.ENDC}")
                routine[field] = None
                self._save_data(path, data)
                return f"{Bcolor.OKGREEN}Successfully cleared {field} from the routine {name} in your {day_name} routines{Bcolor.ENDC}"

        raise AssertionError(f"{Bcolor.FAIL}There is no routine with the name {name} in your {day_name} routines{Bcolor.ENDC}")


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
                if name == new_name:
                    raise AssertionError(f"The routine is already named {new_name}")
                data["routines"][i]["name"] = new_name
                self._save_data(path, data)
                return f"Successfully edited the routine {name} in your {day_name} routines"

        raise AssertionError(f"There is no routine with the name {name} in your {day_name} routines")
        
    def _edit_field(self, day, name, field, new_value):
        day_name = self._normalize_day(day)
        path, data = self._load_data(day_name)
        if field == "subdurations" and not isinstance(new_value, list):
            try:
                new_value = list(map(int, new_value.split(',')))
            except ValueError:
                raise ValueError("Please only enter numbers as subdurations. Don't do something like \"2 min, 4 min, 3 min\" as the tracker already expects the numbers to be in minutes.")
        if field == "subdurations":
            for routine in data["routines"]:
                if routine["name"] == name:
                    if sum(new_value) != routine["duration"]:
                        raise ValueError(f"Your subdurations don't add up to the duration. They must add up to {routine["duration"]}")
        

        for routine in data["routines"]:
            if routine["name"] == name:
                if routine.get(field) is None:
                    raise AssertionError(f"There is no value in {field} for the routine {name} in your {day_name} routines, please add a value to {field} first using the add option")
                routine[field] = new_value
                self._save_data(path, data)
                return f"Successfully edited {field} for the routine {name} in your {day_name} routines"

        raise AssertionError(f"There is no routine with the name {name} in your {day_name} routines")
    
    def name(self, day, name, new_name):
        return self._edit_name(day, name, new_name)

    def time(self, day, name, time):
        return self._edit_field(day, name, "time", time)

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
                print(f"{Bcolor.WARNING}NOTE: Choose option 1 to add a routine {Bcolor.ENDC}")
                return "No routine today!"
        elif day == 2:
            if tuesday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(tuesday_routines["routines"])):
                    print(f"{i + 1}. {tuesday_routines["routines"][i]["name"]}", end = " ") if tuesday_routines["routines"][i]["name"] is not None else None
                    print(f"for {tuesday_routines["routines"][i]["duration"]} minutes", end = " ") if tuesday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {tuesday_routines["routines"][i]["time"]}") if tuesday_routines["routines"][i]["time"] is not None else None
            else:
                print(f"{Bcolor.WARNING}NOTE: Choose option 1 to add a routine {Bcolor.ENDC}")
                return "No routine today!"
        elif day == 3:
            if wednesday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(wednesday_routines["routines"])):
                    print(f"{i + 1}. {wednesday_routines["routines"][i]["name"]}", end = " ") if wednesday_routines["routines"][i]["name"] is not None else None
                    print(f"for {wednesday_routines["routines"][i]["duration"]} minutes", end = " ") if wednesday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {wednesday_routines["routines"][i]["time"]}") if wednesday_routines["routines"][i]["time"] is not None else None
            else:
                print(f"{Bcolor.WARNING}NOTE: Choose option 1 to add a routine {Bcolor.ENDC}")
                return "No routine today!"
        elif day == 4:
            if thursday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(thursday_routines["routines"])):
                    print(f"{i + 1}. {thursday_routines["routines"][i]["name"]}", end = " ") if thursday_routines["routines"][i]["name"] is not None else None
                    print(f"for {thursday_routines["routines"][i]["duration"]} minutes", end = " ") if thursday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {thursday_routines["routines"][i]["time"]}") if thursday_routines["routines"][i]["time"] is not None else None
            else:
                print(f"{Bcolor.WARNING}NOTE: Choose option 1 to add a routine {Bcolor.ENDC}")
                return "No routine today!"
        elif day == 5:
            if friday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(friday_routines["routines"])):
                    print(f"{i + 1}. {friday_routines["routines"][i]["name"]}", end = " ") if friday_routines["routines"][i]["name"] is not None else None
                    print(f"for {friday_routines["routines"][i]["duration"]} minutes", end = " ") if friday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {friday_routines["routines"][i]["time"]}") if friday_routines["routines"][i]["time"] is not None else None
            else:
                print(f"{Bcolor.WARNING}NOTE: Choose option 1 to add a routine {Bcolor.ENDC}")
                return "No routine today!"
        elif day == 6:
            if saturday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(saturday_routines["routines"])):
                    print(f"{i + 1}. {saturday_routines["routines"][i]["name"]}", end = " ") if saturday_routines["routines"][i]["name"] is not None else None
                    print(f"for {saturday_routines["routines"][i]["duration"]} minutes", end = " ") if saturday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {saturday_routines["routines"][i]["time"]}") if saturday_routines["routines"][i]["time"] is not None else None
            else:
                print(f"{Bcolor.WARNING}NOTE: Choose option 1 to add a routine {Bcolor.ENDC}")
                return "No routine today!"
        else:
            if sunday_routines["routines"]:
                print("Today's Routine:")
                for i in range(len(sunday_routines["routines"])):
                    print(f"{i + 1}. {sunday_routines["routines"][i]["name"]}", end = " ") if sunday_routines["routines"][i]["name"] is not None else None
                    print(f"for {sunday_routines["routines"][i]["duration"]} minutes", end = " ") if sunday_routines["routines"][i]["duration"] is not None else None 
                    print(f"at {sunday_routines["routines"][i]["time"]}") if sunday_routines["routines"][i]["time"] is not None else None
            else:
                print(f"{Bcolor.WARNING}NOTE: Choose option 1 to add a routine {Bcolor.ENDC}")
                return "No routine today!"

    def completion_status(self):
        day_name = _normalize_day(current_day)
        path = routines_folder / f"{day_name}_routines.json"
        with path.open(encoding="utf-8") as file:
            data = json.load(file)

        progress_key = f"progress{current_date}"
        if progress_key not in data:
            print(f"{Bcolor.WARNING}No progress data found for {day_name} routines on {current_date}.{Bcolor.ENDC}")
            return

        print(f"Completion Status for {day_name.capitalize()} Routines on {current_date}:")
        if not data["routines"]:
            raise AssertionError(f"{Bcolor.FAIL}No routines found for {day_name} routines. Please add routines to track completion status!{Bcolor.ENDC}")
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
            if f"routine_{routine['name']}_completed" in [key for progress in data[f"progress{current_date}"] for key in progress]:
                print(f"{Bcolor.WARNING}Routine '{routine['name']}' has already been completed today. Skipping.{Bcolor.ENDC}")
                continue
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
                        print(f"{Bcolor.OKGREEN}Finished subduration {i + 1} of {len(subdurations)}: {subduration} minutes{Bcolor.ENDC}")
                    if i == len(subdurations) - 1:
                        print(f"{Bcolor.OKGREEN}Finished routine: {routine['name']}{Bcolor.ENDC}")
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
                    print(f"{Bcolor.OKGREEN}Finished routine: {routine['name']}{Bcolor.ENDC}")
                    progress_tracker.complete(routine["name"])
                    next = input("Would you like to continue to the next routine? (y/n): ")
                    if next.lower() != "y":
                        break
            else:
                print(f"No duration specified for routine: {routine['name']}. Skipping.")
            
        print(f"{Bcolor.OKGREEN}All routines for today have been completed!{Bcolor.ENDC}")


