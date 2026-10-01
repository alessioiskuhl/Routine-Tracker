import ast
import contextlib
import builtins
import io
import json
import tempfile
from pathlib import Path
from unittest.mock import patch
from tkinter import messagebox


all_tests_passed = True
ISSUES_URL = "https://github.com/alessioiskuhl/Routine-Tracker/issues"

MAIN_PATH = (
    Path(__file__).resolve().parents[1]
    / "src"
    / "routine-tracker"
    / "main.py"
)


def expect_exception(exception_type, callback):
    try:
        callback()
    except exception_type:
        return
    except Exception as error:
        raise AssertionError(
            f"Expected {exception_type.__name__}, got {type(error).__name__}"
        ) from error
    raise AssertionError(f"Expected {exception_type.__name__} to be raised")


def load_isolated_module(temp_dir):
    source = MAIN_PATH.read_text(encoding="utf-8")
    syntax_tree = ast.parse(source, filename=str(MAIN_PATH))

    def is_interactive_cli(statement):
        return isinstance(statement, ast.Try) and any(
            isinstance(node, ast.Name)
            and node.id == "action"
            and isinstance(node.ctx, ast.Store)
            for node in ast.walk(statement)
        )

    syntax_tree.body = [
        statement
        for statement in syntax_tree.body
        if not is_interactive_cli(statement)
    ]
    namespace = {
        "__name__": "routine_tracker_under_test",
        "__file__": str(Path(temp_dir) / "main.py"),
    }
    exec(compile(syntax_tree, str(MAIN_PATH), "exec"), namespace)
    return namespace


def print_test_report(results):
    failures = [name for name, passed, _ in results if not passed]
    passed_count = len(results) - len(failures)
    print(f"TEST REPORT: {passed_count} passed, {len(failures)} failed")
    if failures:
        print(f"Failed checks: {', '.join(failures)}")
        print(f"Report an issue: {ISSUES_URL}")


