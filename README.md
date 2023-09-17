# Text-to-Speech (TTS) API with FastAPI

This is a simple API built using FastAPI that provides text-to-speech (TTS) functionality. It takes a text input and an optional language parameter, translates the text into the specified language (or Hindi by default), converts it to speech, and plays the speech as an audio file.

## Features

- Convert text to speech in different languages.
- Supports translation of text to the target language.
- Adjustable speech speed.
- Cross-origin resource sharing (CORS) enabled for web applications.

## Endpoints

### 1. `/speak` (GET)

- **Description:** A simple GET endpoint to check if the API is running.
- **Usage:** Visit `http://your-api-url/speak` to get a "Hello from /speak GET endpoint" message.

### 2. `/speak` (POST)

- **Description:** Converts the provided text to speech and plays it.
- **Usage:** Send a POST request to `http://your-api-url/speak` with a JSON body containing the text you want to convert to speech and an optional language parameter (default is English).
- **Example Request Body:**
  ```json
  {
      "text": "Hello, world!",
      "lang": "es"
  }
  ```
- **Response:** The API will respond with a success message after playing the speech.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   ```

2. Change into the project directory:

   ```bash
   cd your-repo
   ```

3. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

4. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the FastAPI application:

   ```bash
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

## Usage

- To use the API, make POST requests to `http://your-api-url/speak` with the text you want to convert to speech and an optional language parameter.

- You can also test the API by visiting `http://your-api-url/speak` in your web browser to check if it's running.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- This project utilizes the following libraries:
  - FastAPI
  - Pydantic
  - SpeechRecognition
  - Googletrans
  - gTTS (Google Text-to-Speech)
  - Pygame

Feel free to contribute to or modify this project as needed. If you encounter any issues or have suggestions for improvements, please open an issue on GitHub.

Enjoy using the Text-to-Speech API!
