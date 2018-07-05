
function submit_btn_p1() {
	real_entries = T_selection();
	num_of_players = num_players();
	ent_per = entries_per();
	var pass = volume_check();
	
	if ( !isNaN(real_entries) && !isNaN(num_of_players) && !isNaN(ent_per) && pass)
	{
		hideInlineStuff("pg1_rightID");
		showInlineStuff("pg2_rightID");
		tableBuilder();
	}

}

function volume_check() {
	if ( (ent_per * num_of_players) <= real_entries ) // tournament size must be less than total entries.
		var pass = true;
	else {
		var pass = false;
		showStuff("errorID");
		}
	return pass;
}

function T_selection() {
    var x = document.getElementById("size_dropboxID").selectedIndex;
    var y = document.getElementById("size_dropboxID").options;
	var size = parseInt(y[x].text);
	return size;
  
	}
	
function num_players() {
	var a = document.getElementById("numPlayersID").value;
	b = proNumberValid(a,1);
	return b;
	}

function entries_per() {
	var a = document.getElementById("ent_per_playerID").value;
	b = proNumberValid(a,1);
	return b;}
	
function checkNumber(b) {
	if (( (b % 1) == 0 ) && (b >= 0)) { //It has to be a number and it must 
		return true;				   //be an integer and greater than 0
	}
	else {
		return false;
	}
}

function proNumberValid(a, page) {
		
	var b = parseFloat(a);
	if (isNaN(a) == true || checkNumber(b) == false) {
		if (page == 2) { showStuff("errorID2"); }
		else { showStuff("errorID"); }
		return; 
		}
	else if (checkNumber(b) == true) 
		return b;
}


function tableBuilder() {
	 top_Table();
	 p2grpArray = new Array(num_of_players);
	var myTable = document.getElementById("p2table");
	for (var n = 1; n < num_of_players + 1; n++) {

		
		var row = myTable.insertRow(n);
		var c1 = row.insertCell(0);
		var c2 = row.insertCell(1);
		var c3 = row.insertCell(2);
		var c4 = row.insertCell(3);
		c1.innerHTML = "Player " + (n);
			var tbxPlayer = document.createElement("input");
			tbxPlayer.type = "text";
			tbxPlayer.classList.add("p2_playerTx_width");
		c2.appendChild(tbxPlayer); 
		c3.innerHTML = "Entries:";
			var tbxEntry = document.createElement("input");
			tbxEntry.type = "text";
			tbxEntry.classList.add("p2_entrytx_width");
			tbxEntry.value = ent_per;
			c4.classList.add("taRight");
		c4.appendChild(tbxEntry); 
		
		p2grpArray[n-1] = new Array(2);
		p2grpArray[n-1][0] = tbxPlayer; 
		p2grpArray[n-1][1] = tbxEntry;
	}
}


function top_Table() {
	
	var myTable = document.getElementById("p2table");
	
	var rowTop = myTable.insertRow(0);
	rowTop.style.height = 50;
	rowTop.style.backgroundColor = "#D7E9FE";
	var c1 = rowTop.insertCell(0);
	var c2 = rowTop.insertCell(1);
	var c3 = rowTop.insertCell(2);
	var c4 = rowTop.insertCell(3);
	c4.classList.add("taRight");
	c1.innerHTML ="";
	c2.innerHTML = "Player Name";
	c3.innerHTML = "";
	c4.innerHTML = ""; 
}

///////////////////////////////////////////////////////////////////
//
//		Since I took out the Groups check box div, the functions associated 
//		with it showed below, have no use now.
//
///////////////////////////////////////////////////

function overMouse() {
	var thediv = document.getElementById("help_grpID");
	thediv.classList.remove("hiddenClass");
}	

function outMouse() {
	var thediv = document.getElementById("help_grpID");
	thediv.classList.add("hiddenClass");
}


function ck_box_fnc() {
		var ch_box = document.getElementById("ch_bx_groupID");
		if (ch_box.checked == true) {
			showStuff("row_entries");
		}
		else { 
			t1ent = document.getElementById("ent_per_playerID");
			t1ent.value = 1;
			hideStuff("row_entries");
		}
}
////////////////////////////////////////////////////////////////////////////////
//
//	quicker() is for me to test out stuff. Not used in the functioning page			
//
////////////////////////////////////////////////////////////////////////////////
function quicker() {
	var t = document.getElementById("numPlayersID");
	t.value = 5;
	var tt = document.getElementById("ent_per_playerID");
	tt.value = 6;
	
}

function quicker2 () {
	p2grpArray[0][0].value = 'one';
	p2grpArray[1][0].value = 'two';
	p2grpArray[2][0].value = 'three';
	p2grpArray[3][0].value = 'four';
	p2grpArray[4][0].value = 'five';
}

function quicker3() {
	var c111 =0;
	
	for (var i =0; i < p2grpArray.length; i++ ) {
		for (var n =0; n < p2grpArray[i][1].value; n++ ) {
		p3player_entryArray[c111][1].value = p2grpArray[i][0].value + i + c111;
		c111 = c111 + 1;
		}
	}
}