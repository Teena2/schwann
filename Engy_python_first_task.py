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
import hashlib

def hamming_distance(twitter_handle, Slack_handle):
    return sum(c1 != c2 for c1, c2 in zip(Twitter_handle, Slack_handle))

def hamming_distance2(twitter_handle, Slack_handle):
    return len(list(filter(lambda x : ord(x[0])^ord(x[1]), zip(twitter_handle, Slack_handle))))

if __name__=="__main__":
    twitter_handle = hashlib.md5("twitter_handle".encode()).hexdigest()
    Slack_handle = hashlib.md5("Slack_handle".encode()).hexdigest()

    #twitter_handle= '@Engy14705267'
    #Slack_handle= 'Engy'

    assert len(twitter_handle) == len(Slack_handle)

    print('Haming distance =',hamming_distance2(twitter_handle, Slack_handle))



