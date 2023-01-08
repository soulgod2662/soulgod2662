# include <iostream.h>
# include <conio.h>

void swap(int n1,int n2)
{
	int c;
	c=n1;
	n1=n2;
	n2=c;
	cout<<"n1 = "<<n1<<" n2 = "<<n2<<endl;
}
int main()
{
	int n1,n2;
	clrscr();
	cout<<"enter 2 numbers ";
	cin>>n1>>n2;
	swap(n1,n2);
	getch();
	return 0;

}