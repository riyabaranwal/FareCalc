# FareCalc

A lightweight Python command-line application for estimating ride fares based on:
- distance traveled (km)
- vehicle category
- travel hour (with surge pricing support)

This project is ideal as a beginner-friendly example of input handling, conditional pricing logic, and formatted console output.

## Features

- Supports multiple vehicle categories:
  - Economy
  - Premium
  - SUV
- Calculates total fare using per-km base rates
- Applies automatic surge pricing (1.5x) during peak hours (17:00-20:00)
- Prints a clean ride estimate receipt
- Handles invalid numeric input with user-friendly error messaging

## Project Structure

```text
FareCalc/
|- fareCalc.py
|- README.md
```

## Requirements

- Python 3.8+

No external dependencies are required.

## How It Works

Base rates (INR per km):
- Economy: 10
- Premium: 18
- SUV: 25

Fare formula:
1. `total_fare = distance_km * base_rate`
2. If travel hour is between `17` and `20` (inclusive), apply surge:
   - `total_fare = total_fare * 1.5`

If an unsupported vehicle type is entered, the script reports service unavailability.

## Run the Project

From the project root:

```bash
python fareCalc.py
```

You will be prompted to enter:
- distance in km
- vehicle type (`Economy`, `Premium`, or `SUV`)
- hour of travel (`0-23`)

## Example

```text
Enter distance (in km): 12
Enter vehicle type (Economy / Premium / SUV): Premium
Enter hour of travel (0-23): 18

--- Ride Estimate Receipt ---
Distance Travelled : 12.0 km
Vehicle Type       : Premium
Base Rate (/km)    : INR 18
Surge Applied      : Yes (1.5x)
Total Fare         : INR 324.00
-------------------------
```

## Error Handling

- Invalid numeric values for distance or hour trigger a `ValueError` and show a clear message.
- Invalid vehicle categories are handled gracefully by returning service unavailability.

## Possible Enhancements

- Normalize vehicle type input (`economy`, `ECONOMY`, etc.)
- Validate hour range strictly (`0-23`)
- Reject negative distance values
- Add automated unit tests for fare rules
- Refactor script into a reusable module + CLI entrypoint

## License

This project currently has no license file. Add a `LICENSE` file if you plan to distribute it publicly.
