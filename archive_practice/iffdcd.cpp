
#include <iostream>
#include <iomanip>
using namespace std;

int main()
{
    double fd, cd;
    int choose;

    cout << "선택하세요 (1:화씨->섭씨, 2:섭씨->화씨) ==> ";
    cin >> choose;

    if( choose == 1)
    {
        cout << "화씨온도 입력: ";
        cin >> fd;
        cd = 5.0 / 9 * (fd - 32);
        cout << fixed << setprecision(5) << "섭씨온도는 " << cd << " 입니다." << endl;
    }
    else if(choose == 2)
    {
        cout << "섭씨온도 입력: ";
        cin >> cd;
        fd = 9.0 / 5 * cd + 32;
        cout << fixed << setprecision(5) << "화씨온도는 " << fd << " 입니다." << endl;
    }
    else
    {
        cout << "1,2 중에 하나를 입력하세요." << endl;
    }

    return 0;
}