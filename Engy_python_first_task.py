name='Engy'
print(name)
e_mail='Engyabdelkhalik878@gmail.com'
print(e_mail)
slack_username= 'Engy'
print('@',slack_username)
biostack = 'Genomics'
print(biostack)
twitter_handle='@Engy14705267'
print(twitter_handle)
Slack_handle='Engy'
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
Slack_handle = "@Engy"
twitter_handle= "@Engy14705267"

# function call
print(hammingDist(Slack_handle, twitter_handle))




