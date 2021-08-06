<html>  
<head>  
<script type="text/javascript">  
function msg(){  
 alert("Hello Javatpoint");  
}  
</script>  
</head>  
<body>  
<p>Welcome to JavaScript</p>  
<form>  
<input type="button" value="click" onclick="msg()"/> 
</form>
<div id="wrap">
        Slack handle: camiliakamal2
</div>
        
<div id="wrap_mail">   
        e-mail: camiliamhmd@gmail.com
</div>
     
<div id="wrap_slack">
        Biostack: Genomics
</div>
     
<div id="wrap_twitter">    
        Twitter handle: @mkamal_camilia
</div>
    

<script type="text/javascript">
    // JavaScript program to find hamming distance b/w
// two string
 
// function to calculate Hamming distance
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
    document.write(hammingDist (wrap, wrap_twitter));
      
</script>
<script type="text/javascript">  
function msg(){  
 alert("13");  
}  
</script> 
<form>  
<input type="button" value="hamming distance" onclick="msg()"/> 
</form>
</body>  
</html> 