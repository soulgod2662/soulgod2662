# include <iostream.h>
# include <conio.h>

int main()
{
int year;
clrscr();
cout<<"enter a year to find if it is a leap year or not "<<endl;
cin>>year;

if ((year % 4 == 0) && (year % 100 != 0) || (year % 400 == 0)){
	cout<<"it is a leap year"<<endl;
}
else{
	cout<<"it is not a leap year"<<endl;
}


getch();
return 0;

}