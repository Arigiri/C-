
class dt
{
public:
    float x, y, z, t;
    dt(float x, float y, float z, float t)
    {
        this -> x = x, this -> y = y;
        this -> z = z, this -> t = t;
    }
    virtual void ve()
    {
        bar(x, y, z, t);
//        setcolor(BLACK);
        outtextxy((z + x)/2 - 27, (y + t)/2 - 7, "LINE");
    }
    virtual bool isclicked(float X, float Y)
    {
        return (x <= X) && (X <= z) && (y <= Y) && (t >= Y);
    }
};
