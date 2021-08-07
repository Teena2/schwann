#!/usr/bin/perl

$name ="KJ Nandha Kishore";
$email = "nandhakishorekj97@gmail.com";
$slack_usrname = "\@Nandha";
$bio_stack = "Genomics";
$twit_handle = "\@nandha_kj";

#Here both the strings are not equal for calculating the hamming distance

sub hamDist
	{
	  	$fname = $_[0];
		$sname = $_[1];
		
		if (length($fname) <length($sname))
			{
			    $f_name = $sname;
			    $s_name = $fname;
			}
		else
			{
	                   $f_name = $fname;
			   $s_name = $sname;
			}
		@ar = split('',$f_name);
		@arr = split('',$s_name);

		for($x=0; $x<length($f_name); $x++)
			{
		
			   if($ar[$x] ne $arr[$x])
				{
				   $count+=1;
				
				} 
			   else
				{
				   $count+=0;
				}
			}
	
		return $count;
	}

$ham_dist = hamDist($slack_usrname, $twit_handle);
print("$name\n $email\n\ $slack_usrname\n $bio_stack\n $twit_handle\n $ham_dist\n");
