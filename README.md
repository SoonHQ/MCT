# MCT - Martian Coordinated Time

A Python library for handling Martian Coordinated Time (MCT), a UTC-like time system designed for Mars based on the Martian sol.

## Overview

`MCT` provides a standalone framework for managing time on Mars, using the Martian sol (approximately 24 hours, 39 minutes, and 35.244 seconds) as its fundamental unit. It features:
- Current time in MCT.
- Time addition and subtraction.
- Time difference calculations.

This library is ideal for Martian mission planning, hypothetical scheduling on Mars, or exploring extraterrestrial timekeeping.

## Installation

Clone the repository or download `mct.py` directly:

```bash
git clone https://github.com/SoonHQ/MarsTime.git
```
Then, copy mct.py into your project directory and import it as needed.
Alternatively, download mct.py from the releases page or the repository’s main page and place it in your project.

## Usage

### Get Current Martian Time
```python
from mct import MarsTime

now = MarsTime.now()
print(now.to_string())  # Example: "MCT Sol 17859 08:13:45.123"
```

### Add Time
```python

future = now.add_time(sols=2, hours=5)
print(future.to_string())  # Example: "MCT Sol 17861 13:13:45.123"
```

### Calculate Time Difference
```python

diff = future.difference(now)
print(diff.to_string())  # Example: "MCT Sol 2 05:00:00.000"
```

### Subtract Time
```python

past = now.subtract_time(sols=1, hours=3)
print(past.to_string())  # Example: "MCT Sol 17858 05:13:45.123"
```

## Time System
**Martian Coordinated Time (MCT):** A standardized time system for Mars, starting at Sol 0 (aligned with Viking 1 landing, 1976-07-20 UTC).

**Sol:** 88,775.244 Earth seconds (~24h 39m 35s).

**Clock:** 24 Martian hours (61.65 Earth minutes each), 60 Martian minutes (61.65 Earth seconds each).

## Contributing
Contributions are welcome! Fork the repo, submit issues, or send pull requests. Suggestions for Martian time zones, mission-specific features, or improved precision are appreciated.

## License
This project is licensed under the GNU General Public License v3.0 (GPLv3). See below for details:

MCT - Martian Coordinated Time
Copyright (C) 2025 Soon

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <https://www.gnu.org/licenses/>.

For the full license text, refer to the LICENSE file in this repository.

3. **GPLv3 Summary**:
   - The license requires anyone distributing modified versions to share their source code under the same terms. It’s more restrictive than MIT but ensures the library stays open-source.

4. **Push to GitHub**:
   - If not already done: `git init`, `git add .`, `git commit -m "Initial commit with MCT library"`, `git remote add origin https://github.com/SoonHQ/MCT.git`, `git push -u origin main`.
