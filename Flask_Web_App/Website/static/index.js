//Sends POST request to delete-note endpoint
function deleteNote(noteId) {
    fetch('/delete-note', {
        method: "POST",
        body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
        //After receiving a response from delete-note endpoint, page is refreshed
        window.location.href = "/";
    });
}