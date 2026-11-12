/*3회 거래 후의 계좌 잔액을 구하는 프로그램*/

#include <iostream>
using namespace std;

int main()
{
    int balance = 0;
    int transaction;

    //첫번째 거래
    cout << "첫 번째 거래 금액 입력: ";
    cin >> transaction;
    balance = balance + transaction;

    //두번째 거래
    cout << "두 번째 거래 금액 입력: ";
    cin >> transaction;
    balance = balance + transaction;

    //세번째 거래
    cout << "두 번째 거래 금액 입력: ";
    cin >> transaction;
    balance = balance + transaction;

    //잔액
    cout << "계좌의 최종 잔액은 " << balance << " 달러입니다.";
    return 0;
}