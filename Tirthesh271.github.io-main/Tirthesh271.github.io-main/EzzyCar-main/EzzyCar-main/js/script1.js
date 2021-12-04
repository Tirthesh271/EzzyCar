/*var costumer_no,colour,chasis_no,model,yop;
costumer_no=34567;
colour='Blue';
chasis_no=456789;
model='Accord';
yop='2009';


document.getElementById("costumer_n").innerHTML=costumer_no;
document.getElementById("colour").innerHTML=colour;
document.getElementById("chasis").innerHTML=chasis_no;
document.getElementById("model").innerHTML=model;
document.getElementById("pur").innerHTML=yop;
*/
var mysql = require('mysql');

var con = mysql.createConnection({
  host: "localhost",
  user: "root",
  password: "Rajgad@12"
});

con.connect(function(err) {
  if (err) throw err;
  con.query("show tables");
  console.log("Connected!");
  alert("CONNECTED");
});
