
#include <iostream>
using namespace std;

int main()
{
    int temperature;
    bool hot;
    bool cold;

    cout << "현재 온도: ";
    cin >> temperature;

    hot = temperature >= 23;
    cold = temperature <= 15;

    if(hot||cold)
    {
        cout << "에어컨 작동" << endl;
        if(hot)
        {
            cout << "냉방 작동" << endl;
        }
        else
        {
            cout << "난방 작동" << endl;
        }
    }
    else{
        cout << "에어컨 작동 종료" << endl;
    }
    return 0;
}