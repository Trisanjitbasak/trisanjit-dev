// Get the employee table body element
const tableBody = document.querySelector('#employee-table tbody');

// Fetch the employee data from the server and display it in the table
fetch('/employee_table')
  .then(response => response.text())
  .then(data => {
    // Set the innerHTML of the table body to the employee data
    tableBody.innerHTML = data;
  });

// Add an event listener to the form to handle adding a new employee
document.querySelector('#add-employee-form').addEventListener('submit', event => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the form data
  const formData = new FormData(event.target);

  // Send a POST request to the server to add the new employee
  fetch('/add_employee', {
    method: 'POST',
    body: formData
  })
  .then(response => response.text())
  .then(data => {
    // Display the response from the server
    alert(data);

    // Reset the form
    event.target.reset();

    // Fetch the updated employee data and display it in the table
    fetch('/employee_table')
      .then(response => response.text())
      .then(data => {
        // Set the innerHTML of the table body to the employee data
        tableBody.innerHTML = data;
      });
  });
});

// Add an event listener to the form to handle removing an employee
document.querySelector('#remove-employee-form').addEventListener('submit', event => {
  // Prevent the default form submission behavior
  event.preventDefault();

  // Get the form data
  const formData = new FormData(event.target);

  // Send a POST request to the server to remove the employee
  fetch('/remove_employee', {
    method: 'POST',
    body: formData
  })
  .then(response => response.text())
  .then(data => {
    // Display the response from the server
    alert(data);

    // Reset the form
    event.target.reset();

    // Fetch the updated employee data and display it in the table
    fetch('/employee_table')
      .then(response => response.text())
      .then(data => {
        // Set the innerHTML of the table body to the employee data
        tableBody.innerHTML = data;
      });
  });
});