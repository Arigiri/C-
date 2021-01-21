#include <Game.hpp>
#include <fstream>
int main()
{
    freopen("GiaiDau.inp","r",stdin);
//    freopen("GiaiDau.out","w",stdout);
    int PlayersPerMatch, NumberOfMatch, SoThiSinh;
//    std:: cin >> PlayersPerMatch >> NumberOfMatch >> SoThiSinh;
//    std::cout << "Enter Player Per Match: ";
    std::cin >> PlayersPerMatch;
//    std::cout <<"Enter Number Of Match: ";
    std::cin >> NumberOfMatch;
//    std::cout <<"Enter Number Of Participant: ";
    std::cin >> SoThiSinh;
    std::cin.ignore();
    Game game(PlayersPerMatch, NumberOfMatch, SoThiSinh);
    game.XepGiaiDau();
    game.Print();

}
