// Last updated: 8/6/2026, 7:30:12 PM
double myPow(double x, int n) {
    if (n == 0)
        return 1.0;

    // handle negative exponent safely
    long long N = n;
    if (N < 0) {
        x = 1 / x;
        N = -N;
    }

    double result = 1.0;
    while (N > 0) {
        if (N % 2 == 1)
            result *= x;
        x *= x;
        N /= 2;
    }

    return result;
}
