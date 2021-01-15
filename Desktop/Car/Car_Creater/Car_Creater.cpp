#include <Car.hpp>
#include <BackGround.hpp>

int main()
{
    initwindow(1910, 1010, "CarCreater");

    BackGround bk = BackGround();
    bk.Ve();
    command c = NONE, tmp;
    Car C;
    float tx = -1, ty = -1, x, y;
    bool ok = false;
    while(1)
    {
        if(ismouseclick(WM_LBUTTONDOWN))
        {
            if(!ok)
            {
                c = bk.getclicked(mousex(), mousey());
                if(c != NONE)tmp = c;
                else if(tx == -1 && ty == - 1)
                    tx = mousex(), ty = mousey(), ok = true;
            }
            clearmouseclick(WM_LBUTTONDOWN);
        }
        if(ismouseclick(WM_MOUSEMOVE))
        {
            if(ok)
            {
                x = mousex(), y = mousey();
                switch (tmp)
                {
                    case BAR: setfillstyle(1, WHITE), bar(tx, ty, x, y);
                    case LINE: setcolor(WHITE),line(tx, ty, x, y);
                }
                std::cout << tx << ' ' << ty << ' ' << x <<' ' << y << '\n';
            }
            clearmouseclick(WM_MOUSEMOVE);
        }
        if(tmp == FINISH)
            break;
        if(ismouseclick(WM_LBUTTONUP) && c == NONE)
        {
            C.addCommand(Point(tx, ty), Point(x, y), tmp);
            ok = false;
            tx = -1, ty = -1;
            clearmouseclick(WM_LBUTTONUP);
        }
    }
    C.Ghi();
//    getch();
    closegraph();
}
