/*
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    double hours, rate, regularPay, overPay, totalPay;

    cout << "업무 시간을 입력하세요: ";
    cin >> hours;
    cout << "시간당 급여를 입력하세요: ";
    cin >> rate;

    regularPay = hours * rate;
    overPay = 0.0;

    if(hours>40.0)
    {
        overPay = (hours-40.0) * rate * 0.30;
    }

    totalPay = regularPay + overPay;

    cout << fixed << showpoint;
    cout << "일반 급여 = " << setprecision(2) << regularPay << endl;
    cout << "초과 근무에 대한 급여 = " << setprecision(2) << overPay << endl;
    cout << "전체 급여 = " << setprecision(2) << totalPay << endl;

    return 0;
}
    */