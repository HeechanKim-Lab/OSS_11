
#include <iostream>
using namespace std;

int main()
{
    double a, b, h, sum1, sum2, sum3;
    const double PI = 3.14159;
    
    cout << "실수 3개를 입력하세요: ";
    cin >> a >> b >> h;

    sum1 = ((a + b) * h / 2);
    sum2 = PI * a * a;
    sum3 = sum2 * h;

    cout << "밑변 " << a << ", 윗변 " << b << ", 높이 " << h << "인 사다리꼴의 넓이는" << sum1 << endl; 
    cout << "반지름 " << a << "인 원의 넓이는" << sum2 << endl; 
    cout << "반지름 " << a << ", 높이 " << h << "인 원기둥의 부피는" << sum3 << endl;

    return 0;

}