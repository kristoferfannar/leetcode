#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define fill(a)                                                                \
    for (auto &element : a)                                                    \
        cin >> element;
#define sz(s) (ll) s.size()
#define YES (cout << "YES\n")
#define NO (cout << "NO\n")

struct llist {
    struct llist *prev;
    unique_ptr<struct llist> next;
    string url;

    llist(string url, struct llist *prev) : prev(prev), url(url) {}
};

class BrowserHistory {
  private:
    unique_ptr<struct llist> list;
    struct llist *curr;

  public:
    BrowserHistory(string homepage) {
        list = make_unique<llist>(homepage, nullptr);
        curr = list.get();
    };

    void visit(string url) {
        unique_ptr<struct llist> nw = make_unique<llist>(url, curr);

        curr->next = std::move(nw);
        curr = curr->next.get();
    }

    string back(int steps) {
        while (steps-- && curr->prev)
            curr = curr->prev;

        return curr->url;
    }

    string forward(int steps) {
        while (steps-- && curr->next)
            curr = curr->next.get();

        return curr->url;
    }
};

int main() {
    auto s = BrowserHistory("leetcode.com");
    s.visit("google.com");
    s.visit("facebook.com");
    s.visit("youtube.com");
    assert(s.back(1) == "facebook.com");
    assert(s.back(1) == "google.com");
    assert(s.forward(1) == "facebook.com");
    s.visit("linkedin.com");
    assert(s.forward(2) == "linkedin.com");
    assert(s.back(2) == "google.com");
    assert(s.back(7) == "leetcode.com");
}
