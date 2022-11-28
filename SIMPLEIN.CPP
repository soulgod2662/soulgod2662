//simple interest = P*T*R/100

# include<iostream.h>
# include<conio.h>

int main(){

int amount;
int period;
float rate;
float finalamt;

clrscr();
cout<<"welcome to simple interest calculator";
cout<<"please enter the principal amount ";
cin>>amount;

cout<<"please enter the period ";
cin>>period;

cout<<"please enter the rate ";
cin>>rate;

finalamt = amount*period*rate/100;
cout<<"the simple interest is "<<finalamt;

cout<<" Also, the final amount after "<<period<<" will be "<<finalamt+amount;

getch();
return 0;


}