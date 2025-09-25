class UndergroundSystem:

    def __init__(self):
        self.checkedIn: dict[int, tuple[str, int]] = {}
        self.times: dict[tuple[str, str], tuple[int, int]] = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        checkin_station, checkin_time = self.checkedIn[id]
        del self.checkedIn[id]

        travel_time = t - checkin_time
        key = (checkin_station, stationName)

        if key not in self.times:
            self.times[key] = (0, 0)

        total_traveled, num_traveled = self.times[key]
        timesheet = (total_traveled + travel_time, num_traveled + 1)

        self.times[key] = timesheet

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_traveled, num_traveled = self.times[(startStation, endStation)]

        return total_traveled / num_traveled


if __name__ == "__main__":
    obj = UndergroundSystem()
    obj.checkIn(45, "Leyton", 3)
    obj.checkIn(32, "Paradise", 8)
    obj.checkIn(27, "Leyton", 10)
    obj.checkOut(45, "Waterloo", 15)
    obj.checkOut(27, "Waterloo", 20)
    obj.checkOut(32, "Cambridge", 22)
    assert obj.getAverageTime("Paradise", "Cambridge") == 14.0
    assert obj.getAverageTime("Leyton", "Waterloo") == 11.0
    obj.checkIn(10, "Leyton", 24)
    assert obj.getAverageTime("Leyton", "Waterloo") == 11.0
    obj.checkOut(10, "Waterloo", 38)
    assert obj.getAverageTime("Leyton", "Waterloo") == 12.0
