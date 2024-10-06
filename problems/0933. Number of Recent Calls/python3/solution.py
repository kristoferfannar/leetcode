class RecentCounter:

    def __init__(self):
        self.requests = []
        self.t = 0

    def ping(self, t: int) -> int:
        self.requests.insert(0, t)
        count = 0
        while True:
            if count < len(self.requests) and t - self.requests[count] <= 3000:
                count += 1
            else:
                break

        return count


if __name__ == "__main__":
    s = RecentCounter()
    s.ping(1)
    s.ping(2)
    s.ping(100)
    s.ping(3001)
    ans = s.ping(3002)
    print(ans)
    assert ans == 4
