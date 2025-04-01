from datetime import timedelta
import time

class MarsTime:
    # Martian sol length in Earth seconds
    MARS_SECONDS_PER_SOL = 88775.244  # ~24h 39m 35.244s
    # Reference epoch: First sol of MCT, set to Viking 1 landing (July 20, 1976 UTC)
    MCT_EPOCH = 237552000  # Unix timestamp for 1976-07-20 00:00:00 UTC

    def __init__(self, sol=0, hours=0, minutes=0, seconds=0.0):
        """Initialize with a Martian time (sol number and time within the sol)."""
        self.sol = sol
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
        self._normalize()

    @classmethod
    def now(cls):
        """Create a MarsTime instance based on current Earth UTC time converted to MCT."""
        earth_seconds_since_epoch = time.time() - cls.MCT_EPOCH
        total_sols = earth_seconds_since_epoch / cls.MARS_SECONDS_PER_SOL
        sol_number = int(total_sols)
        sol_fraction = total_sols - sol_number
        hours = int(sol_fraction * 24)
        minutes = int((sol_fraction * 24 - hours) * 60)
        seconds = (sol_fraction * 24 * 3600 - (hours * 3600 + minutes * 60))
        return cls(sol_number, hours, minutes, seconds)

    def _normalize(self):
        """Normalize time components to fit within a sol (24 Martian hours)."""
        total_seconds = self.hours * 3600 + self.minutes * 60 + self.seconds
        extra_sols = int(total_seconds // self.MARS_SECONDS_PER_SOL)
        remaining_seconds = total_seconds % self.MARS_SECONDS_PER_SOL

        self.sol += extra_sols
        self.hours = int(remaining_seconds // 3698.9685)  # Martian hour ~3698.9685 Earth seconds
        remaining_seconds %= 3698.9685
        self.minutes = int(remaining_seconds // 61.649475)  # Martian minute ~61.649475 Earth seconds
        self.seconds = remaining_seconds % 61.649475

        if self.hours >= 24:
            self.sol += self.hours // 24
            self.hours %= 24

    def add_time(self, sols=0, hours=0, minutes=0, seconds=0):
        """Add time to the current MarsTime instance."""
        self.sol += sols
        self.hours += hours
        self.minutes += minutes
        self.seconds += seconds
        self._normalize()
        return self

    def subtract_time(self, sols=0, hours=0, minutes=0, seconds=0):
        """Subtract time from the current MarsTime instance."""
        self.sol -= sols
        self.hours -= hours
        self.minutes -= minutes
        self.seconds -= seconds
        self._normalize()
        if self.sol < 0:
            raise ValueError("Time cannot go before MCT epoch (Sol 0)")
        return self

    def difference(self, other):
        """Calculate the difference between two MarsTime instances in sols and time."""
        total_seconds_self = (self.sol

 * self.MARS_SECONDS_PER_SOL + 
                              self.hours * 3698.9685 + self.minutes * 61.649475 + self.seconds)
        total_seconds_other = (other.sol * self.MARS_SECONDS_PER_SOL + 
                               other.hours * 3698.9685 + other.minutes * 61.649475 + other.seconds)
        diff_seconds = total_seconds_self - total_seconds_other

        sols = int(diff_seconds // self.MARS_SECONDS_PER_SOL)
        remaining_seconds = diff_seconds % self.MARS_SECONDS_PER_SOL
        hours = int(remaining_seconds // 3698.9685)
        minutes = int((remaining_seconds % 3698.9685) // 61.649475)
        seconds = remaining_seconds % 61.649475

        return MarsTime(sols, hours, minutes, seconds)

    def to_string(self):
        """Format as a readable string."""
        return f"MCT Sol {self.sol} {self.hours:02d}:{self.minutes:02d}:{self.seconds:06.3f}"

# Example usage (for testing purposes)
if __name__ == "__main__":
    # Current Martian time
    now = MarsTime.now()
    print("Current MCT:", now.to_string())

    # Schedule something 2 sols and 5 hours from now
    future = now.add_time(sols=2, hours=5)
    print("Future MCT:", future.to_string())

    # Difference between now and future
    diff = future.difference(now)
    print("Time difference:", diff.to_string())

    # Subtract 1 sol and 3 hours
    past = now.subtract_time(sols=1, hours=3)
    print("Past MCT:", past.to_string())
