print( "Teena")
print("teena.ra2020@gmail.com")
print("Genomics")
print("@ra_teena")
Slack_handle='@Teena'
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
slack_handle = "@Teena"
twitter_handle = "@ra_teena"



# function call
print(hammingDist(Slack_handle, twitter_handle))
