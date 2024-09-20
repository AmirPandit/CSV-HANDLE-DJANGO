# CSV Upload and Book Management System

This Django project provides functionality for uploading CSV files containing book information and storing this data in a database. It includes a REST API endpoint to handle the upload process and a simple HTML interface for file uploads.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Installation

Follow these steps to set up the project:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AmirPandit/CSV-HANDLE-DJANGO.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd populatedata
   ```

3. **Create and activate a virtual environment (optional but recommended):**

   - **On Windows:**

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - **On macOS/Linux:**

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. **Install the dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply the database migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

## Usage

### Uploading CSV Files

1. **Navigate to the upload page:**

   Open your browser and go to [http://localhost:8000/upload](http://localhost:8000/upload).

2. **Upload a CSV file:**

   - Click on the "Choose File" button and select a CSV file from your local system.
   - Ensure that the CSV file has the following columns: `Title`, `Authors`, `Publisher`, `Description`, `Publish Date`, and `Category`.
   - Click "Upload" to submit the file.

3. **Check the response:**

   After processing, you’ll receive a message indicating the time taken to process the file or any errors encountered.

### API Endpoints

- **POST /upload/**

  Uploads a CSV file containing book information. The expected CSV columns are:
  
  - `Title`: The title of the book
  - `Authors`: The authors of the book
  - `Publisher`: The publisher of the book
  - `Description`: A description of the book
  - `Publish Date`: The publication date of the book
  - `Category`: The category of the book

  **Request Format:**

  ```bash
  curl -X POST -F "file=@/path/to/your/file.csv" http://localhost:8000/upload/
  ```

  **Response:**

  - `200 OK` with a message detailing the processing time.
  - `400 Bad Request` with an error message if the file is missing, not a CSV, or if there's a processing error.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new feature branch:

   ```bash
   git checkout -b feature-branch
   ```

3. Commit your changes:

   ```bash
   git commit -am 'Add new feature'
   ```

4. Push to the branch:

   ```bash
   git push origin feature-branch
   ```

5. Create a Pull Request with a description of the changes.

## Contact

- **Author:** Amir Pandit
- **GitHub:** [github.com/username](https://github.com/AmirPandit)
```

Feel free to customize this template further based on additional details about your project or personal preferences. If you have any other questions or need more details, just let me know!
