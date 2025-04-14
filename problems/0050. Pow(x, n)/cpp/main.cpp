class Solution {
private: 
    double pow(double x, int n) {
        if (n == 0) return 1;

        auto p = pow(x, n / 2);
        if (n % 2)
            return x * p * p;
        return p * p;
    }
public:
    double myPow(double x, int n) {
        auto res = pow(x, n);
        if (n < 0) return 1 / res;
        return res;
    }
};
