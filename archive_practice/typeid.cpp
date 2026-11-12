/* 자료형 변환 */

#include <iostream>
#include <typeinfo>
using namespace std;

int main()
{
    bool x = true;
    char y = 'A';
    short z = 14;
    float t = 24.5;

    cout << "x + 100의 자료형, 값: " << typeid(x + 100).name() << ", " << x + 100 << endl;
    cout << "y + 100의 자료형, 값: " << typeid(y + 100).name() << ", " << y + 100 << endl;
    cout << "z + 100의 자료형, 값: " << typeid(z + 100).name() << ", " << z + 100 << endl;
    cout << "t + 100의 자료형, 값: " << typeid(t + 15000.2).name() << ", " << t + 15000.2;

    return 0;
}