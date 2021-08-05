#include <iostream.h>
#include <string.h>


using namespace std;
 

int main()
{
 int HammingDistance = 0;
 string Name = "Amira Tounsi";
 string email = "amira.tounsi@insat.u-carthage.tn";
 string slackusername = "@AmiraT";
 string biostack = "Data science";
 string Twitterhandle = "@Tmiran";
 cout<<"Name: "<<Name<<"\n";
 cout<<"email: "<<email<<"\n";
 cout<<"Slack user name: "<<slackusername<<"\n";
 cout<<"biostack: "<<biostack<<"\n";
 cout<<"Twitter handle: "<<Twitterhandle<<"\n";

 if (slackusername.length() == Twitterhandle.length())
    {
        for (int i=0; i<slackusername.length(); i++)
        {
            if (slackusername[i] != Twitterhandle[i])
            {
                HammingDistance++;
            }
        }
    } 
else if (slackusername.length() > Twitterhandle.length())
    {

        for (int i=0; i<Twitterhandle.length(); i++)
        {
            if (slackusername[i] != Twitterhandle[i])
            {
                HammingDistance++;
                }
         }
        HammingDistance = HammingDistance + (slackusername.length()-Twitterhandle.length());   
    }
    else
    {
        for (int i=0; i<slackusername.length(); i++)
        {
            if (slackusername[i] != Twitterhandle[i])
            {
                HammingDistance++;
                }
         }
        HammingDistance = HammingDistance + (Twitterhandle.length() - slackusername.length());   
    }
cout<<"Hamming Distance: "<<HammingDistance<<"\n"<<endl;

    return 0;
}
