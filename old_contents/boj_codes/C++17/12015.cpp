// https://www.acmicpc.net/problem/12015
// First Written : 20210706
// Last Modified : 20210711

#include <cstdio>

#define MAXLEN 1000000

int input[MAXLEN+1] = {0};

/* The minumum end value of a subsequence whose length is its idx */
int endval_per_length[MAXLEN+1] = {0};

/* Find the index of the certain value */
int binary_search_idx(int* arr, int left, int right, int val){
    int mid;
    while(left != right){
        mid = (left + right + 1) / 2;
        if(val <= arr[mid]){
            right = mid - 1;
        }
        else{
            left = mid;
        }

    }
    return left;
}

int main(){
    int input_length;
    int max_length = 0;
    int cur_length;

    scanf("%d", &input_length);
    for(int i = 1; i <= input_length; i++){
        scanf("%d", &input[i]);
    }

    for(int idx = 1; idx <=input_length; idx++){
        /* cur length means the maximum legth of subseq that ends with current value */
        cur_length = binary_search_idx(endval_per_length, 0, max_length, input[idx]) + 1;

        /* max length is maximum lengths among cur lengths */
        if(cur_length > max_length){
            max_length = cur_length;
        
        }

        /* update the end value as current value */
        endval_per_length[cur_length] = input[idx];   
    }

    printf("%d\n", max_length);

    return 0;
}