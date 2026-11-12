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