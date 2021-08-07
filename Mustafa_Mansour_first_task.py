def intro(name,Email,slack_user_name,twitter_handle,biostack):
    print(name)
    print (Email)
    print(slack_user_name)
    print(twitter_handle)
    print (biostack)
intro ('Mustafa_Mansour','thnatyh295@gmail.com','@Mustafa','@Mustafa67516760','Genomics')


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

print (str(hammingDist(slack_handle, twitter_handle)))
