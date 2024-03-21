#include <stdio.h>
#include <string.h>
int stk[10];
int top=-1;
int pop();
void push(int);
int main(){
    char prefix[10];
    int len, val, i, opr1, opr2, res;
    printf("\n Enter the prefix expression: ");
    fgets(prefix,10,stdin);
    len = strlen(prefix);
    for(i=len-2;i>=0;i--){
        switch(get_type(prefix[i])){
            case 0:
                val = prefix[i] - '0';
                printf(" o:%d ", val);
                push(val);
                break;
            case 1:
                opr1 = pop();
                opr2 = pop();
                switch(prefix[i]){
                    case '+':
                        res = opr1 + opr2;
                        break;
                    case '-':
                        res = opr1 - opr2;
                        break;
                    case '*':
                        res = opr1 * opr2;
                        break;
                    case '/':
                        res = opr1 / opr2;
                        break;
                }
                printf(" r:%d ", res);
                push(res);
        }
    }
    printf("\n RESULT = %d", stk[0]);
    getchar();
    return 0;
}
void push(int val){
    stk[++top] = val;
}
int pop(){
    return(stk[top--]);
}
int get_type(int c){
    if(c == '+' || c == '-' || c == '*' || c == '/')
        return 1;
    else return 0;
}