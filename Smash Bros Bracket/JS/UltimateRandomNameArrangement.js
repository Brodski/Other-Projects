
function put_all_the_entries_in_tournament_so_that_no_player_faces_himself() {
	sort_player_and_entries();
	check_number_of_player();
	rng_setup_array();
	ordered_setup();
	proArray();
	rngBegin();
	the_consummation();
}


/////////////////////////////////////////////////
//
//			 		SETUP			
//
//////////////////////////////////////////////////
// Make arrays, order arrays, validate numbers  
/////////////////////////////////////////////////

function sort_player_and_entries() {
		//sorts the .values of players so that they are sequential, so that no n is the same as a n + (2 or more)
		
		//Goes through the player names. Once the code comes across a player that is not the same as the previous, perhaps b/c the player
		// is the next player or b/c the names are not in order, then the code then goes through *for* the rest of the players from that point 
		// to the end, (the number of entries) to find whether or not any more exist of that player exists. If there is the same player then 
		// swap positions

	for ( var n = 1; n < real_entries; n ++) {
		if ( p3player_entryArray[n][0].value != p3player_entryArray[n-1][0].value) {
			for ( var t = n; t < real_entries; t++) {
				if ( p3player_entryArray[t][0].value == p3player_entryArray[n-1][0].value) {
					//swap positions
						// holder = b ...position n is saved
						// b = a ...position t goes to n
						// a = holder ...position n goes to t
					var holder_player = p3player_entryArray[n][0].value;
					var holder_entry = p3player_entryArray[n][1].value;
					
					p3player_entryArray[n][0].value = p3player_entryArray[t][0].value;
					p3player_entryArray[n][1].value = p3player_entryArray[t][1].value;
					
					p3player_entryArray[t][0].value = holder_player;
					p3player_entryArray[t][0].value = holder_entry;
					
					
				}
			}
		}
		// p3player_entryArray[n][0] = Players should now be like A A A F F F Y Y B B C C C D D E Z Z Z Z Z Z Z Z 
	}
}

function proArray() {
		// Finds how many players are in the tournament. Even though the program asks before, this checks it and adjusts it.
		var numberOf_groups = 1;
		var gsizeArr = [];
		var size = 0;
		for (var n = 1; n < real_entries; n ++) {
			size = size + 1;
			if ( p3player_entryArray[n][0].value != p3player_entryArray[n-1][0].value) {
				numberOf_groups = numberOf_groups + 1; 
			}
		}
		playersArr = new Array(numberOf_groups);
		entriesArr = new Array(numberOf_groups);
		var gcounter = 0;
		for (var i =0; i < numberOf_groups; i++) {
			playersArr[i] = new Array();
			entriesArr[i] = new Array();
		}
		
		// FIRST
			playersArr[gcounter].push(p3player_entryArray[0][0].value);
			entriesArr[gcounter].push(p3player_entryArray[0][1].value);
		// THE LOOP		
		for ( var n = 1; n < real_entries; n ++) {
			if (p3player_entryArray[n][0].value != p3player_entryArray[n-1][0].value) {
				gcounter = gcounter + 1; }
			playersArr[gcounter].push(p3player_entryArray[n][0].value);
			entriesArr[gcounter].push(p3player_entryArray[n][1].value);
			}	
}

function rng_setup_array() {
	for (var n = 0; n <500; n ++) {
		RNG_arr.push( Math.random()) 
		var numb_rng = Math.random()*real_entries;
		slot_positionRNG_arr.push( Math.floor(numb_rng) );
	}
}


function ordered_setup() {
	ordered_names = new Array(real_entries)
	for (var n = 0; n < real_entries; n++){
		ordered_names[n] = new Array(2);
	}
}

function check_number_of_player() {
	var check_num_p = 0;
	for ( var n = 1; n < real_entries; n ++) {
		if (p3player_entryArray[n][0].value != p3player_entryArray[n-1][0].value)
			check_num_p = check_num_p + 1;
	}
	num_of_players = check_num_p;
}

function fraction_maker2() {
	remaining_pl = 0;
	for(var n = 0; n < playersArr.length; n++) {
		remaining_pl = remaining_pl	+ playersArr[n].length;
	}
	
	fraction_per[0] = 0;
	for (var n = 0; n < playersArr.length; n++) {
		fraction_per[n + 1] = fraction_per[n] + (playersArr[n].length / remaining_pl);	
	}
}


///////////////////////////////////////////////////////
//
//			PRO PLACEMENT OF FIRST ROUND MATCH UPS
//
///////////////////////////////////////////////////////
// Get a random entry and place it in 1st slot, then 2nd, then 3rd
// So that no entry is the same player.
///////////////////////////////////////////////////////
function rngBegin() {
	for (var n = 0; n < real_entries; n ++) { 
	// this array has the player and entry, it should be the correct number in which we can place a thing
	fraction_maker2();
	var twoProRNGNumbers =  get_random_slot(n);
	if (twoProRNGNumbers[0] == "end it") //In the unlikely_case, it retuns "end it". We go back to the top of the loop
		continue;
	var gInd = twoProRNGNumbers[0];
	var pInd = twoProRNGNumbers[1];
	
	
	ordered_names[n][0] = playersArr[gInd][0];
	ordered_names[n][1] = entriesArr[gInd][pInd];

	removeShitfunction(gInd,pInd);
	}
}

