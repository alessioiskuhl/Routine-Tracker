"""A simple routine tracker that allows you to track and time your daily routines."""

from functions import routine_player, routine_reader, routine_edit, routine_clearer, routine_adder, routine_progress
from datetime import datetime, timedelta
import time
from pathlib import Path
import json
from PyQt6.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QLineEdit, QComboBox, QTimeEdit, QCheckBox, QSpinBox, QMessageBox
from PyQt6.QtCore import Qt, QTime
from PyQt6.QtGui import QIcon
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
class routine_editor:
    def __init__(self):
        self.add = routine_adder()
        self.clear = routine_clearer()
        self.edit = routine_edit()
        self.read = routine_reader()
        self.play = routine_player()
        self.progress = routine_progress()
routine = routine_editor()


icon_path = Path(__file__).parent / "Icon" / "routine_tracker_icon.png"
class AddRoutineWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add a Routine")
        self.resize(380, 310)
        self.setFixedSize(380, 310)
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        # Widgets
        self.daySelect = QComboBox(self)
        self.daySelect.setGeometry(10, 10, 170, 20)
        self.daySelect.addItems(["Select day to add to...", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        self.nameEnter = QLineEdit(self)
        self.nameEnter.setGeometry(10, 40, 200, 30)
        self.nameEnter.setPlaceholderText("Enter name of your routine")
        QLabel("<- Name", self).setGeometry(220, 40, 100, 30)
        self.timeSelect = QTimeEdit(self)
        self.timeSelect.setGeometry(10, 110, 100, 30)
        self.timeSelect.setTimeRange(QTime(0, 0, 0), QTime(23, 59, 0))
        self.timeSelect.setEnabled(False)
        QLabel("<- Time", self).setGeometry(220, 110, 100, 30)
        self.timeNeeded = QCheckBox("Do you want your routine at a certain time?", self)
        self.timeNeeded.setGeometry(10, 80, 300, 20)
        self.timeNeeded.stateChanged.connect(self.onStateChangedTime)
        self.durationChoose = QSpinBox(self)
        self.durationChoose.setGeometry(10, 150, 100, 30)
        self.durationChoose.setSuffix(" min")
        self.durationChoose.setMaximum(1440)
        self.durationChoose.setMinimum(1)
        QLabel("<- Duration", self).setGeometry(220, 150, 100, 30)
        self.subdurationNeeded = QCheckBox("Do you want subdurations for phases of your routine?", self)
        self.subdurationNeeded.setGeometry(10, 190, 330, 30)
        self.subdurationNeeded.stateChanged.connect(self.onStateChangedSubdur)
        self.subdurationEnter = QLineEdit(self)
        self.subdurationEnter.setGeometry(10, 220, 200, 30)
        self.subdurationEnter.setPlaceholderText("subduration, subduration, ...")
        self.subdurationEnter.setEnabled(False)
        QLabel("<- Subdurations", self).setGeometry(220, 220, 200, 30)
        self.cancelButton = QPushButton("Cancel", self, clicked = self.cancelPressed)
        self.cancelButton.setGeometry(40, 260, 150, 40)
        self.cancelButton.setStyleSheet("color: red;")
        self.createButton = QPushButton("Create Routine", self, clicked = self.startCreation)
        self.createButton.setGeometry(210, 260, 150, 40)
        self.createButton.setStyleSheet("color: green;")


    def startCreation(self):
        day = self.daySelect.currentText()
        name = self.nameEnter.text()
        time = self.timeSelect.time().toString() if self.timeNeeded.isChecked() else None
        dur = self.durationChoose.value()
        try:
            subdur = list(map(int, self.subdurationEnter.text().split(','))) if self.subdurationNeeded.isChecked() else None
        except ValueError:
            QMessageBox.critical(self, "Error", "Please only enter numbers as subdurations. Don't do something like \"2 min, 4 min, 3 min\" as the tracker already expects the numbers to be in minutes.")
            return None
        if day == "Select day to add to...":
            QMessageBox.critical(self, "Error", "Please choose a day to add the routine to.")
            return None
        elif not name:
            QMessageBox.critical(self, "Error", "Please enter a name for your routine")
            return None
        else:                 
            try:
                routine.add.routine(day, name, time, dur, subdur)
                QMessageBox.information(self, "Succesfully created", f"The routine {name} was succesfully added to {day}" if time == None else f"The routine {name} was succesfully added to {day} at {time}")
                self.close()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"The following error occured: {e}")
                
        
    def cancelPressed(self):
        self.close()
        self.addingwindow = AddSomethingWindow()
        self.addingwindow.show()

    def onStateChangedTime(self):
        if self.timeNeeded.isChecked():
            self.timeSelect.setEnabled(True)
        else:
            self.timeSelect.setEnabled(False)

    def onStateChangedSubdur(self):
        if self.subdurationNeeded.isChecked():
            self.subdurationEnter.setEnabled(True)
        else:
            self.subdurationEnter.setEnabled(False)


class AddTimeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add a Time to a routine")
        self.resize(380, 170)
        self.setFixedSize(380, 170)
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)


        # Widgets
        self.daySelect = QComboBox(self)
        self.daySelect.setGeometry(10, 10, 170, 20)
        self.daySelect.addItems(["Select day of routine...", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        self.nameEnter = QLineEdit(self)
        self.nameEnter.setGeometry(10, 40, 200, 30)
        self.nameEnter.setPlaceholderText("Enter name of the routine")
        QLabel("<- Name of routine", self).setGeometry(220, 40, 150, 30)
        self.timeSelect = QTimeEdit(self)
        self.timeSelect.setGeometry(10, 80, 100, 30)
        self.timeSelect.setTimeRange(QTime(0, 0, 0), QTime(23, 59, 0))
        QLabel("<- Time to add", self).setGeometry(220, 80, 150, 30)
        self.cancelButton = QPushButton("Cancel", self, clicked = self.cancelPressed)
        self.cancelButton.setGeometry(40, 120, 150, 40)
        self.cancelButton.setStyleSheet("color: red;")
        self.createButton = QPushButton("Add time", self, clicked = self.addTime)
        self.createButton.setGeometry(210, 120, 150, 40)
        self.createButton.setStyleSheet("color: green;")

    def cancelPressed(self):
        self.close()
        AddWindow = AddSomethingWindow()
        AddWindow.show()

    def addTime(self):
        day = self.daySelect.currentText()
        name = self.nameEnter.text()
        time = self.timeSelect.time().toString()
        if day == "Select day to add to...":
            QMessageBox.critical(self, "Error", "Please choose a day to add the time to.")
            return None
        elif not name:
            QMessageBox.critical(self, "Error", "Please enter the name of the routine")
            return None
        else:
            try:
                routine.add.time(day, name, time)
                QMessageBox.information(self, "Succesfully added", f"The time {time} was successfully added to the routine {name}")
                self.close()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"The following error occured: {e}")


class AddSubdurationWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add subdurations to a routine")
        self.resize(380, 170)
        self.setFixedSize(380, 170)
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        # Widgets
        self.daySelect = QComboBox(self)
        self.daySelect.setGeometry(10, 10, 170, 20)
        self.daySelect.addItems(["Select day of routine...", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        self.nameEnter = QLineEdit(self)
        self.nameEnter.setGeometry(10, 40, 200, 30)
        self.nameEnter.setPlaceholderText("Enter name of the routine")
        QLabel("<- Name of routine", self).setGeometry(220, 40, 150, 30)
        self.subdurationEnter = QLineEdit(self)
        self.subdurationEnter.setGeometry(10, 80, 200, 30)
        self.subdurationEnter.setPlaceholderText("subduration, subduration, ...")
        QLabel("<- Subdurations to add", self).setGeometry(220, 80, 150, 30)
        self.cancelButton = QPushButton("Cancel", self, clicked = self.cancelPressed)
        self.cancelButton.setGeometry(40, 120, 150, 40)
        self.cancelButton.setStyleSheet("color: red;")
        self.createButton = QPushButton("Add subdurations", self, clicked = self.addSubdurations)
        self.createButton.setGeometry(210, 120, 150, 40)
        self.createButton.setStyleSheet("color: green;")

    def cancelPressed(self):
        self.close()
        AddWindow = AddSomethingWindow()
        AddWindow.show()

    def addSubdurations(self):
        day = self.daySelect.currentText()
        name = self.nameEnter.text()
        try:
            subdur = list(map(int, self.subdurationEnter.text().split(',')))
        except ValueError:
            QMessageBox.critical(self, "Error", "Please only enter whole numbers as subdurations. Don't do something like \"2 min, 4 min, 3 min\" or \"2.5, 4.3, 3.14159\"as the tracker already expects the numbers to be in minutes.")
            return None
        if day == "Select day to add to...":
            QMessageBox.critical(self, "Error", "Please choose a day to add the routine to.")
            return None
        elif not name:
            QMessageBox.critical(self, "Error", "Please enter the name of the routine")
            return None
        else:
            try:
                routine.add.subdurations(day, name, subdur)
                QMessageBox.information(self, "Succesfully added", f"The subdurations {subdur} was successfully added to the routine {name}")
                self.close()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"The following error occured: {e}")

class EditNameWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit the name of a routine")
        self.resize(380, 170)
        self.setFixedSize(380, 170)
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        # Widgets
        self.daySelect = QComboBox(self)
        self.daySelect.setGeometry(10, 10, 170, 20)
        self.daySelect.addItems(["Select day of routine...", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        self.nameEnter = QLineEdit(self)
        self.nameEnter.setGeometry(10, 40, 200, 30)
        self.nameEnter.setPlaceholderText("Enter current name of the routine")
        QLabel("<- Current name of routine", self).setGeometry(220, 40, 150, 30)
        self.newNameEnter = QLineEdit(self)
        self.newNameEnter.setGeometry(10, 80, 200, 30)
        self.newNameEnter.setPlaceholderText("Enter new name of the routine")
        QLabel("<- New name of routine", self).setGeometry(220, 80, 150, 30)
        self.cancelButton = QPushButton("Cancel", self, clicked = self.cancelPressed)
        self.cancelButton.setGeometry(40, 120, 150, 40)
        self.cancelButton.setStyleSheet("color: red;")
        self.changeButton = QPushButton("Change name", self, clicked = self.editName)
        self.changeButton.setGeometry(210, 120, 150, 40)
        self.changeButton.setStyleSheet("color: green;")

    def cancelPressed(self):
        self.close()
        self.editSomethingWindow = EditSomethingWindow()
        self.editSomethingWindow.show()

    def editName(self):
        day = self.daySelect.currentText()
        name = self.nameEnter.text()
        new_name = self.newNameEnter.text()
        if day == "Select day to add to...":
            QMessageBox.critical(self, "Error", "Please choose a day to add the routine to.")
            return None
        elif not name:
            QMessageBox.critical(self, "Error", "Please enter the name of the routine")
            return None
        elif not new_name:
            QMessageBox.critical(self, "Error", "Please enter the new name of the routine")
            return None
        else:
            try:
                routine.edit.name(day, name, new_name)
                QMessageBox.information(self, "Succesfully edited", f"The routine previously called {name} is now called {new_name}")
                self.close()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"The following error occured: {e}")
        
class EditTimeWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit the time of a routine")
        self.resize(380, 170)
        self.setFixedSize(380, 170)
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        # Widgets
        self.daySelect = QComboBox(self)
        self.daySelect.setGeometry(10, 10, 170, 20)
        self.daySelect.addItems(["Select day of routine...", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        self.nameEnter = QLineEdit(self)
        self.nameEnter.setGeometry(10, 40, 200, 30)
        self.nameEnter.setPlaceholderText("Enter name of the routine")
        QLabel("<- Name of routine", self).setGeometry(220, 40, 150, 30)
        self.newTimeEnter = QTimeEdit(self)
        self.newTimeEnter.setGeometry(10, 80, 200, 30)
        self.newTimeEnter.setTimeRange(QTime(0, 0, 0), QTime(23, 59, 59))
        QLabel("<- New time of routine", self).setGeometry(220, 80, 150, 30)
        self.cancelButton = QPushButton("Cancel", self, clicked = self.cancelPressed)
        self.cancelButton.setGeometry(40, 120, 150, 40)
        self.cancelButton.setStyleSheet("color: red;")
        self.changeButton = QPushButton("Change time", self, clicked = self.editTime)
        self.changeButton.setGeometry(210, 120, 150, 40)
        self.changeButton.setStyleSheet("color: green;")

    def cancelPressed(self):
        self.close()
        self.editSomethingWindow = EditSomethingWindow()
        self.editSomethingWindow.show()

    def editTime(self):
        day = self.daySelect.currentText()
        name = self.nameEnter.text()
        new_time = self.newTimeEnter.time().toString()
        if day == "Select day to add to...":
            QMessageBox.critical(self, "Error", "Please choose a day to add the routine to.")
            return None
        elif not name:
            QMessageBox.critical(self, "Error", "Please enter the name of the routine")
            return None
        else:
            try:
                routine.edit.time(day, name, new_time)
                QMessageBox.information(self, "Succesfully edited", f"The routine {name} is now planned for {new_time}")
                self.close()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"The following error occured: {e}")
        
class EditSubdurationsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Edit the subdurations of a routine")
        self.resize(380, 170)
        self.setFixedSize(380, 170)
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        # Widgets
        self.daySelect = QComboBox(self)
        self.daySelect.setGeometry(10, 10, 170, 20)
        self.daySelect.addItems(["Select day of routine...", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])
        self.nameEnter = QLineEdit(self)
        self.nameEnter.setGeometry(10, 40, 200, 30)
        self.nameEnter.setPlaceholderText("Enter name of the routine")
        QLabel("<- Name of routine", self).setGeometry(220, 40, 150, 30)
        self.newSubdurationsEnter = QLineEdit(self)
        self.newSubdurationsEnter.setGeometry(10, 80, 200, 30)
        self.newSubdurationsEnter.setPlaceholderText("subduration, subduration, ...")
        QLabel("<- New subdurations of routine", self).setGeometry(220, 80, 150, 30)
        self.cancelButton = QPushButton("Cancel", self, clicked = self.cancelPressed)
        self.cancelButton.setGeometry(40, 120, 150, 40)
        self.cancelButton.setStyleSheet("color: red;")
        self.changeButton = QPushButton("Change subdurations", self, clicked = self.editSubdurations)
        self.changeButton.setGeometry(210, 120, 150, 40)
        self.changeButton.setStyleSheet("color: green;")

    def cancelPressed(self):
        self.close()
        self.editSomethingWindow = EditSomethingWindow()
        self.editSomethingWindow.show()

    def editSubdurations(self):
        day = self.daySelect.currentText()
        name = self.nameEnter.text()
        new_subdurations = self.newSubdurationsEnter.text()
        try:
            subdur = list(map(int, self.newSubdurationsEnter.text().split(',')))
        except ValueError:
            QMessageBox.critical(self, "Error", "Please only enter whole numbers as subdurations. Don't do something like \"2 min, 4 min, 3 min\" or \"2.5, 4.3, 3.14159\"as the tracker already expects the numbers to be in minutes.")
            return None
        if day == "Select day to add to...":
            QMessageBox.critical(self, "Error", "Please choose a day to add the routine to.")
            return None
        elif not name:
            QMessageBox.critical(self, "Error", "Please enter the name of the routine")
            return None
        else:
            try:
                routine.edit.subdurations(day, name, subdur)
                QMessageBox.information(self, "Succesfully edited", f"The routine {name} now has the following subdurations: {new_subdurations}")
                self.close()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"The following error occured: {e}")

        
class AddSomethingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose what to add...")
        self.resize(400, 150)
        self.setFixedSize(400, 150)
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        # Widget functions
        def AddRoutine():
            self.close()
            self.RoutineWindow = AddRoutineWindow()
            self.RoutineWindow.show()

        def AddTime():
            self.close()
            self.TimeWindow = AddTimeWindow()
            self.TimeWindow.show()

        def AddSubdur():
            self.close()
            self.SubdurWindow = AddSubdurationWindow()
            self.SubdurWindow.show()

        def close():
            self.close()

        # Widgets
        QLabel("What would you like to add?", self).setGeometry(125, 10, 150, 20)
        QPushButton("Add a Routine", self, clicked = AddRoutine).setGeometry(40, 50, 150, 40)
        QPushButton("Add a Time", self, clicked = AddTime).setGeometry(210, 50, 150, 40)
        QPushButton("Add Subdurations", self, clicked = AddSubdur).setGeometry(40, 100, 150, 40)
        self.cancelButton = QPushButton("Cancel", self, clicked = close)
        self.cancelButton.setGeometry(210, 100, 150, 40)
        self.cancelButton.setStyleSheet("color: red;")

class EditSomethingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose what to edit...")
        self.resize(400, 150)
        self.setFixedSize(400, 150)
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        # Widgets
        QLabel("What would you like to edit?", self).setGeometry(125, 10, 155, 30)
        QPushButton("Edit name", self, clicked = self.nameEdit).setGeometry(40, 50, 150, 40)
        QPushButton("Edit time", self, clicked = self.timeEdit).setGeometry(210, 50, 150, 40)
        QPushButton("Edit subdurations", self, clicked = self.subdurationsEdit).setGeometry(40, 100, 150, 40)
        self.cancelButton = QPushButton("Cancel", self, clicked = self.close)
        self.cancelButton.setGeometry(210, 100, 150, 40)
        self.cancelButton.setStyleSheet("color: red;")

    def nameEdit(self):
        self.close()
        self.editNameWindow = EditNameWindow()
        self.editNameWindow.show()

    def timeEdit(self):
        self.close()
        self.editTimeWindow = EditTimeWindow()
        self.editTimeWindow.show()

    def subdurationsEdit(self):
        self.close()
        self.editSubdurationsWindow = EditSubdurationsWindow()
        self.editSubdurationsWindow.show()


class ClearSomethingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Choose what to clear...")
        self.resize(400, 150)
        self.setFixedSize(400, 150)
        self.setWindowIcon(QIcon(str(icon_path)))
        self.setWindowModality(Qt.WindowModality.ApplicationModal)

        # Widgets


class Tracker(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Routine Tracker v1")
        self.setWindowIcon(QIcon(str(icon_path)))
        self.resize(500, 500)
        self.setFixedSize(500, 500)

        # Widget functions
        def add_button():
            self.addingWindow = AddSomethingWindow()
            self.addingWindow.show()

        def edit_button():
            self.editingWindow = EditSomethingWindow()
            self.editingWindow.show()

        def clear_button():
            self.clearingWindow = ClearSomethingWindow()
            self.clearingWindow.show()

        # Widgets
        QLabel("Manage Routines:", self).setGeometry(200, 10, 100, 30)
        QPushButton("Add something...", self, clicked = add_button).setGeometry(10, 50, 150, 40)
        QPushButton("Edit something...", self, clicked = edit_button).setGeometry(174, 50, 150, 40)
        QPushButton("Clear something...", self, clicked = clear_button).setGeometry(338, 50, 150, 40)
        QLabel("____________________________________________________________________________________________________", self).setGeometry(10, 90, 480, 30)
        QLabel("Week Viewer:", self).setGeometry(212, 120, 100, 30)
        

app = QApplication([])
window = Tracker()
window.show()
app.exit(app.exec())


"""
try:
    action = int(input("What routine tool would you like to use?\n1. Routine adder (for adding routines or information to routines)\n2. Routine clearer (for removing a routine a whole day or infos from a routine)\n3. Routine editor (for editing various information about a routine)\n4. Routine reader (for printing todays routines)\n5. View statistics\n6. Exit\n"))
    if action == 1:
        adder_option = int(input("What would you like to add?\n1. A routine\n2. A time to a routine without time\n3. A duration to a routine with no duration\n4. A subduration to a routine with a duration\n"))
        if adder_option == 1:
                adder_option_1_day = int(input("To what day would you like to add a routine (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
                adder_option_1_name = str(input("Please enter the name of your routine: "))
                adder_option_1_time = input("Please enter the time (None for no specific time): ")
                if adder_option_1_time.lower() == "none":
                    adder_option_1_time = None
                adder_option_1_duration = input("Please enter you duration in minutes (None for no specific duration): ")
                if adder_option_1_duration.lower() == "none":
                    adder_option_1_duration = None
                if adder_option_1_duration:
                    adder_option_1_subdurations_notlist = input("Please enter your subdurations in minutes with a comma and a space between the numbers (None for no subduration): ")
                    if adder_option_1_subdurations_notlist.lower() != "none":
                        adder_option_1_subdurations = list(map(int, adder_option_1_subdurations_notlist.split(',')))
                        if int(sum(adder_option_1_subdurations)) != int(adder_option_1_duration):
                            raise AssertionError(f"{Bcolor.FAIL}Please enter subdurations adding up to you duration. Sum is: {sum(adder_option_1_subdurations)}, but duration is: {adder_option_1_duration}{Bcolor.ENDC}")
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
            print(f"{Bcolor.FAIL}Please only enter a number between 1 and 4!{Bcolor.ENDC}")
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
            print(f"{Bcolor.FAIL}Please only enter a number between 1 and 5!{Bcolor.ENDC}")

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
            print(f"{Bcolor.FAIL}NOTE: All previously added subdurations will be deleted if you add new subdurations!{Bcolor.ENDC}")
            editor_option_4_day = int(input("From what day would you like to edit subdurations (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            editor_option_4_name = str(input("Please enter the name of your routine: "))
            editor_option_4_subdurations_notlist = input("Please enter your new subdurations in minutes with a comma and a space between the numbers: ")
            print(routine.edit.subdurations(editor_option_4_day, editor_option_4_name, list(map(int, editor_option_4_subdurations_notlist.split(',')))))
        else:
            print(f"{Bcolor.FAIL}Please only enter a number between 1 and 4!{Bcolor.ENDC}")

    elif action == 4:
        option_4 = input("What would you like to view?\n1. Today's routine\n2. A specific day's routine\n3. The completion status of today's routines\n")
        if option_4 == "1":
            if routine.read.routine(current_day) != "No routine today!":
                play_choice = input("\n\nWould you like to play your routine? (y/n): ")
                if play_choice.lower() == "y":
                    print(f"{Bcolor.OKGREEN}Starting your routine!{Bcolor.ENDC}")
                    routine.play.play_routine()
                elif play_choice.lower() == "n":
                    print(f"{Bcolor.WARNING}You chose not to play your routine. Exiting the program.{Bcolor.ENDC}")
            else:
                print(f"{Bcolor.WARNING}You have no routine today. Exiting the program.{Bcolor.ENDC}")
        elif option_4 == "2":
            specific_day = int(input("Please enter the day you would like to view (1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday): "))
            if routine.read.routine(specific_day) != "No routine today!":
                play_choice = input("\n\nWould you like to play your routine? (y/n): ")
                if play_choice.lower() == "y":
                    print(f"{Bcolor.OKGREEN}Starting your routine!{Bcolor.ENDC}")
                    routine.play.play_routine()
                elif play_choice.lower() == "n":
                    print(f"{Bcolor.WARNING}You chose not to play your routine. Exiting the program.{Bcolor.ENDC}")
            else:
                print(f"{Bcolor.WARNING}You have no routine for {_normalize_day(specific_day)}. Exiting the program.{Bcolor.ENDC}")
        elif option_4 == "3":
            routine.read.completion_status()
    elif action == 5:
        with open(statistics_folder / "statistics.json", "r+", encoding="utf-8") as file:
            data = json.load(file)
            stats = data["statistics"][0]
            for key, value in stats.items():
                print(f"{key} = {value}")
    elif action == 6:
        print(f"{Bcolor.FAIL}Exiting the programm...{Bcolor.ENDC}")
        exit()

    else:
        print(f"{Bcolor.FAIL}Please only enter a number between 1 and 6!{Bcolor.ENDC}")

            
except ValueError as e:
    print(f"{Bcolor.FAIL}Please only enter valid formats! {e}{Bcolor.ENDC}")
except TypeError as e:
    print(f"{Bcolor.FAIL}Please make sure you followed the instructions for the format! The following error occured: {e}{Bcolor.ENDC}")
except Exception as e:
    print(f"{Bcolor.FAIL}Ending script with error: {e}{Bcolor.ENDC}")

"""