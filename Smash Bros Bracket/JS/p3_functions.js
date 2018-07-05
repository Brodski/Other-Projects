
function submit_pg3() {
	hideInlineStuff("pg3_rightID");
	showInlineStuff("bracket");
	showStuff("myCanvas");
	document.getElementById("bodyID").style.backgroundColor = 'rgb(19,22,27)'; //FALCON
	
	if (dont_repeat_this == false) {
		build_bracket();
		dont_repeat_this = true;
	}
	put_all_the_entries_in_tournament_so_that_no_player_faces_himself();
}

function prev_btn_pg3() {
	deleteTable2_fromDynTables();
	hideInlineStuff("pg3_rightID");
	showInlineStuff("pg2_rightID");
	changeToTable_p2();
}
////////////////////////////////////////////////////
// - This below is the button to PAGE 4, the final bracket
///////////////////////////////////////////////////
function prev_btn_brack() { 
	hideInlineStuff("bracket");
	hideStuff("myCanvas");
	showInlineStuff("pg3_rightID");
	document.getElementById("bodyID").style.backgroundColor = 'rgb(21,23,30)'; // shiek
}

function deleteTable2_fromDynTables() {
	var tID = document.getElementById("setup_tableID");
	var tblArr = tID.getElementsByTagName("table");
	for (var n = 0; n < tblArr.length; n++) {
		while( 0 < tblArr[n].rows.length) {
			tblArr[n].deleteRow(0);
		}
	}
}

function testingstuff() {
		var sum1=0;
		for (var n = 0; n < p2grpArray[n][1].value ; n++) {
		var playerName = p2grpArray[n][0];
		var playerName2 = p2grpArray[n][0].value;
		sum1 = sum1 + parseInt( p2grpArray[n][1].value );
		}
}
