function refresh1sec(){
	refresh30sec()
	var rawFile = new XMLHttpRequest();
	rawFile.open("GET", "cpuram", false);
	rawFile.send(null);
	document.getElementById("cpuram").innerHTML = rawFile.responseText;
	setTimeout('refresh1sec()',2000);
}
function refresh30sec(){
	var rawFile = new XMLHttpRequest();
	rawFile.open("GET", "timehostipdisk", false);
	rawFile.send(null);
	document.getElementById("timehostipdisk").innerHTML = rawFile.responseText;
				setTimeout('refresh30sec()',30000);
}