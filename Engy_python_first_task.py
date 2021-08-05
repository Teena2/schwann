name='Engy'
print('Name:',name)
e_mail='Engyabdelkhalik878@gmail.com'
print('E-mail:',e_mail)
user_name= 'Engy'
print('Slack User name: @',user_name)
biostack = 'Genomics'
print('Biostack:',biostack)
twitter_handle='@Engy14705267'
print('Twitter_handle:',twitter_handle)
Slack_handle='Engy'
def hammingDist(  Slack_handle,  twitter_handle):
    i = 0
    count = 0

    while (i < len(Slack_handle)):
        if (Slack_handle[i] != twitter_handle[i]):
            count += 1
        i += 1
    return count


# Driver code
Slack_handle = "Engy"
twitter_handle= "@Engy14705267"

# function call
print('haming distance=',hammingDist(Slack_handle, twitter_handle))




