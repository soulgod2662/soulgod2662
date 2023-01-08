# include<iostream.h>
# include<conio.h>

int max(int n1 , int n2)
{
	int ans;
	if (n1>n2){
		return n1;
	}
	else{
		return n2;
	};

}
int max(int n1, int n2, int n3)
{
	int ans;
	if ((n1 > n2) && (n1> n3)){
		return n1;

	}
	if ((n2>n1) && (n2>n3)){
		return n2;
	}
	if ((n3>n2) && (n3>n1)){
		return n3;
	};

}
int main()
{
	int n1, n2 , n3, ans;
	clrscr();
	cout<<"enter two numbers "<<endl;
	cin>>n1>>n2;
	ans = max(n1,n2);
	cout<<ans;
	cout<<"enter three numbers"<<endl;
	cin>>n1>>n2>>n3;
	ans = max(n1,n2,n3);
	cout<<ans;
	getch();
	return 0;


}