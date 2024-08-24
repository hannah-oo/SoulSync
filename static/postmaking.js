// Array to store all posts
let posts = [];

// Function to display all posts
function displayPosts() {
    const postList = document.getElementById('post-list');
    postList.innerHTML = ''; // Clear the existing posts

    // Iterate through each post in the posts array and display it
    posts.forEach((post, index) => {
        const postContainer = document.createElement('div');
        postContainer.className = 'post-container';

        const postContent = document.createElement('p');
        postContent.className = 'post-content';
        postContent.textContent = `${post.content} (Feeling: ${post.emotion})`;
        postContainer.appendChild(postContent);

        // Reaction buttons
        const reactionButtons = document.createElement('div');
        reactionButtons.className = 'reaction-buttons';

        ['❤️', '👍', '🌟'].forEach(emoji => {
            const button = document.createElement('button');
            button.textContent = emoji;
            button.onclick = () => reactToPost(index, emoji);
            reactionButtons.appendChild(button);
        });

        postContainer.appendChild(reactionButtons);

        // Delete button
        const deleteButton = document.createElement('button');
        deleteButton.className = 'delete-button';
        deleteButton.textContent = 'Delete';
        deleteButton.onclick = () => removePost(index);
        postContainer.appendChild(deleteButton);

        postList.appendChild(postContainer);
    });
}

// Function to create a new post
function createPost() {
    const content = document.getElementById('new-post-content').value;
    const emotion = document.getElementById('current-emotion').value;

    // Check if the content is not empty
    if (content.trim()) {
        // Add the new post to the posts array
        posts.push({ content, emotion });

        // Clear the textarea for new input
        document.getElementById('new-post-content').value = ''; 

        // Update the displayed posts
        displayPosts();
    } else {
        alert('Please write something before posting!');
    }
}


// Function to handle reactions to a post
function reactToPost(index, emoji) {
    alert(`You reacted to the post with ${emoji}`);
}

// Initial display of posts when the page loads
displayPosts();