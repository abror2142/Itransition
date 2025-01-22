<?php
    $dir_handle = opendir('./data');
    $arr = array();
    while(($file_name = readdir($dir_handle)) == true)  
    {  
        if ($file_name !== "." && $file_name != ".."){
            array_push($arr,  strval(hash_file('sha3-256', "./data/".$file_name)));
        }
    }  
    rsort($arr);
    $s = join('', $arr);
    echo hash("sha3-256",  $s . "abror2142@gmail.com");

    closedir($dir_handle); 
?>