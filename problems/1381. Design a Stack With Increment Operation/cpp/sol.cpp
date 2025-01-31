#include <bits/stdc++.h>
using namespace std;

class CustomStack {
private:
  vector<int> stack;
  const int maxSize;

public:
  CustomStack(int maxSize) : stack(), maxSize(maxSize) {}

  void push(int x) {
    if ((int)stack.size() < maxSize)
      stack.push_back(x);
  }

  int pop() {
    if (stack.size() == 0)
      return -1;
    auto item = stack.back();
    stack.pop_back();
    return item;
  }

  void increment(int k, int val) {
    for (int i = 0; i < min(k, (int)stack.size()); i++)
      stack[i] += val;
  }
};

int main() {
  auto s = new CustomStack(1000);
  s->push(1);
  assert(s->pop() == 1);
  assert(s->pop() == -1);

  s->push(1);
  s->push(1);
  s->push(1);
  s->push(1);
  s->push(1);
  s->increment(3, 1);
  assert(s->pop() == 1);
  assert(s->pop() == 1);
  assert(s->pop() == 2);
  assert(s->pop() == 2);
  assert(s->pop() == 2);
}
