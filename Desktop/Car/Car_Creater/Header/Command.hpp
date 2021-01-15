enum command
{
    LINE, BAR, CIRCLE, FINISH, NONE
};
class Command
{
public:
    Point A, B;
    command C;
    Command(Point A, Point B, command C)
    {
        this -> A = A;
        this -> B = B;
        this -> C = C;
    }
};
