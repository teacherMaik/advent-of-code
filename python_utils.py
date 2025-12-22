import os
from pathlib import Path
from dotenv import load_dotenv
import requests

# Always load .env from root
ROOT = Path(__file__).parent
load_dotenv(ROOT / '.env')

AOC_SESSION = os.getenv("AOC_SESSION")
if not AOC_SESSION:
    raise RuntimeError("AOC_SESSION not set in .env!")

def get_input(day: int, year: int) -> str:

    ## Download input for a given day/year.
    url = f"https://adventofcode.com/{year}/day/{day}/input"
    cookies = {"session": AOC_SESSION}
    r = requests.get(url, cookies=cookies)
    r.raise_for_status()
    return r.text

