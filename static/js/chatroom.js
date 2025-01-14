// This script handles the real-time chat using a websocket.

// This is the div where the chat is stored
const chat = document.querySelector('#chat')

// And this is the name of the chatroom
const roomname = JSON.parse(document.getElementById('room-name').textContent);


// Establish a new websocket using the roomname as part of the url
const chatSocket = new WebSocket(
    'ws://'
    + window.location.host
    + '/ws/zoso/chat/'
    + roomname
    + '/'
);


// When a new message arrives...
chatSocket.onmessage = function(e) {
    // Read in the data
    const data = JSON.parse(e.data);

    // Create a new element for the message
    const chatMessage = document.createElement('div')

    // Get the ID of the 'current' user
    const curUser = JSON.parse(document.getElementById('user_id').textContent)

    // And get the ID of the user who sent the message
    const userID = data['user_id']

    // Get the contents of the message
    chatMessage.innerText = data.message
    
    // Add the message as either the 'sender' or the 'receiver'
    // so we can use CSS to display the messages differently
    if (userID === curUser) {
        chatMessage.classList.add('message', 'sender')
    } else {
        chatMessage.classList.add('message', 'receiver')
    }

    // Add the chat to the beginning of the chat div
    // so the message appears at the top
    chat.prepend(chatMessage)
};


// Show error if chat socket is closed unexpectedly
chatSocket.onclose = function(e) {
    console.error('The chat socket has stopped working unexpectedly...');
};


// Handle the 'Enter' key
// When the 'Enter' key is pressed, call the 'click' function
// on the Submit button
document.querySelector('#chat-message-input').onkeyup = function(e) {
    if (e.keyCode === 13) {  // enter, return
        document.querySelector('#chat-message-submit').click();
    }
};


// Function for when the 'Send Message' button is clicked
document.querySelector('#chat-message-submit').onclick = function(e) {
    // Get the message from the input text
    const messageInput = document.querySelector('#chat-message-input');
    const message = messageInput.value;

    // Send the message
    chatSocket.send(JSON.stringify({
        'message': message
    }));

    // Clear the input text to be ready for the next message
    messageInput.value = '';
};


// Set the focus on the chat input
document.querySelector('#chat-message-input').focus();