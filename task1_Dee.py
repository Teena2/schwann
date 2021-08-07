#Python
"""Personal info"""
name = "Dee"
email = "pwwongaa@gmail.com"
slack_username = "@dee"
biotask = "genomics"

print(name, email, slack_username, biotask)
#>>Dee pwwongaa@gmail.com @dee genomics

"""The Hamming Distance """
Hamming_distance = 0
n1 = input("Please input n1")
n2 = input("Please input n2")

if len(n1)>len(n2):
  longer = n1
else:
  longer = n2
 

for i in range(len(longer)):
  if n1[i] != n2[i]:
    Hamming_distance += 1

print(f"The hamming distance would be: {Hamming_distance}")
