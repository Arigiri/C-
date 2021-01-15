
class Finished
{
public:
    float x, y, z, t;
    Finished(float x, float y, float z, float t)
    {
        this -> x = x, this -> y = y;
        this -> z = z, this -> t = t;
    }
    virtual void ve()
    {
        bar(x, y, z, t);
//        setcolor(BLACK);
        outtextxy((z + x)/2 - 38, (y + t)/2 - 7, "Finish");
    }
    virtual bool isclicked(float X, float Y)
    {
        return (x <= X) && (X <= z) && (y <= Y) && (t >= Y);
    }
};
