// Function to post a question dynamically
function postQuestion() {
  const questionInput = document.getElementById('question-input');
  const questionText = questionInput.value.trim();
  const postsSection = document.getElementById('posts-section');

  if (questionText !== '') {
      // Create post container
      const postDiv = document.createElement('div');
      postDiv.classList.add('post');

      // Post content
      postDiv.innerHTML = `
          <h3>${questionText}</h3>
          <p><strong>Anonymous User</strong></p>
          <p>This question has been posted for the community. Feel free to answer.</p>
          <div class="post-actions">
              <span onclick="upvote(this)">👍 Upvote</span>
              <span>💬 Comment</span>
              <span>🔗 Share</span>
          </div>
      `;

      // Insert new post at the top
      postsSection.insertBefore(postDiv, postsSection.children[1]);
      
      // Clear input field
      questionInput.value = '';
  } else {
      alert('Please enter a question before posting.');
  }
}

// Function to handle upvotes
function upvote(element) {
  element.innerHTML = '👍 Upvoted';
  element.style.fontWeight = 'bold';
}