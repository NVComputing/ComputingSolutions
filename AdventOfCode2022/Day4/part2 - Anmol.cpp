#include <iostream>
#include <string>
using namespace std;

int main()
{
    string x;
    int count = 0;
    int z = 0, d1, d2;
    int num1s, num1e, num2s, num2e;
    while(true){
        cin>>x;
        if(x.compare("end") == 0){
            break;
        }
        for (int i = 0; i<x.length(); i++){
            if(x[i] == ','){
                z = i;
            }else if(x[i] == '-'){
                if(z==0){
                    d1 = i;
                }else{
                    d2 = i;
                }
            }
        }
        num1s = stoi(x.substr(0,d1));
        num1e = stoi(x.substr(d1+1,z-d1-1));
        num2s = stoi(x.substr(z+1,d2-z-1));
        num2e = stoi(x.substr(d2+1,x.length()-d2-1));
        if((num1s<=num2e && num1s>=num2s) ||  (num2s>=num1s && num2s<=num1e)){
            count++;
        }
        z = 0;
    }
    cout<<count;
}
