# Vehicle Suggestion System

This project aims to provide vehicle recommendations using unsupervised learning via clustering. It is built with
Python, Flask, and scikit-learn.

## Project Structure

- **app.py**: Main application file that includes the Flask API for vehicle recommendations.
- **generate_vehicles.py**: Script to generate a dataset of vehicles.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Yassim-B/deep-vehicle-suggest.git
    cd VehicleSuggestionSystem
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

4. Generate the dataset:
    ```sh
    python generate_vehicles.py
    ```

## Running the Application

1. Start the Flask application:
    ```sh
    python app.py
    ```

2. The API will be available at `http://127.0.0.1:5000/`.

## API Endpoints

- **GET /coucou**: Test endpoint to check if the API is running.
    - Example:
        ```sh
        curl http://127.0.0.1:5000/coucou
        ```

- **POST /recommander**: Endpoint to get vehicle recommendations based on user input.
    - Request body example (JSON):
        ```json
        {
            "sieges": 5,
            "consommation": 8.5,
            "prix": 30000,
            "design": 4,
            "kilometrage_maxi": 50000,
            "motorisation": "Essence"
        }
        ```
    - Response example:
        ```json
        {
            "count": 50,
            "vehicles": [
                {
                    "Marque": "Toyota",
                    "Modele": "Corolla",
                    "Sieges": 5,
                    "Consommation": 8.0,
                    "Prix": 25000,
                    "Design": 4.5,
                    "Motorisation": "Essence",
                    "Kilometrage": 45000,
                    "Distance": 0.12345
                },
                ...
            ]
        }
        ```

## Explanation

### app.py

The `app.py` file contains the main Flask application which handles the following:

1. **Data Loading and Preprocessing**:
    - Loads vehicle data from `vehicles.csv`.
    - Fills missing values with the mean of their respective columns.
    - Encodes the categorical variable `Motorisation` using `LabelEncoder`.
    - Standardizes numerical features.

2. **KMeans Clustering**:
    - Trains a KMeans model with 5 clusters using the preprocessed data.

3. **Vehicle Recommendation**:
    - Defines a function to find the nearest vehicles to the user's preferences using Euclidean distances.
    - Provides an endpoint `/recommander` to get recommendations.

### generate_vehicles.py

The `generate_vehicles.py` script generates a synthetic dataset of 1000 vehicles with random attributes and saves it
as `vehicles.csv`.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements.
