<?php
$username=$_POST['username'];
$password=$_POST['password '];
$email=$_POST[ 'email ']
//Database Connection
$conn=new mysqli_connect('localhost','root',' ','ram');
if($conn->connect_error)
{echo "$conn->connect_error";
die( "Connection Failed: ".$conn->connect_error);}
else{
$sql="INSERT INTO stu(username,password,email)VALUES ('$username','$password','$email')";
if(mysqli_query($conn,ssql)){
echo "Records added successfully ";}
else{
echo "ERROR:Could not able to execute $sql " mysqli_error($conn);}
$conn->close();
}
?>
