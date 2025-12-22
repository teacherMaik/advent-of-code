from pathlib import Path
import sys
import math

# Add root folder to path so we can import python_utils
ROOT = Path(__file__).parent.parent.parent.resolve()
sys.path.insert(0, str(ROOT))

from python_utils import get_input

day = 2
year = 2025

data = get_input(day, year)
print(f"Input for {year}-Day {day}:\n{data[:100]}...")  # just print first 100 chars

# --- Cache file path (same folder as script) ---
script_folder = Path(__file__).parent
cache_file = script_folder / f"day_{day}_data.txt"

# --- Load input ---
if cache_file.exists():
    data = cache_file.read_text()
    print(f"Loaded input for {year}-Day {day} from {cache_file.name}.")
else:
    data = get_input(day, year)
    cache_file.write_text(data)
    print(f"Downloaded input for {year}-Day {day} and saved to {cache_file.name}.")


with cache_file.open() as f:

    dataArr = []
    for line in f:

        line = line.strip()
        if not line:
            continue

        parts = line.split(',')
        dataArr.extend(parts)

    print(len(dataArr))
    print(dataArr[0])


    for data in dataArr:
        limits = data.split('-')
        start = int(limits[0].strip())
        finish = int(limits[1].strip())

        print(start, finish)

        num = start
        while num <= finish:
            numStr = str(num)
            print(numStr)

            num += 1