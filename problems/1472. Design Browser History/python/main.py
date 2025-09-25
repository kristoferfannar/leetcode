class BrowserHistory:
    def __init__(self, homepage: str):
        self.sites = [homepage]
        self.position = 0

    def visit(self, url: str) -> None:
        if self.position <= len(self.sites) - 1:
            self.sites = self.sites[: self.position + 1]

        self.sites.append(url)
        self.position += 1

    def back(self, steps: int) -> str:
        self.position = max(0, self.position - steps)
        return self.sites[self.position]

    def forward(self, steps: int) -> str:
        self.position = min(self.position + steps, len(self.sites) - 1)
        return self.sites[self.position]


if __name__ == "__main__":
    bh = BrowserHistory("leetcode.com")
    bh.visit("google.com")
    bh.visit("facebook.com")
    bh.visit("youtube.com")

    assert bh.back(1) == "facebook.com"
    assert bh.back(1) == "google.com"
    assert bh.forward(1) == "facebook.com"

    bh.visit("linkedin.com")

    assert bh.forward(2) == "linkedin.com"
    assert bh.back(2) == "google.com"
    assert bh.back(7) == "leetcode.com"
