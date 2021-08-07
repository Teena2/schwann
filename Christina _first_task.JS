var name;
name = "Christina";
var email;
email = "christinaashraf792@gmail.com";
var slack_username;
slack_username = "@Christina"
var biostack; 
biostack = "Genomics";
var twitter_handle;
twitter_handle = "@ChristinaAshra9";
 
console.log(name);
console.log(email);
console.log(slack_username);
console.log(biostack);
console.log(twitter_handle);
function hammingDist(wrap, wrap_twitter)
{
    let i = 0, count = 0;
    while (i < wrap.length)
    {
        if (wrap[i] != wrap_twitter[i])
            count++;
        i++;
    }
    return count;
}
 
// driver code
    let wrap = "@Christina";
    let wrap_twitter = "@ChristinaAshra9";
 
    // function call
    console.log(hammingDist (wrap, wrap_twitter));
