#include <Thisinh.hpp>
#include <algorithm>
#include <chrono>
#include <random>
class Game
{
public:
    int PlayersPerMatch;
    int NumberOfMatch;
    int SoThiSinh;
    int NumberOfMatchEachRound;
    std::vector<thisinh> ListThiSinh;
    std::vector<thisinh> Match[100][100];
    Game(int PlayersPerMatch, int NumberOfMatch, int SoThiSinh)
    {
        this -> PlayersPerMatch = PlayersPerMatch;
        this -> NumberOfMatch = NumberOfMatch;
        this -> SoThiSinh = SoThiSinh;
        this -> NumberOfMatchEachRound = SoThiSinh/PlayersPerMatch;
        for(int i = 1; i <= SoThiSinh; i++)
        {
            thisinh tmp = thisinh();
            this -> ListThiSinh.push_back(tmp);
        }

    }
    virtual bool Find(std::vector<thisinh> S, thisinh A)
    {
        for(auto i : S)if(i == A)return true;
        return false;
    }
    virtual bool check(std::vector<thisinh> ThisMatch,std::vector<thisinh> PreMatch, thisinh A)
    {
        int ThiSinhGapLai = 0;
        for(auto i:PreMatch)
        {
            if(Find(ThisMatch, i))ThiSinhGapLai++;
            if(ThiSinhGapLai > 1)return false;
        }
        return true;
    }
    virtual bool SearchAll(thisinh A, int current_match, std::vector<thisinh>ThisMatch)
    {
//        std::cout << A.name <<' ';
        for(int i = 2; i <= current_match; i++)
            if(!check(ThisMatch,Match[i][A.game[i - 1]],A))
                return false;
        return true;
    }
    virtual void XepGiaiDau()
    {
        for(int match = 1; match <= NumberOfMatch; match++)
        {
            unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
            shuffle(ListThiSinh.begin(), ListThiSinh.end(), std::default_random_engine(seed));
            for(auto &i : ListThiSinh)i.yet = false;
            for(int k = 1; k <= NumberOfMatchEachRound;k++)
            {
                for(int i = 1; i <= PlayersPerMatch; i++)
                {
                    for(auto &j: ListThiSinh)
                    {
                        if(j.yet)continue;
                        if(match == 1 || SearchAll(j, match, Match[match][k]))
                        {
                            Match[match][k].push_back(j);
                            j.game[match] = k;
                            j.yet = true;
                            break;
                        }
                    }
                }
                if(Match[match][k].size() < PlayersPerMatch)
                {
//                    for(auto i : Match[match][k])std::cout << i.name <<' ';
                    Match[match][k].clear();
                    match--;
                    k = NumberOfMatchEachRound + 1;
                }
                if(Match[match][k].size() > PlayersPerMatch)
                {
//                    for(auto i : Match[match][k])std::cout << i.name <<' ';
                    Match[match][k].clear();
                    match--;
                    k = NumberOfMatchEachRound + 1;
                }
            }

        }
    }
    virtual void debug()
    {
        for(int i = 0; i < ListThiSinh.size(); i++)std::cout << ListThiSinh[i].name <<' ';
    }
    virtual void Print()
    {
        for(int match = 1; match <= NumberOfMatch; match++)
        {
            std::cout << "Match " << match << '\n';
            for(int i = 1; i <= NumberOfMatchEachRound; i++)
            {
                std::cout << "   ";
                for(auto j : Match[match][i])std::cout <<j.name <<' ';
                std::cout << std::endl;
            }
        }
    }
};
