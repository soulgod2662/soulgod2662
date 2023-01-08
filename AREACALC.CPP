# include<iostream.h>
# include<conio.h>

int circle(int radius)
{
	float ans;
	int pi = 3.14;
	ans = pi*radius*radius;
	return ans;

}
int rectangle(int l1,int b1)
{
	float ans;
	ans = l1*b1;
	return ans;
}
int main()
{
int l1,b1,ans,radius;
clrscr();
cout<<"enter radius of circle"<<endl;
cin>>radius;
ans = circle(radius);
cout<<ans<<endl;
cout<<"enter length and breadth"<<endl;
cin>>l1>>b1;
ans = rectangle(l1,b1);
cout<<ans<<endl;
getch();
return 0;
};