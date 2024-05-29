# Cookie & Session Difference by Kvnbbg (Kevin MARVILLE)

This project demonstrates the difference between cookies and sessions in a Python web application using Flask. It includes a simple form to generate random user data, which is then stored in a session. The project also features dynamic, recursive comments to simulate real-world interactions.

## Features
- Generate random user data
- Store data in session (server-side)
- Display data with flash messages
- Responsive design for mobile devices
- Dynamic, recursive comments

## Screenshots

![Mobile View 1](static/replit_python_mobile.png)
![Mobile View 2](static/replit_python_mobile_2.png)

## Setup

1. Ensure you have the necessary packages installed:
   ```bash
   pip install flask flask-wtf
   ```

2. Run the Flask application:
   ```bash
   python main.py
   ```

3. Access the application in your web browser:
   - Navigate to `http://127.0.0.1:5000/`.

## Code Overview

### `main.py`

This is the main file for the Flask application. It sets up routes for generating and displaying random user data, and includes functionality for recursive flash messages.

### `templates/index.html`

This file contains the HTML template for the index page, where users can generate random data.

### `templates/show_data.html`

This file contains the HTML template for displaying the generated data and dynamic comments.

### `static/styles.css`

This file contains the CSS for styling the application, including responsive design for mobile devices.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.