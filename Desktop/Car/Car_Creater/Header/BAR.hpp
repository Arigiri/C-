class B
{
public:
    float poslx, posly, posrx, posry;
    B(float lx, float ly, float rx, float ry)
    {
        poslx = lx, posly = ly, posrx = rx, posry = ry;
    }
    virtual void ve()
    {
        bar(poslx, posly, posrx, posry);
//        setcolor(BLACK);
        outtextxy((poslx + posry)/2 - 21, (posly + posry)/2 - 7, "BAR");
    }
    virtual bool isclicked(float X, float Y)
    {
        return (poslx <= X) && (X <= posrx) && (posly <= Y) && (posry >= Y);
    }
};
