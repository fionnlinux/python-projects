# System Health Check

A simple Python script that checks disk usage and memory usage on a Linux
system, using `subprocess` to run shell commands and `re` to parse
their output.

## What it does

- Runs `df -h /` and extracts the disk usage percentage
- Runs `free -h` and extracts the amount of RAM currently in use
- Prints both in a clean, readable summary

## Usage

```bash
python3 health_check.py
```

No dependencies beyond the Python standard library.

## What I learned building this

- Using `subprocess.run()` to call shell commands from Python and
  capture their output.
- Writing regex patterns with `re.search()` to pull specific values out
  of command output.
- A real bug: my first regex for memory usage matched "total" RAM
  instead of "used" RAM, because `free -h` prints several similar-looking
  numbers on the same line. Fixed by anchoring the pattern on the literal
  text `Mem:` and skipping past the first number to reach "used".
- Another real bug: tried to convert a value like `"3.9"` to an integer
  with `int()`, which fails on decimal values. Switched to `float()`.

## Possible improvements

- Add a warning threshold (e.g. flag if disk usage is over 80%)
- Accept the threshold as a command-line argument instead of hardcoding it
- Save results to a JSON file with a timestamp, to track usage over time
- Use Python's `logging` module instead of `print()` for proper log levels
- Send an alert via a webhook if a threshold is breached
