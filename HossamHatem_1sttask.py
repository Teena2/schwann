name='Hossam'
print (name)
e_mail='hossamhatim2000@gmail.com'
print (e_mail)
slack_username='@HossamHatem'
print(slack_username)
Biostack='Genomics'
print(Biostack)
twitter_handle='@HossamH67906960'
print (twitter_handle)
# Hamming distance
def hammingDist(slack_handle, twitter_handle):
    i = 0
    count = 0

    while (i < len(slack_handle)):
        if (slack_handle[i] <= twitter_handle[i]):
            count += 1
        i += 1

    return count

# Driver code
twitter_handle = "@HossamH67906960"
slack_handle = "@HossamHatem"

# function call
print(hammingDist(slack_handle, twitter_handle))
