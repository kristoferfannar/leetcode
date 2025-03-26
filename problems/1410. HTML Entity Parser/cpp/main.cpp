#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
  string entityParser(string text) {
    string out;

    /* probably faster to use a trie tree / dfa here so we don't have to perform
     * the dictionary lookups */
    map<string, char> mp = {{"&quot;", '"'}, {"&apos;", '\''},
                            {"&amp;", '&'},  {"&gt;", '>'},
                            {"&lt;", '<'},   {"&frasl;", '/'}};

    string curr;
    for (auto s : text) {
      if (s == '&') {
        out += curr;
        curr = "";
      }
      curr += s;
      if (s == ';') {
        if (mp.find(curr) != mp.end()) {
          out += mp[curr];
          curr = "";
        }
      }
    }

    out += curr;

    return out;
  }
};

int main() {
  auto s = Solution();

  assert(s.entityParser("&amp; is an HTML entity but &ambassador; is not.") ==
         "& is an HTML entity but &ambassador; is not.");

  assert(s.entityParser("and I quote: &quot;...&quot;") ==
         "and I quote: \"...\"");
}
