#include <string>
#include <vector>
#include <iostream>
#include <cstring>
class thisinh
{
public:
    std::string name;
    int game[100];
    int Play;
    bool yet;
    thisinh()
    {
        yet = false;
        getline(std::cin, name);
        memset(game, 0, sizeof game);
    }
    bool operator == (thisinh const &B)
    {
        return this -> name == B.name;
    }
};
