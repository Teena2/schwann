#include <iostream>
#include <string>


using namespace std;
 

int main()
{
 int HammingDistance = 0;
 string Name = "Amira Tounsi";
 string email = "amira.tounsi@insat.u-carthage.tn";
 string slackusername = "@AmiraT";
 string biostack = "Data science";
 string Twitterhandle = "@Tmiran";
 cout<<Name<<"\n";
 cout<<email<<"\n";
 cout<<slackusername<<"\n";
 cout<<biostack<<"\n";
 cout<<Twitterhandle<<"\n";

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
cout<<HammingDistance<<"\n"<<endl;

    return 0;
}
