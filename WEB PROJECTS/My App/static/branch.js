// Get the branch table body element
const tableBody = document.querySelector('#branch-table tbody');

// Fetch the branch data from the server and display it in the table
fetch('/branch_table')
  .then(response => response.text())
  .then(data => {
    // Set the innerHTML of the table body to the branch data
    tableBody.innerHTML = data;
  });

// Add an event listener to the form to handle adding a new branch
document.querySelector('#add-branch-form').addEventListener('submit', event => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the form data
  const formData = new FormData(event.target);

  // Send a POST request to the server to add the new branch
  fetch('/add_branch', {
    method: 'POST',
    body: formData
  })
  .then(response => response.text())
  .then(data => {
    // Display the response from the server
    alert(data);

    // Reset the form
    event.target.reset();

    // Fetch the updated branch data and display it in the table
    fetch('/branch_table')
      .then(response => response.text())
      .then(data => {
        // Set the innerHTML of the table body to the branch data
        tableBody.innerHTML = data;
      });
  });
});

// Add an event listener to the form to handle removing a branch
document.querySelector('#remove-branch-form').addEventListener('submit', event => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the form data
  const formData = new FormData(event.target);

  // Send a POST request to the server to remove the branch
  fetch('/remove_branch', {
    method: 'POST',
    body: formData
  })
  .then(response => response.text())
  .then(data => {
    // Display the response from the server
    alert(data);

    // Reset the form
    event.target.reset();

    // Fetch the updated branch data and display it in the table
    fetch('/branch_table')
      .then(response => response.text())
      .then(data => {
        // Set the innerHTML of the table body to the branch data
        tableBody.innerHTML = data;
      });
  });
});