	
	function clickWinner() {
		
		var ele = this;
		var thisID = parseInt(this.id);
			
		if  ((thisID % 2) == 0) { //if the button clicked is from even pair
			var loser = thisID + 1;
			if (winnerStatus[thisID] == true) { // clicking a winner
				winnerStatus[thisID] = false;
				//clear functions
				removeWinnerClass(ele, loser);
				reverse_names_advBtn(ele);
			}
			else { //we know winnerStatus[thisID] is false // clicking a ""loser""  or selecting a winner
				winnerStatus[thisID + 1 ] = false; 
				winnerStatus[thisID] = true;
				//functions
				esthetics_txtbox_btn(ele, loser); 
				names_advnaceBtn(ele);
			}		
		}
		if (( thisID % 2) == 1){ // if the button is odd
			var loser = thisID -1;
			if (winnerStatus[thisID] == true) { //clicking a winner
				winnerStatus[thisID] = false;
				//clear functions
				removeWinnerClass(ele, loser);
				reverse_names_advBtn(ele);
			}
			else { //clicking a 'loser' or selecting a winner
				winnerStatus[thisID -1] = false; 
				winnerStatus[thisID] = true;
				//functions
				esthetics_txtbox_btn(ele,loser);
				names_advnaceBtn(ele);
			}
		}
	}
function esthetics_txtbox_btn(ele_, _loser) {
	
		txt_boxes[ele_.id].className ="winner";
		arrayButton[ele_.id].className ="winnerbtn";
		
		txt_boxes[_loser].className = "loser";
		arrayButton[_loser].className = "loserbtn";
}

function removeWinnerClass(_ele,_loser) {
	
		txt_boxes[_ele.id].className = "";
		arrayButton[_ele.id].className = "";
		
		txt_boxes[_loser].className = "";
		arrayButton[_loser].className = "";
}

function names_advnaceBtn(_ele){
		
		var k; var i; var count = 0;
				
		for (k = 0; k < txt_boxes.length; k++) {
			if (justEndIt ==true)
				break;
			for (i = 0; i < two_d_textboxes[k].length; i++) {
				if ( _ele.id == count) { 
					var justEndIt = true;
					break; }
					count = count + 1;
				}
			}
		var i_pro = pair_txtbox[k-1][i];
		two_d_textboxes[k][i_pro].value = txt_boxes[count].value;
}

function reverse_names_advBtn(_ele) {
	
		var k; var i; var count = 0;
		for (k = 0; k < txt_boxes.length; k++) {
			if (justEndIt ==true)
				break;
			for (i = 0; i < two_d_textboxes[k].length; i++) {
				if ( _ele.id == count) { 
					var justEndIt = true;
					break; }
					count = count + 1;
				}
			}
		
	var i_pro = pair_txtbox[k-1][i];
	two_d_textboxes[k][i_pro].value = "";
	
}


