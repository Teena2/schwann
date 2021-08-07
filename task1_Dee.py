#Python
"""Personal info"""
name = "Dee"
email = "pwwongaa@gmail.com"
slack_username = "@dee"
bioslack = "genomics"
twitter_handle = "@dee"

print(name,'\n',email,'\n', slack_username,'\n', bioslack,'\n',twitter_handle)
#>>Dee pwwongaa@gmail.com @dee genomics @deee

"""The Hamming Distance """
Hamming_distance = 0
n1 = slack_username
n2 = twitter_handle

if len(n1)>len(n2):
  longer = n1
else:
  longer = n2
 

for i in range(len(longer)):
  if n1[i] != n2[i]:
    Hamming_distance += 1

print(Hamming_distance)
