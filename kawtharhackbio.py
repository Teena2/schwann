

print( "Kawthar")
print("olatundekawtharolaitan@gmail.com")
print("@kawthar")
print(" Drug development")
print("@Kawthar0002")
Slack_handle='@Kawthar'
def hammingDist(  Slack_handle,  twitter_handle):
    i = 0
    count = 0

    while (i < len(Slack_handle)):
        if (Slack_handle[i] != twitter_handle[i]):
            count += 1
        i += 1
    count = count + ( len(twitter_handle) - len(Slack_handle))
    return count



# Driver code
slack_handle = "@Kawthar"
twitter_handle = "@Kawthar0002"



# function call
print(hammingDist(Slack_handle, twitter_handle))
