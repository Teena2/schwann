#setting variables 
name="Mennatullah Mahmoud"
email="menaturky@gmail.com"
slack_username="@Mennatullah"
biostack="genomics"
twitter_handle="@Mennatallah"


string1=$slack_username
string2=$twitter_handle
hamming_dis=0

 for (( i=0; i<${#string1}; ++i )); do
            if [ ${string1:$i:1} != ${string2:$i:1} ]; then
                let "hamming_dis++"
            fi
        done
echo $name 
echo $email
echo $slack_username
echo $biostack
echo $twitter_handle
echo $hamming_dis 
