# include <iostream.h>
# include <conio.h>

int main(){
int num;
clrscr();

cout<<"Enter any number between 1 and 7 ";
cin>>num;

switch(num)
{
	case 1:
		cout<<"Today is Monday";
		break;
	case 2:
		cout<<"Today is Tuesday";
		break;
	case 3:
		cout<<"Today is Wednesday";
		break;
	case 4:
		cout<<"Today is Thursday";
		break;
	case 5:
		cout<<"Today is Friday";
		break;
	case 6:
		cout<<"Today is Saturday";
		break;
	case 7:
		cout<<"Today is Sunday";
		break;
	default:
		cout<<"There are only 7 days in a week";
		break;

}
getch();
return 0;

}