# Flask URL Shortener

Flask URL Shortener is a simple web application built with Flask that allows users to shorten URLs.

## Features

- Shorten long URLs to more manageable and shareable links.
- Redirect users from shortened URLs to the original long URLs.
- Responsive design using Bootstrap for seamless experience across devices.
- Persistent storage of shortened URLs using SQLite database.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/kanagaraj3/urlShortner.git
    ```

2. Navigate into the project directory:

    ```bash
    cd urlShortner
    ```

3. Install the required dependencies using pip:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:

    ```bash
    python app.py
    ```

5. Access the application in your web browser at [http://localhost:5000](http://localhost:5000).

## Usage

1. Enter a long URL into the input field and click the "Shorten" button.
2. Copy the generated short URL and share it with others.
3. When users visit the short URL, they will be redirected to the original long URL.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them to your branch.
4. Push your changes to your fork.
5. Submit a pull request to the main repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
