
# include<iostream.h>
# include<conio.h>

int main(){


float temperature;
float a1;
float answer;
clrscr();

cout<<"please enter temperature in farnheit ";
cin>>temperature;
a1 = temperature-32;
answer = a1*5/9;
cout<<"temperature in celcius is "<<answer;
getch();
return 0;

}
