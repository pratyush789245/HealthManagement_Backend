import csv
import datetime
import json
import os
from typing import List, Tuple, Any


def _entries_from_csv(path: str) -> List[Tuple[str, Any, Any]]:
    entries: List[Tuple[str, Any, Any]] = []
    with open(path, mode='r', newline='', encoding='utf-8') as f:
        reader = csv.reader(f)
        try:
            header = next(reader)
        except StopIteration:
            return entries
        for r in reader:
            if any(cell.strip() for cell in r):
                
                nums = [c.strip() for c in r if c.strip()]
                if len(nums) >= 2:
                    entries.append(('user', nums[0], nums[1]))
    return entries


def _entries_from_json(path: str) -> List[Tuple[str, Any, Any]]:
    entries: List[Tuple[str, Any, Any]] = []
    with open(path, mode='r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, dict):
        user_label = data.get('current_user', 'user')
        h = data.get('height')
        w = data.get('weight')
        if h is not None and w is not None:
            entries.append((user_label, h, w))
            return entries

        users = data.get('users')
        if isinstance(users, dict):
            for name, val in users.items():
                if isinstance(val, dict):
                    h = val.get('height')
                    w = val.get('weight')
                    if h is not None and w is not None:
                        entries.append((name, h, w))

    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict):
                name = item.get('name', 'user')
                h = item.get('height')
                w = item.get('weight')
                if h is not None and w is not None:
                    entries.append((name, h, w))

    return entries


def compute_bmis(input_path: str = 'users_data.json', output_path: str = 'bmi_logs.csv') -> None:
    if not os.path.exists(input_path):
        print(f"Error: {input_path} not found.")
        return

    entries: List[Tuple[str, Any, Any]] = []
    if input_path.lower().endswith('.json'):
        entries = _entries_from_json(input_path)
    else:
        entries = _entries_from_csv(input_path)

    if not entries:
        print("No valid height/weight entries found in input.")
        return

    file_needs_header = not os.path.exists(output_path) or os.path.getsize(output_path) == 0
    with open(output_path, mode='a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        if file_needs_header:
            writer.writerow(['User', 'BMI', 'Computed on'])

        for user_label, h_raw, w_raw in entries:
            try:
                height = float(h_raw)
                weight = float(w_raw)
                if height > 3:
                    height = height / 100.0
                bmi_val = round(weight / (height ** 2), 2)
                timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                writer.writerow([bmi_val, timestamp])
            except Exception:
                continue

    print(f"BMI calculations saved to {output_path}")


if __name__ == '__main__':
    compute_bmis()