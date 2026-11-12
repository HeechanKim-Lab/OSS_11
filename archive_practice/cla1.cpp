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