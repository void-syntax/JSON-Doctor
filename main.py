import argparse
import json
from pathlib import Path


def resolve_file_path(input_path_str: str) -> Path | None:
    target = Path(input_path_str)

    if target.exists():
        return target

    user_home = Path.home()
    search_dirs = [
        user_home / "Desktop",
        user_home / "Downloads",
        user_home / "Documents",
        user_home / "Projects",
    ]

    for directory in search_dirs:
        candidate = directory / target.name
        if candidate.exists():
            return candidate

    return None


parser = argparse.ArgumentParser(
    description="JSON Doctor - A tool to validate and format JSON data."
)
parser.add_argument("--file", required=True, help="Path or name of the JSON file")
parser.add_argument("--pretty", action="store_true", help="Print formatted JSON.")
args = parser.parse_args()

file_path = resolve_file_path(args.file)

if not file_path:
    print(
        f"Error: The file '{args.file}' was not found in current directory or standard user folders."
    )
    exit(1)
elif not file_path.is_file():
    print(f"Error: '{file_path}' is not a valid file.")
    exit(1)

try:
    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)

    print("JSON Doctor")
    print("-----------")
    print(f"File   : {file_path.name}")
    print(f"Path   : {file_path.resolve()}")
    print("Status : Valid JSON")
    print(f"Type   : {type(data).__name__}")

    if args.pretty:
        print("\nFormatted JSON:")
        print(json.dumps(data, indent=2, ensure_ascii=False))

except json.JSONDecodeError as error:
    print("JSON Doctor")
    print("-----------")
    print(f"File   : {file_path.name}")
    print("Status : Invalid JSON")
    print(f"Error  : {error.msg}")
    print(f"Line   : {error.lineno}")
    print(f"Column : {error.colno}")

except OSError as error:
    print(f"File error : {error}")