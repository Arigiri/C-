#include <GP.hpp>
#include <Command.hpp>
#include <vector>
#include <fstream>
#include <iostream>
class Car
{
public:
    std::vector <Command> CommandList;
    virtual void addCommand(Point A, Point B, command C)
    {
        Command tmp = Command(A, B, C);
        CommandList.push_back(tmp);
    }
    virtual void Ghi()
    {
        std::ofstream T;
        T.open("Xe1");
        CommandList.erase(CommandList.end());
        for(auto i : CommandList)
        {
            bool ok = true;
            switch(i.C)
            {
                case BAR: std::cout << "BAR " << ' '; break;
                case LINE: std::cout << "LINE " << ' '; break;
                default:ok = false;
            }
            if(ok)std::cout << i.A.x <<' ' << i.A.y<<' '<<i.B.x <<' '<<i.B.y<<std::endl;
        }
    }
};
