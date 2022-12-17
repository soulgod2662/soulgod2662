# include<iostream.h>
# include<conio.h>

int main(){
int num;
cout<<"\n\n1, India \n2, japan\n3, Italy";
cout<<"\n enter your choice";
cin>>num;

switch(num)
{
    case 1:
	cout<<"I am in India ";
	break;
    case 2:
	cout<<"I am in Japan ";
	break;
    case 3:
	cout<<"I am in Italy ";
	break;
    default:
	cout<<"This choice is not available";
	}
getch();
return 0;

}







