#include <iostream>
using namespace std;
int solution(nums[], target, n){
    for (int i=0; i<n-1; i++){
        for (int j=i; j<n; j++){
            if (nums[i]+nums[j]==target){
                cout<<i<<", "<<j;
            }
        }
    }
}
int main(){
    int n; cin>>n;
    int nums[n];
    for (int i=0; i<n; i++){
        cin>>nums[i];
    }
    int target; cin>>target;
    solution(nums[n], target, n)
}