
#include <iostream>
using namespace std;

int main()
{
    int number;
    cout << "정수 입력: ";
    cin >> number;
    cout << number << "이하 자연수 중" << endl;
    cout << "3 혹은 5의 배수는" << endl;
    cout << "---------------" << endl;

    int i = 1, count = 0;
    while ( i <= number )
    {
        if ( i % 3 == 0 || i % 5 == 0 )
        {
            cout << i << endl;
            count++;
        }
        i++;
    }

    cout << "---------------" << endl;
    cout << "총 " << count << " 개입니다." << endl;
}