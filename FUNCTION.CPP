# include<iostream.h>
# include<conio.h>

int add(int n1,int n2)
{
	int ans;
	ans = n1+n2;
	return ans;

}
int add(int n1,int n2,int n3)
{
	int ans;
	ans = n1+n2+n3;
	return ans;

}
int main()
{
	int n1,n2,n3,ans;
	clrscr();
	cout<<"enter 2 numbers ";
	cin>>n1>>n2;
	ans = add(n1,n2);
	cout<<"Addition = "<<ans<<endl;
	cout<<"enter 3 numbers "<<endl;

	cin>>n1>>n2>>n3;
	ans = add(n1,n2,n3);
	cout<<"Addition = "<<ans<<endl;
	getch();
	return 0;

}