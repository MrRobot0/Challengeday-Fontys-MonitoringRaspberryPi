function refreshsimpel(){
	var rawFile = new XMLHttpRequest();
	rawFile.open("GET", "refreshsimpel", false);
	rawFile.send(null);
	document.getElementById("refreshsimpel").innerHTML = rawFile.responseText;
	setTimeout('refreshsimpel()',1000);
}