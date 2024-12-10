# dailybait 📰

dailybait is an app that generates a clickbait-style news headline every day, answering simple, attention-grabbing questions with short, punchy answers. Using FastAPI and the OpenAI API, it delivers a new headline daily with creativity and flair.

## Features

- **Daily Updates:** Automatically generates a unique clickbait headline every day.  (This is the goal at least!)
- **FastAPI Backend:** Lightweight and efficient API for fetching the latest headline.  
- **AI-Powered:** Uses OpenAI API for creative ideas generation.  
- **Minimalistic Design:** Focused solely on generating and serving engaging headlines.

## Getting Started

### Prerequisites
- Python 3.9+
- FastAPI  
- OpenAI API key  

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/DailyBait.git
   cd DailyBait
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up your environment variables:
   - Add your OpenAI API key as an environment variable:
     ```bash
     export OPENAI_API_KEY=your_api_key
     ```

4. Run the app:
   ```bash
   uvicorn app.main:app --reload
   ```

### Usage
- Access the API locally at `http://127.0.0.1:8000/`.
- Example endpoint:
  - `/headline` - Fetches the latest generated headline.

### Example Output
**Headline:**  
*What does skipping breakfast do to your brain?*  
**Answer:**  
*Nothing.*

## Contributing
Feel free to submit issues or pull requests. _Most_ contributions are welcome!

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.
