# include<iostream.h>
# include<conio.h>

int main()
{

int no[5],i,s;
clrscr();
for(i=0;i<5;i++)
{
cout<<"enter a number ";
cin>>no[i];
}
cout<<"enter the number you want to search ";
cin>>s;
for(i = 0; i<5 ;i++)
{
	if(no[i] == s){
		cout<<s<<" is present";
		break;
	}

}
if(i==5)
	cout<<s<<" is not present"<<endl;

getch();
return 0;
}