var name;
name = "camilia";
var email;
email = "camiliamhmd@gmail.com";
var slack_username;
slack_username = "camiliakamal2"
var biostack; 
biostack = "Genomics";
var twitter_handle;
twitter_handle = "@mkamal_camilia";
 
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
    let wrap = "CamiliaKamal2";
    let wrap_twitter = "@mkamal_camilia";
 
    // function call
    console.log(hammingDist (wrap, wrap_twitter));
