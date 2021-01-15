#include <Point.hpp>
#include <graphics.h>
//#include <Global.hpp>
void Line(Point a, Point b)
{
    line(a.x, a.y, b.x, b.y);
}
void Bar(Point a, Point b)
{
    bar(a.x, a.y, b.x, b.y);
}
void Cirlce(Point a, float radius)
{
    circle(a.x, a.y, radius);
}
