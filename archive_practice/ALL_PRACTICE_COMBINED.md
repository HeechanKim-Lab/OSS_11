# 📦 학기 중 개인 실습 파일 통합 보관본 (`archive_practice`)

최상위 경로에 흩어져 있던 C++, Python, Jupyter Notebook(`.ipynb`), 텍스트 실습 파일들을 한곳에 모아 보관한 통합 문서입니다.

## 📋 수록 파일 목록

1. [`'25.03.13. 사다리꼴, 원, 원기둥.txt`](./'25.03.13. 사다리꼴, 원, 원기둥.txt)
2. [`**.py`](./**.py)
3. [`0313-1.cpp`](./0313-1.cpp)
4. [`airconditioner.cpp`](./airconditioner.cpp)
5. [`app.py`](./app.py)
6. [`bank.cpp`](./bank.cpp)
7. [`cla1.cpp`](./cla1.cpp)
8. [`clf1.cpp`](./clf1.cpp)
9. [`clf2.cpp`](./clf2.cpp)
10. [`daily_shitpost.sh`](./daily_shitpost.sh)
11. [`feed_the_grass.sh`](./feed_the_grass.sh)
12. [`ifelse1.cpp`](./ifelse1.cpp)
13. [`ifelse2.cpp`](./ifelse2.cpp)
14. [`iffdcd.cpp`](./iffdcd.cpp)
15. [`ifintro.cpp`](./ifintro.cpp)
16. [`main.cpp`](./main.cpp)
17. [`multipleFor.cpp`](./multipleFor.cpp)
18. [`multiplesOf3,5.cpp`](./multiplesOf3,5.cpp)
19. [`overld.cpp`](./overld.cpp)
20. [`penny.cpp`](./penny.cpp)
21. [`pmassign.cpp`](./pmassign.cpp)
22. [`setup_daily_streak.sh`](./setup_daily_streak.sh)
23. [`shitpost_generator.py`](./shitpost_generator.py)
24. [`typeid.cpp`](./typeid.cpp)
25. [`공학용_계산기_만들기.ipynb`](./공학용_계산기_만들기.ipynb)
26. [`자살률_구하기.ipynb`](./자살률_구하기.ipynb)

---

## 📄 `'25.03.13. 사다리꼴, 원, 원기둥.txt`

```txt

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
```

---

## 📄 `**.py`

```py
"""Star pattern generator module."""
# pylint: disable=invalid-name
a = int(input())

for i in range(a):
    for j in range(a-(i+1)):
        print(' ', end='')

    for k in range(1 + 2*(i)):
        print('*', end='')
    print()

```

---

## 📄 `0313-1.cpp`

```cpp

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
```

---

## 📄 `airconditioner.cpp`

```cpp

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
```

---

## 📄 `app.py`

```py
"""Streamlit app module."""
# pylint: disable=import-error
import streamlit as st

st.title("환영합니다!")

st.video("https://www.youtube.com/watch?v=J9VG-j9okmk")

```

---

## 📄 `bank.cpp`

```cpp
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
```

---

## 📄 `cla1.cpp`

```cpp
#include <iostream>
using namespace std;

class Circle
{
    private:
        double Radious;

    public:
    double getRadious() const;
    double getArea() const;
    double getPerimeter() const;
    void setRadious(double value);
};

double Circle::getRadious() const
{
    return Radious;
}

double Circle::getArea() const
{
    const double PI = 3.141592;
    return (Radious * Radious * PI);
}

double Circle::getPerimeter() const
{
    const double PI = 3.141592;
    return (2.0 * PI * Radious);
}

void Circle::setRadious(double value)
{
    Radious = value;
}

int main()
{

    cout << "Circle1: " << endl;
    Circle circle1;
    circle1.setRadious(10.0);
    cout << "Radious: " << circle1.getRadious() << endl;
    cout << "Area: " << circle1.getArea() << endl;
    cout << "Perimeter: " << circle1.getPerimeter() << endl;

    cout << "Circle2: " << endl;
    Circle circle2;
    circle2.setRadious(20.0);
    cout << "Radious: " << circle2.getRadious() << endl;
    cout << "Area: " << circle2.getArea() << endl;
    cout << "Perimeter: " << circle2.getPerimeter() << endl;

    return 0;
}
```

---

## 📄 `clf1.cpp`

```cpp
#include <iostream>
using namespace std;

class Circle
{
    private:
        double radius;
    
    public:
        Circle(double radious);
        Circle();
        ~Circle();
        Circle(const Circle& circle);
        void setRadious(double radious);
        double getRadious() const;
        double getArea() const;
        double getPerimeter() const;
};

Circle::Circle(double rds)
: radius(rds)
{
    cout << "매개변수가 있는 생성자가 호출되었습니다. " << endl;
}

Circle::Circle()
: radius(0.0)
{
    cout << "기본 생성자가 호출되었습니다. " << endl;
}

Circle::Circle(const Circle& c)
: radius(c.radius)
{
    cout << "복사 생성자가 호출되었습니다. " << endl;
}

Circle::~Circle()
{
    cout << "소멸자가 호출되었습니다: " << radius << endl;
}

void Circle::setRadious(double value)
{
    radius = value;
}

double Circle::getRadious() const
{
    return radius;
}

double Circle::getArea() const
{
    const double PI = 3.141592;
    return (PI * radius * radius);
}

double Circle::getPerimeter() const
{
    const double PI = 3.141592;
    return (2 * PI * radius);
}

int main()
{
    Circle circle1(5.2);
    cout << "Radius: " << circle1.getRadious() << endl;
    cout << "Area: " << circle1.getArea() << endl;
    cout << "Perimeter: " << circle1.getPerimeter() << endl;

    Circle circle2(circle1);
    cout << "Radius: " << circle2.getRadious() << endl;
    cout << "Area: " << circle2.getArea() << endl;
    cout << "Perimeter: " << circle2.getPerimeter() << endl;

    Circle circle3;
    circle3.setRadious(3.5);
    cout << "Radius: " << circle3.getRadious() << endl;
    cout << "Area: " << circle3.getArea() << endl;
    cout << "Perimeter: " << circle3.getPerimeter() << endl;

    return 0;
}
```

---

## 📄 `clf2.cpp`

```cpp

```

---

## 📄 `daily_shitpost.sh`

```sh
#!/usr/bin/env bash
# ==============================================================================
# ULTIMATE LOW-EFFORT BRAINROT COMMIT STREAK AUTOMATION
# Purpose: Keep the GitHub contribution grass green at negative brain cost.
# ==============================================================================

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

# List of uncivilized, brain-dead log entries
ENTRIES=(
  "Status: Braincell count zero. Action: Dropped a pebble into the void."
  "Unga bunga me push code me see green square me happy."
  "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
  "Grass status: VERIFIED GREEN. Sanity status: 404 NOT FOUND."
  "Roses are red, violets are blue, this commit is worthless, and so are you."
  "Skibidi toilet sigma ohio rizzler commit #99999."
  "Git push --force-my-will-to-live-into-this-useless-repository."
  "I forgor 💀"
  "Another day, another pixel of dopamine on GitHub profile."
  "Beep boop me robotic primate hitting keys randomly: $(cat /dev/urandom | LC_ALL=C tr -dc 'a-zA-Z0-9' | head -c 16)"
  "Why are we still here? Just to suffer? And to commit?"
  "The grass must grow. Blood for the Blood God, commits for the Green Graph."
  "Nothing changed. Absolutely nothing. Perfectly balanced trash."
  "Commit message not found. Brain stopped responding. Press any key to continue."
)

# Pick random entry
RANDOM_INDEX=$(( RANDOM % ${#ENTRIES[@]} ))
RANDOM_ENTRY="${ENTRIES[$RANDOM_INDEX]}"
TODAY=$(date "+%Y-%m-%d %H:%M:%S")

# Append to daily_brainrot.txt
cat <<EOF >> "$REPO_DIR/daily_brainrot.txt"

[$TODAY]
$RANDOM_ENTRY
EOF

# Ensure git is on main and up to date
git checkout main
git pull --rebase origin main

# Commit and push
COMMIT_MESSAGES=(
  "chore(brainrot): unga bunga daily grass ritual"
  "shitpost: touching grass virtually"
  "feat(grass): greenification ceremony"
  "docs: updated the sacred scroll of garbage"
  "chore: 0iq play to keep the streak alive"
  "fix(brain): memory leak in skull"
  "refactor: moved air molecules around"
)
RANDOM_MSG_INDEX=$(( RANDOM % ${#COMMIT_MESSAGES[@]} ))
COMMIT_MSG="${COMMIT_MESSAGES[$RANDOM_MSG_INDEX]}"

git add "$REPO_DIR/daily_brainrot.txt"
git commit -m "$COMMIT_MSG"
git push origin main

echo "[$TODAY] Successfully committed and pushed brainrot to origin/main! Grass is green."

```

---

## 📄 `feed_the_grass.sh`

```sh
#!/usr/bin/env bash
# ==============================================================================
#  THE SACRED BRAINROT GRASS SUSTENANCE PROTOCOL
#  Keeps the GitHub contribution graph violently green with zero mental effort.
# ==============================================================================

set -euo pipefail

export PATH="/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/Library/Frameworks/Python.framework/Versions/3.13/bin:/usr/bin:/bin:/usr/sbin:/sbin:$PATH"

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
cd "$REPO_DIR"

# Ensure git author is HeechanKim-Lab so the commit is credited to the grass graph
git config user.name "HeechanKim-Lab"
git config user.email "2218160@donga.ac.kr"

# Make sure we're on main and cleanly rebased
git checkout -q main 2>/dev/null || true
git pull --rebase -q origin main 2>/dev/null || true

# Run the python brainrot generator to append uncivilized nonsense
python3 "$REPO_DIR/shitpost_generator.py"

COMMIT_FILE="$REPO_DIR/.git_commit_msg.txt"

# Stage the sacred shitpost ledger files
git add "$REPO_DIR/SHITPOST.md" "$REPO_DIR/daily_brainrot.txt" "$REPO_DIR/.gitignore"

# Commit and push
if [ -f "$COMMIT_FILE" ]; then
  git commit -F "$COMMIT_FILE"
  rm -f "$COMMIT_FILE"
else
  git commit -m "feat(grass): uncivilized automated photosynthesis ritual 🌿"
fi

git push origin main

echo ">>> [SUCCESS] Grass fed with top-tier brainrot! Contribution graph secured."

```

---

## 📄 `ifelse1.cpp`

```cpp
/*
#include <iostream>
using namespace std;

int main()
{

    int score;

    cout << "0~100사이의 점수 입력: ";
    cin >> score;

    if(score >= 70)
    {
        cout << "PASS" << endl;
    }
    else
    {
        cout << "FAIL" << endl;
    }
    return 0;
}
    */
```

---

## 📄 `ifelse2.cpp`

```cpp

#include <iostream>
using namespace std;

int main()
{

    int score;
    char grade;

    cout << "0~100점 사이의 점수 입력: ";
    cin >> score;

    if(score >= 90)
    {
        grade = 'A';
    }
    else if(score >= 80)
    {
        grade = 'B';
    }
    else if(score >= 70)
    {
        grade = 'C';
    }
    else if(score >= 60)
    {
        grade = 'D';
    }
    else
    {
        grade = 'F';
    }

    cout << "최종학점 = " << grade << endl;
    
    return 0;
}
```

---

## 📄 `iffdcd.cpp`

```cpp

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
```

---

## 📄 `ifintro.cpp`

```cpp
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
```

---

## 📄 `main.cpp`

```cpp
#include <iostream>

int main() {
    std::cout << "Hello World!" << std::endl;
    std::cout << "Hiii" << std::endl;
    std::cout << "안녕" << std::endl;
    std::cout << "grass" << std::endl;
    return 0;
}


```

---

## 📄 `multipleFor.cpp`

```cpp

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

    int count = 0;
    for ( int i = 1; i <= number; i++)
    {
        if ( i % 3 == 0 || i % 5 == 0)
        {
            cout << i << endl;
            count++;
        }
    }

    cout << "---------------" << endl;
    cout << "총 " << count << " 개입니다." << endl;
}
```

---

## 📄 `multiplesOf3,5.cpp`

```cpp

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
```

---

## 📄 `overld.cpp`

```cpp

```

---

## 📄 `penny.cpp`

```cpp
/*동전과 지폐들의 금액 합계를 구하는 프로그램*/

#include <iostream>
using namespace std;

int main()
{

    const unsigned int pennyValue = 1;
    const unsigned int nickelValue = 5;
    const unsigned int dimeValue = 10;
    const unsigned int quarterValue = 25;
    const unsigned int dollarValue = 100;

    unsigned int pennies;
    unsigned int nickels;
    unsigned int dimes;
    unsigned int quarters;
    unsigned int dollars;

    unsigned long int totalValue;

    cout << "페니의 수: ";
    cin >> pennies;
    cout << "니켈의 수: ";
    cin >> nickels;
    cout << "다임의 수: ";
    cin >> dimes;
    cout << "쿼터의 수: ";
    cin >> quarters;
    cout << "달러의 수: ";
    cin >> dollars;

    totalValue = pennies * pennyValue + nickels * nickelValue
    + dimes * dimeValue + quarters * quarterValue + dollars * dollarValue;

    cout << "전체 값은" << totalValue << "페니입니다.";
    return 0;

}
```

---

## 📄 `pmassign.cpp`

```cpp
/* 각종 연산자와 할당, 복합할당 

#include <iostream>
using namespace std;

int main()
{
    int a = 10;
    int b = 20;
    int x = 2;

    x += 4;

    cout << "a + b: " << a + b << endl;
    cout << "-a: " << -a << endl;
    cout << "a * b: " << a * b << endl;
    cout << "x += 4: " << x << endl;

    b /= 10;
    cout << b;

    return 0;

}*/
```

---

## 📄 `setup_daily_streak.sh`

```sh
#!/usr/bin/env bash
# ==============================================================================
#  DAILY GRASS SUSTENANCE - LOCAL LAUNCHD INSTALLER
#  Installs a macOS LaunchAgent to automatically run feed_the_grass.sh every day
# ==============================================================================

set -euo pipefail

REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PLIST_LABEL="com.heechan.dailygrass"
PLIST_PATH="$HOME/Library/LaunchAgents/${PLIST_LABEL}.plist"
LOG_DIR="$REPO_DIR/reports"
mkdir -p "$LOG_DIR"

echo "=== 🌿 GitHub Contribution Grass Sustenance Installer ==="
echo "Repo path: $REPO_DIR"

cat <<EOF > "$PLIST_PATH"
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>Label</key>
    <string>${PLIST_LABEL}</string>
    <key>ProgramArguments</key>
    <array>
        <string>/bin/bash</string>
        <string>${REPO_DIR}/feed_the_grass.sh</string>
    </array>
    <key>StartCalendarInterval</key>
    <dict>
        <key>Hour</key>
        <integer>9</integer>
        <key>Minute</key>
        <integer>15</integer>
    </dict>
    <key>EnvironmentVariables</key>
    <dict>
        <key>PATH</key>
        <string>/opt/homebrew/bin:/opt/homebrew/sbin:/usr/local/bin:/Library/Frameworks/Python.framework/Versions/3.13/bin:/usr/bin:/bin:/usr/sbin:/sbin</string>
    </dict>
    <key>StandardOutPath</key>
    <string>${LOG_DIR}/launchd_grass.log</string>
    <key>StandardErrorPath</key>
    <string>${LOG_DIR}/launchd_grass.err</string>
    <key>RunAtLoad</key>
    <false/>
</dict>
</plist>
EOF

chmod 644 "$PLIST_PATH"

# Unload previous if exists, then load
launchctl unload "$PLIST_PATH" 2>/dev/null || true
launchctl load "$PLIST_PATH"

echo ">>> [SUCCESS] LaunchAgent installed and loaded at $PLIST_PATH"
echo ">>> It will automatically execute feed_the_grass.sh every day at 09:15 local time!"
echo ">>> To test run manually anytime: ./feed_the_grass.sh"
echo ">>> To uninstall: launchctl unload $PLIST_PATH && rm $PLIST_PATH"

```

---

## 📄 `shitpost_generator.py`

```py
#!/usr/bin/env python3
# pylint: skip-file
"""
shitpost_generator.py
Generates the most brain-dead, uncivilized, and low-effort entries imaginable
to keep the GitHub grass green.
"""

import datetime
import random
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LEDGER_PATH = os.path.join(BASE_DIR, "SHITPOST.md")
BRAINROT_PATH = os.path.join(BASE_DIR, "daily_brainrot.txt")
COMMIT_MSG_PATH = os.path.join(BASE_DIR, ".git_commit_msg.txt")

ASCII_GRAVEYARD = [
    r"""
     (\__/)
     (•ㅅ•)  me touching virtual grass
    / 　 づ  so i never touch real grass
    """,
    r"""
       \  /
      .-""-.
    /  _  _  \   [BRAIN CELL NOT FOUND]
    | (o)(o) |   
    |   /\   |   OOG BOOG ME PUSH CODE
    \  =--=  /
     '-....-'
    """,
    r"""
    (╯°□°)╯︵ ┻━┻  (why write clean code when you can write trash)
    """,
    r"""
       /\_/\
      ( o.o )  <-- cat observing this dumpster fire
       > ^ <
    """,
    r"""
       [ 0% BRAIN USAGE DETECTED ]
       ===========================
         ( \ / )
         ( . .)   photosynthesis in progress...
         c(")(")
    """,
    r"""
         _________
        /         \
       /   REST    \
      /     IN      \
     /    PEACE      \
    |   CLEAN CODE    |
    |   2026 - 2026   |
    |                 |
    |_________________|
    """,
    r"""
    ( ͡° ͜ʖ ͡°)  another day, another green tile stolen from github
    """,
    r"""
       ▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
       █  SKIBIDI GIT  █
       █   GRASS FEED  █
       ▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
              ||
           (  ಠ_ಠ )
    """,
    r"""
        (  .      )
       )           (     [ DUMPSTER FIRE ]
      (    (  .     )    status: burning nicely
       )     )    (      efficiency: 100%
     [===============]
     |   GARBAGE     |
     |   PIPELINE    |
     [===============]
    """,
    r"""
          ___
         /   \
        |  o  |  <-- a potato has more cognitive function
         \___/       than this git commit
    """,
    r"""
        [RETURN TO MONKE]
             __
        .-"''  ''"-.
       /            \
      |  (o)    (o)  |   🍌 BANANA CONSUMED
      |      /\      |   🟩 TILE GREENIFIED
       \    ====    /    💤 ME GO SLEEP
        '-..____..-'
    """,
    r"""
       .----------------.
      |  404 SANITY     |
      |  NOT FOUND      |
      |  COMMIT PUSHED  |
      '----------------'
             ||
         \(^Д^)/
    """,
    r"""
         \   /
          .-.
        ― ( ) ―   [QUANTUM PHOTOSYNTHESIS]
          `-’     Absorbing photons into GitHub commit squares...
         /   \
    """,
    r"""
       >(')____,  <-- duck possessing higher cognitive capacity
         (` =~~/      than this repository's entire architecture
      ~^~^`---'~^~^
    """,
    r"""
        [ MUNICIPAL TRASH RECEPTACLE ]
           ___________
          |  __   __  |   STATUS: OVERFLOWING
          | |  | |  | |   VIBES: IMMACULATE
          | |__| |__| |   STREAK: UNBROKEN
          |___________|
    """,
    r"""
          ( ˶•_•˶)  me committing absolute nonsense
          / >🟩     here have a green square
    """
]

PHILOSOPHICAL_TRASH = [
    "If a commit is pushed to an empty forest and nobody reviews it, does it still turn the GitHub tile green? Yes. Yes it does.",
    "Why write 1000 lines of functional architecture when a single whitespace commit achieves the exact same green pixel?",
    "Today's intellectual epiphany: C++ stands for 'Crying ++'.",
    "Current status: 99.8% water, 0.2% caffeine, 100% uncivilized git streak addict.",
    "Real programmers optimize time complexity O(1). Legendary programmers optimize grass greenness O(daily).",
    "I hit the keyboard with a rock. Git accepted the patch. The CI pipeline approved. Society continues to crumble.",
    "Virtual grass touched. Sunlight avoided. Vitamin D deficiency secured.",
    "Doctors recommend 30 minutes of outdoor activity. I recommend 1 brain-dead push to main.",
    "Scientists confirm: pushing absolute garbage to GitHub stimulates the same dopamine receptors as finding clean water in prehistoric times.",
    "The repo is trash. The code is trash. But the streak? Immaculate.",
    "My code doesn't have bugs; it has surprise unplanned features with emotional issues.",
    "Today I breathed air, drank lukewarm water, and fed the green monster on my GitHub profile. Productive day.",
    "Archaeologists in the year 3050 will dig up this git log and classify our civilization as deeply confused.",
    "Caveman rule #1: Rock hard. Fire hot. Commit green.",
    "Commiting from the void. The void whispered back: 'Nice streak, bro'.",
    "I don't need a 401(k), I need a green GitHub contribution graph.",
    "CSS center a div? Impossible. Push trash to GitHub? Effortless.",
    "My code compiles because the compiler took pity on me.",
    "Eating crayons is a valid debugging strategy if you believe hard enough.",
    "Git blamed myself and honestly, git was right.",
    "DORA metrics status: Lead Time 0.001s, Deployment Frequency infinity, Change Failure Rate undefined (never had tests anyway).",
    "Why touch grass outside when grass inside screen never gives seasonal allergies?",
    "A smooth brain has no wrinkles, meaning zero friction for incoming thoughts.",
    "Keyboard goes clack, server goes ping, tile turns green, ape is king.",
    "I asked ChatGPT for code, it refused on moral grounds, so here we are.",
    "My git commit history looks like an EKG of an over-caffeinated raccoon.",
    "You call it technical debt. I call it an emotional inheritance.",
    "Some people write unit tests. I write git commit messages to ward off evil spirits.",
    "Senior engineer: 'What design pattern did you use?' Me: 'The panic-and-push pattern.'",
    "If you can't handle me at my `git push --force`, you don't deserve me at my green tile streak."
]

CAVEMAN_GRUNTS = [
    "OOG BOOG GRASS GREEN ME HAPPY",
    "UGGA CHUGGA GIT PUSH BRRRRRRR",
    "BONK KEYBOARD WITH SHARP STICK",
    "ME HUNGRY FOR GREEN SQUARE",
    "CLACK CLACK ENTER PUSH DONE ZZZZ",
    "BRAIN OFF. FINGERS FAST. TILE GREEN.",
    "OOF OOF AAH AAH MONKE CODE LEVEL ACHIEVED",
    "MONKE PRESS BUTTON MONKE GET DOPAMINE 🍌",
    "BRAIN SO SMOOTH IT REFLECTS SUNLIGHT ☀️",
    "UNGA BUNGA MERGE CONFLICT EAT ROCKS 🪨",
    "HIT LAPTOP SCREEN WITH HEAVY STONE ME FIX MERGE CONFLICT 🪨💻",
    "ME NO UNDERSTAND LINUS TORVALDS BUT ME PRESS PUSH 🌳",
    "HEAD EMPTY. NO THOUGHTS. ONLY GREEN PIXELS.",
    "ERROR 418: I AM A TEAPOT FILLED WITH PURE TRASH.",
    "BRAIN PROTOCOL DISENGAGED. COMMENCE KEYBOARD SLAPPING."
]

COMMIT_MESSAGES = [
    "chore(grass): photosynthesis goes brrrr 🌿",
    "brainrot: unga bunga daily grass feeding 🦧",
    "fix(sanity): deleted 3 brain cells for optimal performance",
    "feat(vegetation): watered github tile with pure tears 🌿",
    "shitpost: low effort high yield green square guaranteed",
    "caveman: me hit keyboard rock rock clack green 🪨🌿",
    "refactor: rearranged dust particles in the repo",
    "style: added uncivilized spiritual aura to the codebase",
    "perf: optimized grass growth by yelling at git",
    "docs: updated manifesto on why this repo is peak engineering",
    "feat: photosynthesizing at 420 gigahertz",
    "chore: feeding the green square void",
    "brainrot: skibidi commit toilet algorithm v2.0",
    "ugga: oog oog commit pushed grass green me sleep",
    "fix: resolved bug where grass was insufficiently vibrant",
    "feat: aggressively staring at git log until commits appear",
    "chore: virtual grass touched, real grass safely avoided",
    "refactor: converted oxygen into pure git garbage",
    "feat: certified trash-tier contribution",
    "ci: automated brain-death protocol executed successfully",
    "feat(monke): smashed coconut against keyboard, git approved 🥥🌿",
    "chore(brainrot): 0iq quantum photosynthesis ritual initiated 🌿",
    "fix(entropy): added more chaos to an already ruined repository 📉",
    "refactor(void): screamed into the terminal until commit appeared 🗣️",
    "docs(crayons): delicious debugging nutrition acquired 🖍️",
    "feat(dopamine): hijacked github algorithm with absolute zero effort 🧠",
    "chore(potato): transferred life savings into green tile pixels 🥔",
    "fix(reality): git commit -m 'it is what it is' --force-sanity",
    "refactor(dora): elite tier deployment frequency achieved via pure garbage 📊",
    "feat(microtom): injected memes into rhizosphere amplicon pipeline 🧬",
    "chore(grass): touched keyboard instead of touching grass 🌱",
    "perf(brain): smooth brain aerodynamic efficiency +100% 🦧",
    "style(chaos): beautified dumpster fire with indentation 🗑️🔥",
    "feat(matrix): broke out of simulation to push 1 byte to git 🕶️",
    "docs(monke): return to monke protocol step 42: push to main 🍌",
    "chore(streak): sacrificial offering to the almighty contribution graph ⛩️",
    "feat(quantum): commit observed, wavefunction collapsed into green pixel ⚛️",
    "chore(brainrot): sacrificed sanity to appease the green square gods 🧎‍♂️🟩",
    "feat(chaos): introduced non-deterministic vibes into main branch 🎲",
    "fix(logic): removed all logic to prevent further logical fallacies 🧠🚫",
    "refactor(garbage): upgraded dumpster fire to municipal landfill status 🚜🔥",
    "docs(truth): admitted in writing that I have no idea what I'm doing 📜",
    "chore(grass): cyber-botany ritual executed at minimum cognitive altitude 🌱",
    "feat(banana): converted 1 ripe banana into 1 green GitHub pixel 🍌",
    "style(dumpster): added festive fairy lights to the trash heap 🎄🗑️"
]


def generate_entry():
    now = datetime.datetime.now()
    timestamp_str = now.strftime("%Y-%m-%d %H:%M:%S")
    
    ascii_art = random.choice(ASCII_GRAVEYARD).strip("\n")
    quote = random.choice(PHILOSOPHICAL_TRASH)
    grunt = random.choice(CAVEMAN_GRUNTS)
    brain_cells_left = random.randint(-150, 2)
    photosynthesis_rate = random.randint(9000, 99999)
    green_index = f"#{random.randint(10, 50):02x}{random.randint(180, 255):02x}{random.randint(10, 50):02x}"

    entry = f"""
### 🌿 Grass Feeding Session - {timestamp_str}

> **Caveman Verdict:** `{grunt}`  
> **Remaining Brain Cells:** `{brain_cells_left}` | **Photosynthesis Output:** `{photosynthesis_rate} lumens` | **Tile Color:** `{green_index}`

```text
{ascii_art}
```

**Deep Thoughts From The Dumpster:**
> *"{quote}"*

---
"""
    return entry, grunt, quote, brain_cells_left

def update_shitpost_ledger(entry):
    if not os.path.exists(LEDGER_PATH):
        header = """# 🌿 The Sacred Brainrot Grass Ledger

Welcome to the bottom of the software engineering barrel.
This document exists for exactly one holy purpose: **to keep Heechan's GitHub grass aggressively green with the lowest effort humanly possible.**

No architectural reviews. No unit tests. No civilization. Only green tiles.

---
"""
        with open(LEDGER_PATH, "w", encoding="utf-8") as f:
            f.write(header)

    with open(LEDGER_PATH, "a", encoding="utf-8") as f:
        f.write(entry)

def update_daily_brainrot_txt(commit_msg, brain_cells):
    now = datetime.datetime.now()
    today_str = now.strftime("%Y-%m-%d")
    
    statuses = [
        "Potato cognitive baseline achieved, rocks eaten",
        "Primate keyboard assault completed",
        "Monke hit keyboard with coconut 🥥",
        "0 IQ quantum photosynthesis ritual initiated",
        "Violently headbutting enter key to photosynthesize grass pixels",
        "Absolute zero / quantum brain death",
        "Dopamine receptor stimulated by green square"
    ]
    status = random.choice(statuses)

    entry = f"""
[{today_str}]
- Effort: Sub-zero negative cognitive density
- Status: {status}
- Brain cells remaining: {brain_cells}
- Message: {commit_msg}
"""
    with open(BRAINROT_PATH, "a", encoding="utf-8") as f:
        f.write(entry)

def write_commit_message(msg):
    now = datetime.datetime.now()
    body = f"Timestamp: {now.strftime('%Y-%m-%d %H:%M:%S')} | Powered by Uncivilized Automation"
    with open(COMMIT_MSG_PATH, "w", encoding="utf-8") as f:
        f.write(f"{msg}\n\n{body}\n")

def main():
    entry, grunt, quote, brain_cells = generate_entry()
    chosen_msg = random.choice(COMMIT_MESSAGES)
    
    update_shitpost_ledger(entry)
    update_daily_brainrot_txt(chosen_msg, brain_cells)
    write_commit_message(chosen_msg)

    print(f"[SUCCESS] Generated uncivilized shitpost entry.")
    print(f"  - Message: {chosen_msg}")
    print(f"  - Ledger updated: {LEDGER_PATH}")
    print(f"  - Ledger updated: {BRAINROT_PATH}")
    print(f"  - Commit msg cached: {COMMIT_MSG_PATH}")

if __name__ == "__main__":
    main()

```

---

## 📄 `typeid.cpp`

```cpp
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
```

---

## 📄 `공학용_계산기_만들기.ipynb`

```json
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPLAOED5y5YmtY5uY0bQzEZ",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Heechan-Kim-2869/OSS_11/blob/main/%EA%B3%B5%ED%95%99%EC%9A%A9_%EA%B3%84%EC%82%B0%EA%B8%B0_%EB%A7%8C%EB%93%A4%EA%B8%B0.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "NDsum-mzC0hY"
      },
      "outputs": [],
      "source": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "#공학용 계산기 개발의 필요성\n",
        "본 프로젣트는 많은 학생들이 **공학용 계산기**를 구매해야하는 문제를 해결하기 위해 만들었습니다. 예를 들면, $a^6$ 을 개발하는게 어렵습니다."
      ],
      "metadata": {
        "id": "UgC4qum3C_Zm"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 초기값 입력\n",
        "계싼을 원하는 값을 설정해주세요."
      ],
      "metadata": {
        "id": "s61Xaas0I8sB"
      }
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "1EOJjIUsJDuB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# @title Example form fields\n",
        "# @markdown Forms support many types of fields.\n",
        "\n",
        "x = 20 # @param {type: \"number\"}\n",
        "y = 102  # @param {type: \"number\"}\n",
        "date = '2010-11-05'  # @param {type: \"date\"}\n",
        "pick_me = \"monday\"  # @param ['monday', 'tuesday', 'wednesday', 'thursday']\n",
        "select_or_input = \"apples\" # @param [\"apples\", \"bananas\", \"oranges\"] {allow-input: true}\n",
        "# @markdown ---\n"
      ],
      "metadata": {
        "id": "Rk-Q2__zJGUL"
      },
      "execution_count": 4,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## 지수 값 구하기"
      ],
      "metadata": {
        "id": "5BB1Kx40C_9j"
      }
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "sDfZj68pHmy5"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "x = 800\n",
        "\n",
        "x6 = x*x*x*x*x*x\n",
        "\n",
        "if x6 > 2000000:\n",
        "  print(\"너무 큰 수를 입력하셨습니다.\")\n",
        "else:\n",
        "  print(\"안녕\")\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "tnclsNHJGML7",
        "outputId": "53b54c32-ab6c-4e3b-f41b-f470ccbc0ff7"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "너무 큰 수를 입력하셨습니다.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "8mcZsRDaDAUs"
      }
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "fhSJJdVoDBIA"
      }
    }
  ]
}
```

---

## 📄 `자살률_구하기.ipynb`

```json
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "toc_visible": true,
      "authorship_tag": "ABX9TyO/t6T5NwXB2GZEeI5c4zsO",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Heechan-Kim-2869/OSS_11/blob/main/%EC%9E%90%EC%82%B4%EB%A5%A0_%EA%B5%AC%ED%95%98%EA%B8%B0.ipynb\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# 해당 년도의 평균 자살률과 나이대별 평균 자살률 구하기\n",
        "\n",
        "## 데이터 선택\n",
        "데이터는 미국 정부에서 운영하는 오픈 데이터 [사이트](https://data.gov/)를 이용함.\n",
        "\n",
        "데이터 중, 미국에서 일어난 자살을 성별, 인종, 히스패닉 여부, 나이에 따라 정리된 [데이터](https://catalog.data.gov/dataset/death-rates-for-suicide-by-sex-race-hispanic-origin-and-age-united-states-020c1)를 발견하였고, 이 데이터를 이용하여 과제를 수행함.\n",
        "\n",
        "**Death rates for suicide, by sex, race, Hispanic origin, and age: United States**\n",
        "\n",
        "\n",
        "## 데이터 분석\n",
        "\n",
        "Gemini를 이용하여 데이터에서 어떤 분석을 기대할 수 있을지를 의뢰함. 데이터에서 성별과 인종 등의 나이를 제외한 데이터들은 종종 표기되지 않은 경우가 있어, 완벽하게 분석할 수 없다는 사실을 알게됨.\n",
        "\n",
        "## 코드 만들기\n",
        "\n",
        "다음은 생성형 AI를 이용해 연도와 나이대에 따른 자살률을 얻기 위해 입력한 값임.\n",
        "\n",
        "*/content/Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv*\n",
        "\n",
        "*연도를 입력하면 해당 년도의 자살률을 나이대별로 출력하는 코드를 짤거야. 1950~2018 사이의 연도를 입력하게 해줘. 연도를 입력하면 데이터에서 \"ESTIMATE\" column을 조사해서 해당 연도의 평균을 구해줘. 평균치는 반올림한 정수로 나타내줘. 또한 해당 년도의 데이터 중, 나이를 나타내는 데이터가 있다면 따로 수집해서 나이대별로 10살씩 다시 \"ESTIMATE\" column을 평균을 구해서 출력해줘. 이 평균치는 소숫점 한 자릿수의 실수로 출력해줘.*\n",
        "\n",
        "## 코드 실행 후 입력\n",
        "\n",
        "코드 실행 시 데이터세트의 연도의 범위를 설정하기 위해 이를 생성형 AI에게 주문했으며, 실행 시 \"*Please enter a year between 1950 and 2018.*\" 이라는 문구가 출력됨. 이에 원하는 연도를 입력하면 실행됨.\n",
        "\n",
        "## 코드 결과\n",
        "\n",
        "코드의 결과는 해당 연도의 자살률과 나이대별의 자살률의 평균값을 구해서 출력하며, 출력 결과는 다음과 같음.\n",
        "\n",
        "\n",
        "*  예시, '1987'을 입력.\n",
        "\n",
        "  *Enter a year between 1950 and 2018: 1987\n",
        "The average suicide death rate in 1987 is: 16\n",
        "Average death rate for age group All ages: 10.9\n",
        "Average death rate for age group 10-14 years: 1.5\n",
        "Average death rate for age group 15-24 years: 11.0\n",
        "Average death rate for age group 15-19 years: 10.1\n",
        "Average death rate for age group 20-24 years: 14.9\n",
        "Average death rate for age group 25-44 years: 13.6\n",
        "Average death rate for age group 25-34 years: 15.5\n",
        "Average death rate for age group 35-44 years: 15.1\n",
        "Average death rate for age group 45-64 years: 13.7\n",
        "Average death rate for age group 45-54 years: 16.2\n",
        "Average death rate for age group 55-64 years: 17.2\n",
        "Average death rate for age group 65 years and over: 22.3\n",
        "Average death rate for age group 65-74 years: 23.9\n",
        "Average death rate for age group 75-84 years: 34.3\n",
        "Average death rate for age group 85 years and over: 41.7*\n",
        "\n",
        "## 결론\n",
        "\n",
        "코드가 정상적으로 작동하며, 요청한 대로 해당 연도의 자살률은 정수로 나타내며 나이대별 사망률은 소숫점 한자리의 실수로 나타냄."
      ],
      "metadata": {
        "id": "_aI8EJhwPXPI"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# prompt: /content/Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv\n",
        "# 연도를 입력하면 해당 년도의 자살률을 나이대별로 출력하는 코드를 짤거야. 1950~2018 사이의 연도를 입력하게 해줘. 연도를 입력하면 데이터에서 \"ESTIMATE\" column을 조사해서 해당 연도의 평균을 구해줘. 평균치는 반올림한 정수로 나타내줘. 또한 해당 년도의 데이터 중, 나이를 나타내는 데이터가 있다면 따로 수집해서 나이대별로 10살씩 다시 \"ESTIMATE\" column을 평균을 구해서 출력해줘. 이 평균치는 소숫점 한 자릿수의 실수로 출력해줘.\n",
        "\n",
        "import pandas as pd\n",
        "\n",
        "def analyze_suicide_rates(year):\n",
        "    df = pd.read_csv('/content/Death_rates_for_suicide__by_sex__race__Hispanic_origin__and_age__United_States.csv')\n",
        "\n",
        "    if not 1950 <= year <= 2018:\n",
        "        print(\"Please enter a year between 1950 and 2018.\")\n",
        "        return\n",
        "\n",
        "    # Calculate the overall average death rate for the given year\n",
        "    yearly_data = df[df['YEAR'] == year]\n",
        "    average_death_rate = round(yearly_data['ESTIMATE'].mean())\n",
        "    print(f\"The average suicide death rate in {year} is: {average_death_rate}\")\n",
        "\n",
        "    # Analyze age-specific death rates\n",
        "    if 'AGE' in df.columns:  #Check if the 'AGE' column exists\n",
        "        age_groups = yearly_data['AGE'].unique()\n",
        "        for age_group in age_groups:\n",
        "            age_specific_data = yearly_data[yearly_data['AGE'] == age_group]\n",
        "            avg_rate = age_specific_data[\"ESTIMATE\"].mean()\n",
        "            print(f\"Average death rate for age group {age_group}: {avg_rate:.1f}\")\n",
        "    else:\n",
        "        print(\"Age-specific data not available in the dataset.\")\n",
        "\n",
        "# Get user input for the year\n",
        "year_input = int(input(\"Enter a year between 1950 and 2018: \"))\n",
        "analyze_suicide_rates(year_input)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aQWm9eg0UBhS",
        "outputId": "75a0c30b-89bd-4c72-f954-b5df97b8fa0d"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Enter a year between 1950 and 2018: 1987\n",
            "The average suicide death rate in 1987 is: 16\n",
            "Average death rate for age group All ages: 10.9\n",
            "Average death rate for age group 10-14 years: 1.5\n",
            "Average death rate for age group 15-24 years: 11.0\n",
            "Average death rate for age group 15-19 years: 10.1\n",
            "Average death rate for age group 20-24 years: 14.9\n",
            "Average death rate for age group 25-44 years: 13.6\n",
            "Average death rate for age group 25-34 years: 15.5\n",
            "Average death rate for age group 35-44 years: 15.1\n",
            "Average death rate for age group 45-64 years: 13.7\n",
            "Average death rate for age group 45-54 years: 16.2\n",
            "Average death rate for age group 55-64 years: 17.2\n",
            "Average death rate for age group 65 years and over: 22.3\n",
            "Average death rate for age group 65-74 years: 23.9\n",
            "Average death rate for age group 75-84 years: 34.3\n",
            "Average death rate for age group 85 years and over: 41.7\n"
          ]
        }
      ]
    }
  ]
}
```

---

