function sumbit_pg2() {
	var isValid = entryRealValid();
	if ( isValid == true)
	{
		hideInlineStuff("pg2_rightID"); 
		changeToTable_p3(); 
		showInlineStuff("pg3_rightID");
		
		nameTableBuilder();
		putsNamesFromP2toP3();
	}
}

function prev_btn_p2() {
	deleteTable();
	hideInlineStuff("pg2_rightID");
	hideInlineStuff("errorID2");
	showInlineStuff("pg1_rightID");
}

function deleteTable() { 

	var dltTable = document.getElementById("p2table");
	while( 0 < dltTable.rows.length) {
		dltTable.deleteRow(0);
	}
}

function entryRealValid() {
	var sum =0;
	for (var n = 0; n < p2grpArray.length; n++) {
		if (p2grpArray[n][1].value == "") 
		p2grpArray[n][1].value = 0; 
	}
	for (var n = 0; n < p2grpArray.length; n++) {
		var a = p2grpArray[n][1].value;
		var b = proNumberValid(a,2);
		sum = sum + b;
		if (sum > real_entries || isNaN(b) == true) {
			showInlineStuff("errorID2"); 
			return; 
			}
	}	
	return true;
}


function nameTableBuilder() {
	var COLUMS = 4;
	if (made_already == false) {
		multiTableBuild(COLUMS); }
	top_nameTable(COLUMS);
	body_nameTable(COLUMS);
	putsNamesFromP2toP3();
}

function multiTableBuild(COLUMS) {
	var theDiv = document.getElementById("setup_tableID");
	for (var i = 0; i < COLUMS; i ++)
	{
		var newTable = document.createElement("table");
		theDiv.appendChild(newTable);
		newTable.classList.add("table_lay");
		newTable.id = "table"+i;
	}
	made_already = true;
}
	
function top_nameTable(COL) { // colums = 4
	for ( var n=0; n < COL; n++) {
		var myTable = document.getElementById("table"+n);
		var rowTop = myTable.insertRow(0);
		rowTop.classList.add("topRow");
	
		var c1 = rowTop.insertCell(0);
		var c2 = rowTop.insertCell(1);
		c1.innerHTML = "Player Name";
		c2.innerHTML = "Entry";
		c1.id = "playerHead" + n;
		c2.id = "entryHead" + n;
	}
}

// 	ASSIGNS TEXTBOX TO ARRAY TOO
function body_nameTable(COLUMS) {
	
	var count = 0;
	p3player_entryArray = new Array(real_entries);
	for (var i = 0; i < COLUMS; i ++) {
		var myTable = document.getElementById("table"+i);
		for (var n = 0; n < real_entries / COLUMS; n++) { //  rows = 1, 4, 8, or 16 = n
			var row = myTable.insertRow(n+1);
			var c1 = row.insertCell(0);
			var c2 = row.insertCell(1);
		
			var tbx = document.createElement("input");
			tbx.type = "text";
			tbx.classList.add("p3_player_width");
			c1.appendChild(tbx); 
		
			var tbx2 = document.createElement("input");
			tbx2.type = "text";
			tbx2.classList.add("p3_entry_width");
			c2.appendChild(tbx2); 
			
			p3player_entryArray[count] = new Array(2);
			p3player_entryArray[count][0] = tbx;
			p3player_entryArray[count][1] = tbx2;
			count = count + 1;	
			}
		}
}


function putsNamesFromP2toP3() {

	var count = 0;
	for (var n = 0; n < p2grpArray.length; n++) {
		for (var i = 0; i < p2grpArray[n][1].value; i++) {
			p3player_entryArray[count][0].value = p2grpArray[n][0].value;
			count = count + 1;
		}
	}
}
