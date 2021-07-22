#include <iostream>
#include <string>
using namespace std;
class Room{
    public:
        Room(string z){
            setName(z);
        }
        void setName(string x){
            name = x;
        }
        string getName(){
            return name;
        }
    private:
        string name;
};
int main(){
    Room one("Gta V");
    cout << one.getName() << endl;
    Room Two("PUBG Ban ho gaya");
    cout << Two.getName() << endl;
    return 0;   
}

