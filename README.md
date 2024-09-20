# CSV Upload and Book Management System

This Django-based application allows users to upload CSV files containing book details, storing the information in a database. It also features a REST API for handling the upload and a basic HTML interface for file submission.

## Contents

- [Setup](#setup)
- [How It Works](#how-it-works)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)
- [Contact Information](#contact-information)

## Setup

To get started, follow these instructions:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/AmirPandit/CSV-HANDLE-DJANGO.git
   ```

2. **Enter the project directory:**

   ```bash
   cd populatedata
   ```

3. **Set up a virtual environment (recommended):**

   - **Windows:**

     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

   - **macOS/Linux:**

     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. **Install the necessary dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

5. **Apply database migrations:**

   ```bash
   python manage.py migrate
   ```

6. **Start the local development server:**

   ```bash
   python manage.py runserver
   ```

## How It Works

### Uploading CSV Files

1. **Access the upload page:**

   Open a browser and navigate to [http://localhost:8000/upload](http://localhost:8000/upload).

2. **Submit a CSV file:**

   - Click "Choose File" to select a CSV file from your device.
   - Ensure the CSV includes columns for `Title`, `Authors`, `Publisher`, `Description`, `Publish Date`, and `Category`.
   - Click "Upload" to submit the file.

3. **Check the response:**

   After uploading, you'll receive feedback on processing success or any encountered issues.

### API Endpoints

- **POST /upload/**

  Use this endpoint to upload a CSV file with book details. The CSV should include:
  
  - `Title`: Name of the book
  - `Authors`: Book authors
  - `Publisher`: Book publisher
  - `Description`: Brief description of the book
  - `Publish Date`: Date the book was published
  - `Category`: Genre or category of the book

  **Sample Request:**

  ```bash
  curl -X POST -F "file=@/path/to/your/file.csv" http://localhost:8000/upload/
  ```

  **Possible Responses:**

  - `200 OK` with details about the upload process.
  - `400 Bad Request` if the file is missing, not a CSV, or processing fails.

## Contributing

If you'd like to contribute, follow these steps:

1. Fork the repository.
2. Create a new branch for your feature:

   ```bash
   git checkout -b feature-branch
   ```

3. Make your changes and commit:

   ```bash
   git commit -am 'Add new feature'
   ```

4. Push the branch to GitHub:

   ```bash
   git push origin feature-branch
   ```

5. Submit a Pull Request with a description of your changes.

## Contact Information

- **Author:** Amir Pandit
- **GitHub:** [AmirPandit](https://github.com/AmirPandit)

Let me know if you'd like further adjustments!
