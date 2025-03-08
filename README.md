# Crime Prediction Project

This project is a Django-based web application for predicting crime rates in different areas.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/crime_prediction.git
    cd crime_prediction
    ```

2. Create and activate a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Project

1. Apply the migrations:
    ```bash
    python manage.py migrate
    ```


3. Run the development server:
    ```bash
    python manage.py runserver
    ```

4. Open your web browser and go to `http://127.0.0.1:8000/` to access the application.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please read the [CONTRIBUTING](CONTRIBUTING.md) file for guidelines on how to contribute to this project.



## Accessing the Admin Side

To access the admin side of the application, use the following credentials:

- **Username:** root
- **Password:** root

Navigate to `http://127.0.0.1:8000/admin/` in your web browser and log in with the above credentials.