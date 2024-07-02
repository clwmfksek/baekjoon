#include <bits/stdc++.h>
using namespace std;

int main(){
    ios::sync_with_stdio(0);
    cin.tie(0);
    int a,b;
    cin >> a >> b;
    for(int i=0; i<a;i++){
        int num1;
        cin >> num1;
        if(num1 < b) cout << num1 << " ";
    }
}