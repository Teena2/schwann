<?php
// Your code here!
$name ='Ahmed sameh';
$email = "sameh7831@ gmail.com";
$biostack = "genomics";
$twitterhandle = "@ahhmedsamehh";
$slackhandle = "@ahhmedsamehh";

echo $name;
echo "<br>";
echo $email;
echo "<br>";
echo $biostack;
echo "<br>";
echo $twitterhandle ;
echo "<br>";
echo $slackhandle;
echo "<br>";

// Your code here!
// PHP program to find hamming distance b/w
// two string
 
// function to calculate
// Hamming distance
function hammingDist($str1, $str2)
{
    $i = 0; $count = 0;
    while (isset($str1[$i]) != '')
    {
        if ($str1[$i] != $str2[$i])
            $count++;
        $i++;
    }
    return $count;
}
 
    // Driver Code
    $str1 = "@ahhmedsamehh";
    $str2 = "@ahhmedsamehh";
 
    // function call
    echo hammingDist ($str1, $str2);
     
// This code is contributed by nitin mittal.
?>
