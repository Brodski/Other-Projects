

function build_bracket() {
	initialize_Important_Variables();
	textBoxMaker(real_entries);
	location_Bracket(real_entries);
	addButton();
	addButton2();
	pair_assigner();
	prepWinner();
	lines_bracket();
	resizeStuff();
}

//
//Creates all textboxes, their is no location initially
//
function initialize_Important_Variables() {
	brackID = document.getElementById("bracket");
	T_boxesID = document.getElementById("T_boxesID");
	txt_boxes = T_boxesID.getElementsByTagName("input");
}

	function textBoxMaker(num_entries)
	{
		var textboxes_at_each_step;
		steps = Math.log2(num_entries);
		var count = 0;
		for (k = 0; k < steps+1; k++)
		{
			textboxes_at_each_step = num_entries/Math.pow(2,k);
			for (i =0; i <textboxes_at_each_step; i++) 
			{
				var textEle = document.createElement("input");
				textEle.type = "text";
				T_boxesID.appendChild(textEle);
				count = count + 1;
			}
		}
	}	

	function location_Bracket(num_entries) {
		txt_boxes[0].parentElement.style.position ="relative"
		make_textbox_array(num_entries);
		
		//roundOne_Positioning will postion the 1st round, And it will return count, ie the textbox
		// pro_Positioning will place the next round in between the previous round.
		count = roundOne_Positioning(num_entries);
		pro_Positioning(num_entries, count);
	}
	
	function make_textbox_array(num_entries) {
		
		var steps = Math.log2(num_entries);
		var textboxes_at_each_step;
		var cnt =0;
		two_d_textboxes;
		for (var k = 0; k < steps+1; k++)
		{
			two_d_textboxes.push( [] ); // new Array
			pair_txtbox.push( [] );
		}
		for (var k = 0; k < steps+1; k++)
		{
			textboxes_at_each_step = num_entries/Math.pow(2,k);
			for (var i =0; i <textboxes_at_each_step; i++) 
			{
				
				two_d_textboxes[k].push( txt_boxes[cnt]);
				var testlolo=	two_d_textboxes[k][i];
				var testlol =	two_d_textboxes[k][0];
				two_d_textboxes[k][i];
				two_d_textboxes[k];
				cnt = cnt +1;
			}
		}
	}
	
	function roundOne_Positioning(num_entries) {
		//Arbitrary location and change, ie distance between boxes, for esthetics
		var _count = 0;
		var y = 10;
		var x = 35;
		change_y = 60;
		pairs_of_boxes_gap = txt_boxes[0].offsetHeight + 5; //gets height of textbox + add arbitrary value

		//initial
		txt_boxes[_count].style.position ="absolute";
		txt_boxes[_count].style.zIndex =10;
		txt_boxes[_count].style.left = x;
		txt_boxes[_count].style.top	= y; 
		_count = _count +1;	
		
		for ( n = 1; n < num_entries; n++) 
		{
			if (_count % 2 == 0) // if even
			{
				y = y + change_y; //y = a fixed distance away from previous
				txt_boxes[_count].style.position ="absolute";
				txt_boxes[_count].style.zIndex =10;
				txt_boxes[_count].style.left = x;
				txt_boxes[_count].style.top	= y; 
				_count = _count +1;
			}
		
			else if (_count % 2 == 1) // if odd
			{
				y = y + pairs_of_boxes_gap; // y = just below the previous box
				txt_boxes[_count].style.position ="absolute";
				txt_boxes[_count].style.zIndex =10;
				txt_boxes[_count].style.left = x;
				txt_boxes[_count].style.top	= y;
				_count = _count +1;
			}
		}
		return _count;
	}
	
	function pro_Positioning(num_entries, _count)
	{
		change_x = 280; //Arbitrary value
		var box_height = two_d_textboxes[0][0].offsetHeight;
		for (k = 1; k < steps+1; k++)
		{	
			//Very last textbox
			if ( k == steps) {
				laststep(k);
				break;
			}
		textboxes_at_each_step = num_entries/Math.pow(2,k);
		var dist = two_d_textboxes[k-1][2].offsetTop - two_d_textboxes[k-1][0].offsetTop;
		
		for (i =0; i< textboxes_at_each_step; i++)
		{
			if ( (i % 2) == 0) {
				two_d_textboxes[k][i].style.position ="absolute";
				two_d_textboxes[k][i].style.zIndex =10;		
				two_d_textboxes[k][i].style.top = two_d_textboxes[k-1][2*i].offsetTop + (0.5)*dist;
				two_d_textboxes[k][i].style.left = two_d_textboxes[k-1][0].offsetLeft + change_x;
			}		
			else if ( (i % 2) ==1) {
				two_d_textboxes[k][i].style.position ="absolute";
				two_d_textboxes[k][i].style.zIndex =10;
				two_d_textboxes[k][i].style.top = 5 + two_d_textboxes[k][i-1].offsetTop + box_height;
				two_d_textboxes[k][i].style.left = two_d_textboxes[k-1][0].offsetLeft + change_x;
					
			}
		}
		}	
	}
	
	function laststep(_k) {
		
			var change_x = 260; //Arbitrary value
			dist = two_d_textboxes[_k-1][1].offsetTop - two_d_textboxes[_k-1][0].offsetTop;
			two_d_textboxes[_k][0].style.position ="absolute";
			two_d_textboxes[_k][0].style.zIndex =10;
			two_d_textboxes[_k][0].style.top  = two_d_textboxes[_k-1][0].offsetTop + (0.5)*dist;
			
			two_d_textboxes[_k][0].style.left = two_d_textboxes[_k-1][0].offsetLeft + change_x;
	}
	
	function addButton() { 		
		for (var i =0; i < txt_boxes.length-1; i ++) 
		{
			btn_win = document.createElement("button");
			var t = document.createTextNode("W");
			btn_win.appendChild(t);
			btn_win.className = "txtz"
			btn_win.id = "i";
			T_boxesID.appendChild(btn_win);
		}
	}
		
	function addButton2() {
		arrayButton = T_boxesID.getElementsByTagName("button");
		var count=0;
		for (var k = 0; k < steps; k++){
			
			textboxes_at_each_step = num_entries/Math.pow(2,k);
			
			for( var i =0; i < two_d_textboxes[k].length; i++) {
		    arrayButton[count].addEventListener("click", clickWinner);
			arrayButton[count].id = count;
			arrayButton[count].style.position ="absolute";
			arrayButton[count].style.zIndex =10;
			arrayButton[count].style.height = txt_boxes[count].offsetHeight; 
				                                                        	// I can't get it to work, so I guess value
			arrayButton[count].style.left = txt_boxes[count].offsetLeft - arrayButton[0].offsetWidth + 1;// - arrayButton[count].style.width;
			arrayButton[count].style.top = txt_boxes[count].offsetTop; 
			var mylol = txt_boxes[count].offsetTop; 
			var mylmoa = arrayButton[count].style.top;
			count = count + 1;
			
			}
		}
	}
		
	function pair_assigner() {
			//give ID
			for (var k =0; k < steps +1;  k++)
			{
				var skill_count = 0;
				pair_txtbox[k][0] = skill_count; //initial 
				for( var i = 1; i < two_d_textboxes[k].length ; i++) 
				{
				pair_txtbox[k][i] = skill_count;
				if ((i % 2) ==1) {
					skill_count = skill_count + 1; }
				}
			}
	}
		
	function prepWinner() {
		//set all values to false
		for ( var i = 0; i <arrayButton.length; i++) {
			winnerStatus[i] = false; 
		}
	}
	
	function lines_bracket() {
		steps = Math.log2(real_entries);
		var c = document.getElementById("myCanvas");
		var ctx = c.getContext("2d");
			/* (comment below is copyed from internet somewhere)
            * Your drawings need to be inside this function otherwise they will be reset when 
            * you resize the browser window and the canvas goes will be cleared.
            */// so, first size then draw 
		resizeCanvas();
		
		var yshift = 5;
		var x1shift = 10;
		var x2shift = 40;
		var x3shift = 40;
		var x; var y;
		
		for ( var k = 0; k < steps -1; k ++) {
			
			var dist = two_d_textboxes[k][2].offsetTop - two_d_textboxes[k][0].offsetTop;
		
			for (var i = 0; i < (0.5)*two_d_textboxes[k].length; i++) {
			ctx.beginPath();
			//1st
			x = two_d_textboxes[k][2*i].offsetLeft + two_d_textboxes[0][0].offsetWidth + x1shift; 
			y = two_d_textboxes[k][2*i].offsetTop + two_d_textboxes[0][0].offsetHeight + yshift; 
			ctx.moveTo(x,y); //start here. should be between the textbox pair of clicked
		
			//2nd
			x = x + x2shift;
			ctx.lineTo(x,y);
		
			//3rd
			if ((pair_txtbox[k][2*i] % 2) == 0) { // if the pair is even
			y = y + (0.5)*dist; }
		
			else if ((pair_txtbox[k][2*i] % 2) == 1) { // if the pair is odd
			 y = y - (0.5)*dist;    }
			ctx.lineTo(x,y);
		
			//4th
			x = x + x3shift;
			ctx.lineTo(x,y);
		
			ctx.strokeStyle = "#00FFFF" //aqua
			ctx.stroke();
			}
			
		}
		
		//very last bracket, the champion!
		ctx.beginPath();
		// 1st
		x = two_d_textboxes[steps-1][0].offsetLeft + two_d_textboxes[0][0].offsetWidth + x1shift; 
		y = two_d_textboxes[steps-1][0].offsetTop + two_d_textboxes[0][0].offsetHeight + yshift; 
		ctx.moveTo(x,y); //start here. should be between the textbox pair of clicked
		//2nd
		x = x + x1shift +x3shift + 40;
		ctx.lineTo(x,y);
		ctx.strokeStyle = "#00FFFF" //aqua
		ctx.stroke();	
	}
	
	function zFixing() {
		txt_boxes.style.zIndex = 10;
		arrayButton.style.zIndex= 10;
	}
	

	function resizeStuff() {
		
		var width_arbitrary = 10;
		var vert_arbitrary = 10;
		var bigWrap = document.getElementById("big_wrapID");
		var lft_ban = document.getElementById("leftBannerID");
		var topBan = document.getElementById("topBanID");
		var btn_brack = document.getElementById("btn_Bracket");
		
		var dist_y_txt_box = two_d_textboxes[0][2].offsetTop - two_d_textboxes[0][0].offsetTop;
		var dist_x_txt_box = two_d_textboxes[1][0].offsetLeft - two_d_textboxes[0][0].offsetLeft;
		
		all_height = dist_y_txt_box*(real_entries * 0.5 +1);
		all_width = dist_x_txt_box * (steps+1) + lft_ban.offsetWidth ; 
		
		bigWrap.style.height = all_height + vert_arbitrary; 
		topBan.style.minWidth = all_width + width_arbitrary;
		btn_brack.style.position ="absolute";
		btn_brack.style.top =  all_height + vert_arbitrary - 100; 
				
	}
	
	function resizeCanvas() {
		var vert_arbi = 50;
		var c = document.getElementById("myCanvas");
		var vert_dist =  two_d_textboxes[0][2].offsetTop - two_d_textboxes[0][0].offsetTop;
		var hori_dist = two_d_textboxes[1][0].offsetLeft - two_d_textboxes[0][0].offsetLeft
		c.height = vert_dist*(real_entries * 0.5 ); 
		c.width =  hori_dist*(steps+1);
		//  http://stackoverflow.com/questions/4288253/html5-canvas-100-width-height-of-viewport
	}
	