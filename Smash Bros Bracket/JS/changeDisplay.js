
function changeToTable_p2() { 
		
//	document.getElementById("bodyID").style.backgroundColor  =  'rgb(21,23,30)'; // shiek
	document.getElementById("Table_css").setAttribute("href", "CSS/Table_p2.css");		
}

function changeToTable_p3() { 
		
//	document.getElementById("bodyID").style.backgroundColor  =  'rgb(21,23,30)'; // shiek
	document.getElementById("Table_css").setAttribute("href", "CSS/Table_p3.css");		
		
	}

function hideInlineStuff(ID_ofThingToHide) { 
	document.getElementById(ID_ofThingToHide).style.display = "none"; //.classList.add("hiddenClass");
}
	
function showInlineStuff(ID_ofThingToHide) { 
	document.getElementById(ID_ofThingToHide).style.display = "inline-block"; //.classList.add("hiddenClass");
}
	
	
function hideStuff(ID_ofThingToHide) { 
	document.getElementById(ID_ofThingToHide).classList.add("hiddenClass");
}
	
function showStuff(ID_ofThingToShow) { // showStuff("errorID");
	document.getElementById(ID_ofThingToShow).classList.remove("hiddenClass");
}
	
	