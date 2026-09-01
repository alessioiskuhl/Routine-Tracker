"""A simple routine tracker that allows you to track and timme your daily routines."""


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

    def _set_field_subdurations(self, day, name, field, value):
        day_name = self._normalize_day(day)
        path, data = self._load_data(day_name)
        duration = None
        for i in range(len(data["routines"])):
            if data["routines"][i]["name"] == name:
                duration = data["routines"][i]["duration"]
        if duration is None:
            raise AssertionError(f"{bcolor.FAIL}Please add a duration to the routine {name} in your {day_name} routines before adding subdurations{bcolor.ENDC}")

        if int(sum(value)) != int(duration):
            raise AssertionError(f"{bcolor.FAIL}Please enter subdurations adding up to you duration. Sum is: {sum(value)}, but duration is: {duration}{bcolor.ENDC}")

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
        self._set_field(day, name, "time", time)

    def duration(self, day, name, duration):
        self._set_field(day, name, "duration", duration)

    def subdurations(self, day, name, subdurations_notlist):
        try:
            if subdurations_notlist != "None" and subdurations_notlist != "none":
                subdurations = list(map(int, subdurations_notlist.split(',')))
            else:
                subdurations = None
        except Exception as e:
            print(f"{bcolor.FAIL}An error occurred while processing subdurations: {e}{bcolor.ENDC}")
        return self._set_field_subdurations(day, name, "subdurations", subdurations)


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

try:
    action = int(input("What routine tool would you like to use?\n1. Routine adder (for adding routines or information to routines)\n2. Routine clearer (for removing a routine a whole day or infos from a routine)\n3. Routine editor (for editing various information about a routine)\n4. Routine reader (for printing todays routines)\n"))
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
                print(routine.add.routine(adder_option_1_day, adder_option_1_name, adder_option_1_time, adder_option_1_duration, adder_option_1_subdurations))
        elif adder_option == 2:
            adder_option_2_day = int(input("To what day would you like to add a time (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            adder_option_2_name = str(input("Please enter the name of your routine: "))
            adder_option_2_time = input("Please enter the time you would like to add: ")
            print(routine.add.time(adder_option_2_day, adder_option_2_name, adder_option_2_time))

        elif adder_option == 3:
            adder_option_3_day = int(input("To what day would you like to add a duration (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            adder_option_3_name = str(input("Please enter the name of your routine: "))
            adder_option_3_duration = input("Please enter the duration you would like to add in minutes: ")
            print(routine.add.duration(adder_option_3_day, adder_option_3_name, adder_option_3_duration))

        elif adder_option == 4:
            print(f"{bcolor.FAIL}NOTE: All previously added subdurations will be deleted if you add new subdurations!{bcolor.ENDC}")
            adder_option_4_day = int(input("To what day would you like to add subdurations (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            adder_option_4_name = str(input("Please enter the name of your routine: "))
            adder_option_4_subdurations_notlist = input("Please enter your subdurations in minutes with a comma and a space between the numbers: ")
            print(routine.add.subdurations(adder_option_4_day, adder_option_4_name, adder_option_4_subdurations_notlist))

        else:
            print(f"{bcolor.FAIL}Please only enter a number between 1 and 4!{bcolor.ENDC}")

            
except ValueError:
    print(f"{bcolor.FAIL}Please only enter valid formats!{bcolor.ENDC}")
except TypeError as e:
    print(f"{bcolor.FAIL}Please make sure you followed the instructions for the format! The following error occured: {e}{bcolor.ENDC}")
except Exception as e:
    print(f"{bcolor.FAIL}Ending script with error: {e}{bcolor.ENDC}")

