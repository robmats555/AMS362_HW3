#include <iostream>
#include <random>
#include <chrono>
#include <fstream>
  
using namespace std; 

int main() 
{
    unsigned seed = std::chrono::system_clock::now().time_since_epoch().count();
    std::default_random_engine generator (seed);
    std::uniform_real_distribution<double> distribution(0,1.0);

    int counter = 0;
    int lands = 0;
    double u1 = 0;
    while (counter < 1984444444){
        u1 = distribution(generator);
        if (u1 < 3.0/8 || u1 > 5.0/8) {
            lands++;
        }
        if (counter % 10000000 == 0){
            cout << counter << '\n';
        }
        counter++;     
    }

    cout << "The disc intersects: " << lands*100.0/counter << "% of the time";
}