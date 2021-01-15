#include <BAR.hpp>
#include <Circle.hpp>
#include <Line.hpp>
#include <Finished.hpp>
//#include <GP.hpp>
class BackGround
{
public:
    B b = B(0, 0, 60, 60);
    dt l = dt(90, 0, 150, 60);
    Finished f = Finished(1810, 910,1910, 1010);
    BackGround() {}
    virtual void Ve()
    {
        setbkcolor(WHITE);
        setcolor(BLACK);
        settextstyle(0, 0, 2);
        b.ve();
        l.ve();
        settextstyle(0, 0, 2);
        f.ve();
    }
    virtual command getclicked(float x, float y)
    {
        if(b.isclicked(x, y))return BAR;
        else if(l.isclicked(x, y))return LINE;
        else if(f.isclicked(x, y))return FINISH;
        return NONE;
    }
};
