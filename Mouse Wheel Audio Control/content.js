//alert("hello from youtube kickass!")

// content.js
chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if( request.message === "clicked_browser_action" ) {
      console.log("click on clicked_browser_action yo!");
	  console.log("You just clicked on the browserAction button, from " + request.urlID);
    }
	if(request.action === "pause"){
		pauseIt();
	}
  }
);

var VOLUME_VEL = 0.05; //How much the volume changes per mousewheel click


function pauseIt(){
	
	document.addEventListener('click', function(e) {
		var target = e.target;
		var textzz = target.id;
		console.log("e.target.id: " + textzz);
		console.log("e.target.localName: " + e.target.localName);
	});
	
	var playersArr = document.getElementsByTagName("video");
	var ytplayer = playersArr[0];
	ytplayer.addEventListener("wheel", respondToHover);
	ytplayer.addEventListener("mousedown", respondToClick);
	ytplayer.addEventListener("keydown", respondToKey,false);
	ytplayer.addEventListener("keypress", respondToKey,false);
	
	if (ytplayer.paused) {
		ytplayer.play();
		console.log("PLAYING!"); 
	}
	else {
		ytplayer.pause();
		console.log("PAUSING!");
	}
	console.log("ytplayer.paused: " + ytplayer.paused )
}

function respondToKey(e){
	console.log("e.key: " + e.key + " e.keyCode " + e.keyCode);
	
}

function respondToHover(e) {
	e.preventDefault();
	var playersArr = document.getElementsByTagName("video");
	var ytplayer = playersArr[0];
	
	if (e.deltaY > 0){
		console.log("-----MOUSE WHEEL DOWN!-----");
		//adjustVolumeWheel("decrease");
	//	ytplayer.volume = ytplayer.volume - 0.1 ;
		sendWheelEventToAudioButton("decrease", ytplayer);
	}
	else {
		console.log("-----MOUSE WHEEL UP!-----");
		//adjustVolumeWheel("increase");
		//ytplayer.volume = ytplayer.volume + 0.1 ;
		sendWheelEventToAudioButton("increase", ytplayer);
	}	
	
	hoverOnMute();
	//uselessStuff();
	//OtherStuff(ytplayer);
	
}

function sendWheelEventToAudioButton(direction, ytplayer){
	hoverOnMute();
	
	if (ytplayer.muted){
		clickOnMute();
		console.log("MUTED");
	}
	console.log("ytplayer.muted: " +ytplayer.muted);
	
	if (direction == "increase"){
		
		var wheelEvent = new WheelEvent("wheel", {"deltaY": -1, "deltaMode": 1});
	}
	else{
		var wheelEvent = new WheelEvent("wheel", {"deltaY": 1, "deltaMode": 1});
	}
	var ytpHover = document.getElementsByClassName("ytp-volume-control-hover")[0];
	ytpHover.dispatchEvent(wheelEvent);
	
	
}

function uselessStuff(){
	//var volCont = document.getElementsByClassName("ytp-volume-control-hover");
	var volCont = document.getElementsByClassName("ytp-mute-button");
	
	var syntheticEvent = new WheelEvent("wheel", {"deltaY": 4, "deltaMode": 1});
	//console.log(syntheticEvent.deltaY);
	//ytplayer.dispatchEvent(syntheticEvent);
	
	var keyEvent = new KeyboardEvent ("keydown", {key: "ArrowUp",
			view: window,
			bubbles: true,
			cancelable: true} );
	var divz = document.getElementById('player-api');
	divz.dispatchEvent(keyEvent);
	
	var movieP = document.getElementById("movie_player");
	movieP.dispatchEvent(syntheticEvent);
	movieP.dispatchEvent(keyEvent);
	//console.log("keyEvent.key: " + keyEvent.key);
	
}

function respondToClick(e) {
	if (e.which == 2){
		console.log("MOUSE WHEEL CLICK!");	
		clickOnMute();
	}	
	console.log("clickEvent " + clickEvent + " clickEvent.which " + clickEvent.which);

}

function clickOnMute(){
	//Click Mute Button
	var clickEvent = new MouseEvent('click');
	var muteButton = document.getElementsByClassName("ytp-mute-button")[0].parentElement;
	muteButton.dispatchEvent(clickEvent);
	document.getElementsByClassName("ytp-mute-button")[0].dispatchEvent(clickEvent);
	
}

function hoverOnMute(){
	
	var overEvent = new MouseEvent("mouseover");
	var muteButton = document.getElementsByClassName("ytp-mute-button")[0].parentElement;
	muteButton.dispatchEvent(overEvent);
}

//This doesnt realy do anything
function OtherStuff(ytplayer){
	//var kyEvent = new KeyboardEvent ("keydown", {key: "ArrowUp"});	
}

function adjustVolumeWheel(direction){
	var playersArr = document.getElementsByTagName("video");
	var ytplayer = playersArr[0];
	var nVol;
	
	var preVolSlider = document.getElementsByClassName("ytp-volume-slider-handle")[0];
	var volSlider = preVolSlider.attributes;
	
	//volSlider.getNamedItem("style").value = "left: 10px";
	//var oldVol = ytplayer.volume;
	console.log("OLD VOLUME " + ytplayer.volume);
	console.log("OLD style: " + volSlider.getNamedItem("style").value);
	if (!isVolumeAtLimit(direction, ytplayer)){
		ytplayer.muted = false;
		if (direction == "increase"){
			ytplayer.volume = ytplayer.volume + VOLUME_VEL;
		} else {
			ytplayer.volume = ytplayer.volume - VOLUME_VEL;
		}	
	}
	var sValue = "left: " + (ytplayer.volume*40) + "px";
	volSlider.getNamedItem("style").value = sValue;
	console.log("sValue: " + sValue);
		

//	printAttributes(volSlider);
	//console.log("PRINTING ytplayer.attributes")
	console.log("ytplayer.muted " + ytplayer.muted);
	//printAttributes(ytplayer.attributes);

}

function isVolumeAtLimit(direction, ytplayer){
	if ((direction == "increase") && ytplayer.volume > (1 - VOLUME_VEL) ){
		ytplayer.volume = 1;
		ytplayer.muted = false;
		return true;
	} 
	if ((direction == "decrease") && ytplayer.volume < (0 + VOLUME_VEL) ){
		ytplayer.volume = 0;
		ytplayer.muted = true;
		return true;
	}
	return false;
}

function printAttributes(attrib){
	for (var i=0; i <attrib.length; i++){
		console.log("" + i + " attrib[i]; " + attrib[i] + " attrib[i].name " + attrib[i].name + " " + attrib[i].value);
	}
}

