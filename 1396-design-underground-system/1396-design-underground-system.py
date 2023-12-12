class UndergroundSystem:

    def __init__(self):
        self.checkInMap = {}  # Uid - [StationName, Time]
        # Dictionary to store the total time taken for each route
        # Key: (startStation, endStation), Value: total time
        self.routeTotalTime = defaultdict(int)

        # Dictionary to store the count of trips for each route
        # Key: (startStation, endStation), Value: number of trips
        self.routeCount = defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # Records the check-in information when a customer checks in
        self.checkInMap[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Retrieves the check-in information for the customer
        startStation, startTime = self.checkInMap.pop(id)

        # Forms a tuple representing the route (startStation, endStation)
        routeName = (startStation, stationName)

        # Updates the total time and count for the route
        self.routeTotalTime[routeName] += t - startTime
        self.routeCount[routeName] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # Calculates and returns the average time for a given route
        routeName = (startStation, endStation)
        return self.routeTotalTime[routeName] / self.routeCount[routeName]