# ChatGPT JSON Dataset Generator

This application allows you to generate a JSON dataset from ChatGPT conversations shared via a URL.

## Features

- Extracts ChatGPT conversation data from a shareable URL.
- Converts the extracted data into a JSON format.
- Provides a downloadable JSON file of the conversation data.

## How to Use

1. **Enter the ChatGPT Share URL:** Enter the URL of the ChatGPT conversation you want to scrape in the provided input field. Note that the URL must be a shareable link created from the ChatGPT conversation options.

2. **Generate Dataset:** Click the "Generate Dataset" button to start scraping. If the URL is valid, the conversation data will be displayed on the screen and a download button will appear to download the JSON file.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/streamlit_scraper.git
    cd streamlit_scraper
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Run the Streamlit app:**

    ```sh
    streamlit run app.py
    ```

## Files

- `app.py`: The main Streamlit app script.
- `scraper.py`: The script that contains the web scraping logic using Selenium.
- `requirements.txt`: The list of required Python packages.
- `.gitignore`: Git ignore file to exclude unnecessary files and directories.
- `README.md`: This file.

## Error Handling

- If the URL field is empty, an error message will be displayed: `Please paste URL to start.`
- If the URL does not have the required structure (`/share/`), an error message will be displayed: `Please create share link in conversation options.`

## Meta

- **Author:** Anthony Tatekawa
- **Description:** Generate a JSON dataset from ChatGPT conversations.
- **Keywords:** ChatGPT, JSON dataset generator, Streamlit app

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
