// This function establishes the chatroom name.
// It takes the current user and the selected contact 
// and creates a chatroom ane consisting of both names
// put into alphabetical order so that when these two
// people chat, they will always use the same chatroom.
// This way, when they start a new chat, they can see 
// their history of their previous chats

document.querySelector('#new-room-name').onclick = function (e) {
    // Get all the contacts
    var contacts = document.getElementById("contact-list");

    // And get the seleceted contact
    var contact = Array.from(contacts).find(contacts => contacts.checked);

    // And get the current username
    const username = JSON.parse(document.getElementById('username').textContent);

    // This array will hold both the current username and the
    // selected contact
    let room_array = []
    room_array.push(username);
    room_array.push(contact.value);

    // Then sort the array
    room_array.sort();

    // Save the sorted, concatenated room name
    let roomname = ""
    for (var i = 0; i < room_array.length; i++) {
        roomname += room_array[i]
    }

    // And set the path with the new room name
    window.location.pathname = '/zoso/chat/' + roomname + '/';
};