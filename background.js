// background.js
chrome.webNavigation.onCommitted.addListener(function (details) {
  const currentURL = details.url;
  // const currentURL = window.location.href;
  sendURLToServer(currentURL);
});

function sendURLToServer(url) {
  fetch('http://localhost:5000/url_log', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ url: url })
  })
    .then(response => response.json())
    .then(data => {
      console.log('Successful', data.blockornot);
      if(data.blockornot=='block'){
        console.log('yes');
        browser.tabs.update({ url: "https://developer.mozilla.org" });
      }
    })
    .catch(error => {
      console.error('Failed to send URL :', error);
    });
}