def run_tests():
    global all_tests_passed

    all_tests_passed = True
    test_results = []
    with tempfile.TemporaryDirectory(prefix="routine_tracker_tests_") as temp_dir:
        temp_dir_path = Path(temp_dir)
        try:
            module = load_isolated_module(temp_dir)
        except Exception as error:
            all_tests_passed = False
            print(f"\033[91mFAIL module setup: {error}\033[0m")
            test_results.append(("module setup", False, str(error)))
            print_test_report(test_results)
            return

        day_number = module["current_day"]
        day_name = module["_normalize_day"](day_number)
        base_name = "Automated Smoke Routine"
        editor_name = "Automated Editor Routine"
        renamed_base_name = "Directly Renamed Routine"
        adder = module["routine_adder"]()
        clearer = module["routine_clearer"]()
        editor = module["routine_edit"]()
        reader = module["routine_reader"]()
        progress = module["routine_progress"]()

        def check(name, callback):
            global all_tests_passed
            try:
                callback()
            except Exception as error:
                all_tests_passed = False
                test_results.append((name, False, str(error)))
                print(f"\033[91mFAIL {name}: {error}\033[0m")
            else:
                test_results.append((name, True, None))
                print(f"\033[92mPASS {name}\033[0m")

        def test_routine_files_created():
            for filename in module["DAY_FILES"].values():
                routine_path = module["routines_folder"] / filename
                assert routine_path.is_file(), f"Missing routine file: {filename}"
                data = json.loads(routine_path.read_text(encoding="utf-8"))
                assert "routines" in data
                assert f"progress{module['current_date']}" in data
            statistics_path = module["statistics_folder"] / "statistics.json"
            assert statistics_path.is_file()
            statistics = json.loads(statistics_path.read_text(encoding="utf-8"))
            assert len(statistics["statistics"]) == 1

        def test_module_normalize_day():
            assert module["_normalize_day"](1) == "monday"
            assert module["_normalize_day"]("FRIDAY") == "friday"

        def test_progress_normalize_day():
            method = module["routine_progress"]._normalize_day
            assert method(2) == "tuesday"
            assert method("SUNDAY") == "sunday"

        def test_progress_init():
            instance = module["routine_progress"]()
            assert instance.today == day_number
            assert instance.current_date == module["current_date"]

        def test_progress_get_current_routines():
            assert progress.get_current_routines() == []

        def test_adder_normalize_day():
            assert adder._normalize_day(3) == "wednesday"
            assert adder._normalize_day("MONDAY") == "monday"

        def test_adder_load_data():
            path, data = adder._load_data(day_number)
            assert path.name == f"{day_name}_routines.json"
            assert data["routines"] == []

        def test_adder_save_data():
            path = Path(temp_dir) / "save_test.json"
            expected = {"routines": [{"name": "saved"}]}
            adder._save_data(path, expected)
            assert json.loads(path.read_text(encoding="utf-8")) == expected

        def test_adder_routine():
            result = adder.routine(day_number, base_name, None, None, None)
            assert "Successfully added" in result
            expect_exception(
                Exception,
                lambda: adder.routine(day_number, base_name, None, None, None),
            )

        def test_adder_set_field():
            result = adder._set_field(day_number, base_name, "note", "test-note")
            assert "Successfully added note" in result
            expect_exception(
                AssertionError,
                lambda: adder._set_field(day_number, "missing", "note", "value"),
            )

        def test_adder_time():
            assert "Successfully added time" in adder.time(
                day_number, base_name, "08:00"
            )

        def test_adder_duration():
            assert "Successfully added duration" in adder.duration(
                day_number, base_name, 10
            )

        def test_adder_subdurations():
            assert "Successfully added subdurations" in adder.subdurations(
                day_number, base_name, [4, 6]
            )

        def test_progress_complete():
            adder.routine(day_number, "Progress Routine", None, None, None)
            progress.complete("Progress Routine")
            data = adder._load_data(day_number)[1]
            assert {"routine_Progress Routine_completed": True} in data[
                f"progress{module['current_date']}"
            ]
            stats = json.loads(
                (module["statistics_folder"] / "statistics.json").read_text(
                    encoding="utf-8"
                )
            )["statistics"][0]
            assert stats[f"completions today ({module['current_date']})"] == 1

        def test_clearer_normalize_day():
            assert clearer._normalize_day(4) == "thursday"
            assert clearer._normalize_day("SATURDAY") == "saturday"

        def test_clearer_load_data():
            path, data = clearer._load_data(day_number)
            assert path.name == f"{day_name}_routines.json"
            assert any(item["name"] == base_name for item in data["routines"])

        def test_clearer_save_data():
            path = Path(temp_dir) / "clear_save_test.json"
            expected = {"routines": []}
            clearer._save_data(path, expected)
            assert json.loads(path.read_text(encoding="utf-8")) == expected

        def test_edit_normalize_day():
            assert editor._normalize_day(5) == "friday"
            assert editor._normalize_day("SUNDAY") == "sunday"

        def test_edit_load_data():
            path, data = editor._load_data(day_number)
            assert path.name == f"{day_name}_routines.json"
            assert any(item["name"] == base_name for item in data["routines"])

        def test_edit_save_data():
            path = Path(temp_dir) / "edit_save_test.json"
            expected = {"routines": [{"name": "edited"}]}
            editor._save_data(path, expected)
            assert json.loads(path.read_text(encoding="utf-8")) == expected

        def test_edit_name_internal():
            result = editor._edit_name(day_number, base_name, renamed_base_name)
            assert "Successfully edited" in result

        def test_edit_field_internal():
            result = editor._edit_field(
                day_number, renamed_base_name, "note", "edited-note"
            )
            assert "Successfully edited note" in result

        def test_edit_name():
            adder.routine(day_number, editor_name, "07:00", 20, [10, 10])
            assert "Successfully edited" in editor.name(
                day_number, editor_name, "Edited Routine"
            )

        def test_edit_time():
            assert "Successfully edited time" in editor.time(
                day_number, renamed_base_name, "09:00"
            )

        def test_edit_duration():
            assert "Successfully edited duration" in editor.duration(
                day_number, renamed_base_name, 12
            )

        def test_edit_subdurations():
            assert "Successfully edited subdurations" in editor.subdurations(
                day_number, renamed_base_name, [5, 7]
            )

        def test_clearer_clear_field_internal():
            result = clearer._clear_field(
                day_number, renamed_base_name, "note"
            )
            assert "Successfully cleared note" in result

        def test_clearer_time():
            assert "Successfully cleared time" in clearer.time(
                day_number, renamed_base_name
            )

        def test_clearer_duration():
            assert "Successfully cleared duration" in clearer.duration(
                day_number, renamed_base_name
            )

        def test_clearer_subdurations():
            assert "Successfully cleared subdurations" in clearer.subdurations(
                day_number, renamed_base_name
            )

        def test_clearer_clear_routine_internal():
            adder.routine(day_number, "Direct Clear Routine", None, None, None)
            assert "Successfully cleared" in clearer._clear_routine(
                day_number, "Direct Clear Routine"
            )

        def test_clearer_routine():
            assert "Successfully cleared" in clearer.routine(
                day_number, renamed_base_name
            )

        def test_clearer_day():
            other_day = day_number % 7 + 1
            adder.routine(other_day, "Day Clear Routine", None, None, None)
            assert "Successfully cleared all routines" in clearer.day(other_day)
            assert clearer._load_data(other_day)[1]["routines"] == []

        def test_progress_player_setup():
            adder.routine(day_number, "Playback Routine", None, 0, None)
            module[f"{day_name}_routines"] = {
                "routines": [
                    {"name": "Playback Routine", "duration": 0, "subdurations": None}
                ]
            }
            module["data"] = adder._load_data(day_number)[1]
            output = io.StringIO()
            with patch.object(builtins, "input", return_value="n"):
                with contextlib.redirect_stdout(output):
                    module["routine_player"]().play_routine()
            assert "Finished routine: Playback Routine" in output.getvalue()
            refreshed_data = adder._load_data(day_number)[1]
            assert {"routine_Playback Routine_completed": True} in refreshed_data[
                f"progress{module['current_date']}"
            ]

        def test_reader_routine():
            for index, weekday in enumerate(module["DAY_NUMBERS"].values(), start=1):
                module[f"{weekday}_routines"] = {
                    "routines": [{"name": f"Routine {index}", "time": None, "duration": None}]
                }
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                for weekday_number in range(1, 8):
                    assert reader.routine(weekday_number) is None
            for index in range(1, 8):
                assert f"Routine {index}" in output.getvalue()

        def test_reader_completion_status():
            output = io.StringIO()
            with contextlib.redirect_stdout(output):
                reader.completion_status()
            assert "Completion Status" in output.getvalue()
            assert "Progress Routine: Completed" in output.getvalue()

        def test_clearer_clear_day_internal():
            assert clearer._load_data(day_number)[1]["routines"]
            assert "Successfully cleared all routines" in clearer._clear_day(
                day_number
            )
            assert clearer._load_data(day_number)[1]["routines"] == []

        def test_editor_init():
            instance = module["routine_editor"]()
            assert all(
                hasattr(instance, attribute)
                for attribute in ("add", "clear", "edit", "read", "play", "progress")
            )

        tests = [
            ("routine/statistics files created", test_routine_files_created),
            ("_normalize_day", test_module_normalize_day),
            ("routine_progress._normalize_day", test_progress_normalize_day),
            ("routine_progress.__init__", test_progress_init),
            ("routine_progress.get_current_routines", test_progress_get_current_routines),
            ("routine_adder._normalize_day", test_adder_normalize_day),
            ("routine_adder._load_data", test_adder_load_data),
            ("routine_adder._save_data", test_adder_save_data),
            ("routine_adder.routine", test_adder_routine),
            ("routine_adder._set_field", test_adder_set_field),
            ("routine_adder.time", test_adder_time),
            ("routine_adder.duration", test_adder_duration),
            ("routine_adder.subdurations", test_adder_subdurations),
            ("routine_progress.complete", test_progress_complete),
            ("routine_clearer._normalize_day", test_clearer_normalize_day),
            ("routine_clearer._load_data", test_clearer_load_data),
            ("routine_clearer._save_data", test_clearer_save_data),
            ("routine_edit._normalize_day", test_edit_normalize_day),
            ("routine_edit._load_data", test_edit_load_data),
            ("routine_edit._save_data", test_edit_save_data),
            ("routine_edit._edit_name", test_edit_name_internal),
            ("routine_edit._edit_field", test_edit_field_internal),
            ("routine_edit.name", test_edit_name),
            ("routine_edit.time", test_edit_time),
            ("routine_edit.duration", test_edit_duration),
            ("routine_edit.subdurations", test_edit_subdurations),
            ("routine_reader.routine", test_reader_routine),
            ("routine_reader.completion_status", test_reader_completion_status),
            ("routine_player.play_routine", test_progress_player_setup),
            ("routine_clearer._clear_routine", test_clearer_clear_routine_internal),
            ("routine_clearer._clear_field", test_clearer_clear_field_internal),
            ("routine_clearer.day", test_clearer_day),
            ("routine_clearer.time", test_clearer_time),
            ("routine_clearer.duration", test_clearer_duration),
            ("routine_clearer.subdurations", test_clearer_subdurations),
            ("routine_clearer.routine", test_clearer_routine),
            ("routine_clearer._clear_day", test_clearer_clear_day_internal),
            ("routine_editor.__init__", test_editor_init),
        ]

        for name, callback in tests:
            check(name, callback)

    if temp_dir_path.exists():
        all_tests_passed = False
        test_results.append(("temporary test files cleanup", False, "directory remains"))
        messagebox.showerror("Failed", "Temporary test files cleanup failed: temporary directory remains")
    else:
        test_results.append(("temporary test files cleanup", True, None))
        print("\033[92mPASS temporary test files cleanup\033[0m")

    print_test_report(test_results)
    if all_tests_passed:
        messagebox.showinfo("Passed", "All automated tests passed!")
    else:
        messagebox.showerror("Failed", "One or more automated tests failed. Check the console output for details.")
        print(f"Report an issue: {ISSUES_URL}")


if __name__ == "__main__":
    run_tests()
