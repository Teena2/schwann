def intro(name,Email,slack_user_name,twitter_handel,biostack):
    print('My name is: '+name)
    print ('My E-mail is: '+Email)
    print('My slack user name is: '+slack_user_name)
    print('My twitter user name is: '+ twitter_handel)
    print ('biostack is: '+biostack)
intro ('Mustafa Mansour','thnatyh295@gmail.com','Mustafa','@Mustafa67516760','Genomic')


def hammingDist(slack_handle, twitter_handle):
    i = 0
    count = 0

    while (i < len(slack_handle)):
        if (slack_handle[i] != twitter_handle[i]):
            count += 1
        i += 1
    return count

slack_handle = 'Mustafa'
twitter_handle = '@Mustafa67516760'

print ('hammingDist = '+ str(hammingDist(slack_handle, twitter_handle)))