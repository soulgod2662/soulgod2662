# include<iostream.h>
# include<conio.h>

int main()
{
int no[5], i , s = 0;
clrscr();
for(i = 0; i<5 ; i++)
	{
	cout<<"\n ENTER a number ";
	cin>>no[i];

	}

for(i=0; i<5; i++)
	{
	s = s+no[i];
	cout<<i<<" number is "<<no[i]<<" ";
	}
cout<<"sum of the numbers is "<<s;
getch();
return 0;
}