function removeShitfunction(gInd, pInd) {
	playersArr[gInd].splice(0, 1);
	entriesArr[gInd].splice(pInd, 1);
}

function get_random_slot(n) {
	
	var pre_rng;
	var contains;
	
	var gInd = getRandom_playergroup();
	var pInd = getRand_entryOfPlayer(gInd);
	
	//Second check - If the slot is even it does not matter what goes there, b/c it will not face itself.
	//				BUT if the slot is ODD then the previous slot cannot be the same player, unless it is a computer.
	
	// Subtest - "pass" will be true if the slot is a computer
	// Subtest 2 - "pass2" will be true if the previous slot is a computer and not from the same group then we are good to go
	var isComputer = is_slot_computerAI(gInd);
	if (n > 0) 
		var pass2 = is_previousSlot_comp_or_notSamePlayer(n, gInd);  	
			else 
			var pass2 = true;
	
	if (n % 2 == 1)	{
		if (isComputer == false //&& pass2 == false 
			 && pass2 == false
			 && playersArr[gInd].length >= remaining_pl ) {
			unlikely_case(n,gInd, pInd);
			return ["end it", "end it"];
		}
		while ( isComputer == false 		//while HUMAN and same previous slot is the same player and previous is not a computer
			&& pass2 == false) {
			// Run all the tests agains.
			// First reroll
			gInd = getRandom_playergroup();
			pInd = getRand_entryOfPlayer(gInd);
			// Second check if passes tests
			var isComputer = is_slot_computerAI(gInd);
			var pass2 = is_previousSlot_comp_or_notSamePlayer(n, gInd);
		}
	}
	var twoProRNGNumbers = [gInd, pInd];
	return twoProRNGNumbers;
}

function unlikely_case(n, gInd, pInd) {
			var adjusted;
			var int_rand;
			var r1;
			//get random number
		function roll_int() {
			r1 = Math.random() * (n);
			int_rand = Math.floor( r1 );
			if (int_rand % 2 == 1) {
				adjusted = true;
				int_rand = int_rand - 1; 
				}
			else adjusted = false;
			}
			roll_int();
			//while the groups interfere with each other
			while (ordered_names[int_rand][0] == ordered_names[n-1][0]
				|| ordered_names[int_rand+1][0] == playersArr[gInd][0]) {
				roll_int();	
				}
			if (adjusted == true)
				int_rand = int_rand + 1;
			
			ordered_names[n][0] = ordered_names[int_rand][0]; //holderPlay;
			ordered_names[n][1] = ordered_names[int_rand][1]; //holderEnt;
			ordered_names[int_rand][0] = playersArr[gInd][0];
			ordered_names[int_rand][1] = entriesArr[gInd][pInd];
			removeShitfunction(gInd,pInd);
}
	
	////////////////////////////////////////////
	//Grabs random group and random player
	////////////////////////////////////////
	function getRandom_playergroup() {
		var twoRandNumb = []
		for (var n = 0; n < playersArr.length ; n ++) {
			if (fraction_per[n+1] >= RNG_arr[counter_rng]) {
				counter_rng = counter_rng + 1;
				return n;
			}
		}
	}

	function getRand_entryOfPlayer(gInd) {
		p1 = Math.random() * (playersArr[gInd].length)
		return Math.floor(p1);
	}
	
	/////////////////////////////////////////////////	
	// Easy checking
	// Easy True or False
	//////////////////////////////////////////////////
function is_previousSlot_comp_or_notSamePlayer(theSlot, g){
	var pass2;
		if (   ordered_names[theSlot-1][0] == "" 		
			|| ordered_names[theSlot-1][0] != playersArr[g][0] )
				pass2 = true;
		else
				pass2 = false;
			return pass2;
	}
	
function is_slot_computerAI(g) {
	var pass; 
	if (playersArr[g][0] == "")
		pass = true;
	else
		pass = false;
	return pass;
}

function does_it_contain(the_array, item) {
	var contains = false;
	for (var n = 0; n < the_array.length; n++){
			if ( the_array[n] == item) {
				contains = true;
				break;
			}		
	}
	return contains;
}

	// THE FINALE
function the_consummation() {
	for ( var n = 0; n < real_entries; n ++) {
		if (ordered_names[n][0] != "")
			two_d_textboxes[0][n].value =  ordered_names[n][0] + " - " + ordered_names[n][1];
		else										
			two_d_textboxes[0][n].value = "AI level " + (Math.floor( Math.random() * 9) + 1); //RNG between 1 - 9
	}
}
	