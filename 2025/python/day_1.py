from pathlib import Path
import sys
import math

# Add root folder to path so we can import python_utils. Root is 3 leves up from here
ROOT = Path(__file__).parent.parent.parent.resolve()
sys.path.insert(0, str(ROOT))

from python_utils import get_input

day = 1
year = 2025

data = get_input(day, year)

## Preview up to 100 charcaters of the loaded input
print(f"Input for {year}-Day {day}:\n{data[:100]}...")

# Cache file path (same folder as script)
script_folder = Path(__file__).parent
cache_file = script_folder / f"day_{day}_data.txt"

# Load input from cached file if already exists, otherwise use utils module to load from AoC
if cache_file.exists():
    data = cache_file.read_text()
    print(f"Loaded input for {year}-Day {day} from {cache_file.name}.")
else:
    data = get_input(day, year)
    cache_file.write_text(data)
    print(f"Downloaded input for {year}-Day {day} and saved to {cache_file.name}.")


## Part 1
with cache_file.open() as f:

    dialPos = 50
    numNetZeros = 0

    for line in f:
        line = line.strip()
        if not line:
            continue
        
        # Separate letters from numbers
        direction = line[0]
        clicks = int(line[1:])

        if direction == 'R':
            dialPos = (dialPos + clicks) % 100
        else:
            dialPos = ((dialPos - clicks) % 100 + 100) % 100

        if dialPos == 0:
            numNetZeros += 1

    print(f"Answer for Day 1 Part 1 -> {numNetZeros}")


## Part 2
with cache_file.open() as f:

    dialPos = 50
    numNetZeros = 0

    for line in f:
        line = line.strip()
        if not line:
            continue

        direction = line[0]
        clicks = int(line[1:])

        ## Cal num of full turns (100's) add them to netZeros and get remaining clicks
        fullTurns = math.floor(clicks / 100)
        remainingClicks = clicks % 100

        numNetZeros += fullTurns

        if direction == 'R':
            end = dialPos + remainingClicks
            if end >= 100:
                numNetZeros += 1
            
            dialPos = end % 100
        else:
            end = dialPos - remainingClicks

            ## Edge case if turning left from 0
            if dialPos == 0:
                if remainingClicks == 100:
                    numNetZeros += 1
            else:
                if end <= 0:
                    numNetZeros += 1

            dialPos = ((end % 100) + 100) % 100


    print(f"Answer for Day 1 Part 2 -> {numNetZeros}")