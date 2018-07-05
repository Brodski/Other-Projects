
// Called when the user clicks on the browser action.
// Send a message to the active tab
chrome.browserAction.onClicked.addListener(function(tab) {
  chrome.tabs.query({active: true, currentWindow: true}, function(tabs) {
    var activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, {"message": "clicked_browser_action", "urlID": activeTab.id, "action": "pause" });
  });
});

//var playersArr = document.getElementsByTagName("video");
//var ytplayer = playersArr[0];



