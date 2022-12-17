# include<iostream.h>
# include<conio.h>

int main(){
int num;
clrscr();
cout<<"Enter 1 for addition";
cout<<"\n Enter 2 for subtration";
cout<<"\n Enter 3 for multiplication";
cout<<"\n Enter 4 for division ";
cin>>num;

switch(num)
{
	case 1:
		int n1,n2;
		int sum1;
		cout<<"Enter 1st number ";
		cin>>n1;
		cout<<"\n Enter 2nd number ";
		cin>>n2;
		sum1 = n1+n2;
		cout<<"The addition is "<<sum1;
		break;
	case 2:
		int s1,s2;
		int sub1;
		cout<<"Enter 1st number ";
		cin>>s1;
		cout<<"Enter 2nd number ";
		cin>>s2;
		sub1 = s1-s2;
		cout<<"The subtraction is "<<sub1;
		break;
	case 3:
		int m1,m2;
		int mul1;
		cout<<"Enter 1st number ";
		cin>>m1;
		cout<<"Enter 2nd number ";
		cin>>m2;
		mul1 = m1*m2;
		cout<<"The multiplication is "<<mul1;
		break;
	case 4:
		int d1,d2;
		int div1;
		cout<<"Enter 1st number ";
		cin>>d1;
		cout<<"Enter 2nd number ";
		cin>>d2;
		div1 = d1/d2;
		cout<<"The division is "<<div1;
		break;



}
getch();
return 0;
}