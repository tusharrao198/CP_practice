#include <iostream>
#include <string>
using namespace std;

class myClass{
    public:

    private:
        string name;
};

int main()
{
    myClass myThought;
    myThought.name = "Harry";
    cout << myThought.name;
    return 0;
}
