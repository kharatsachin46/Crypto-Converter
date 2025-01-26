# Cryptocurrency Converter

A real-time cryptocurrency converter that uses the CoinGecko API to provide up-to-date conversion rates between various cryptocurrencies and fiat currencies.

## Features

- Real-time cryptocurrency price data from CoinGecko API
- Support for multiple cryptocurrencies
- Support for multiple fiat currencies
- Clean and modern user interface
- Responsive design for mobile and desktop
- No API key required

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd crypto_converter
```

2. Create a virtual environment and activate it:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Start the Flask application:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Select your desired cryptocurrency, enter the amount, and choose the target currency for conversion.

## Technologies Used

- Backend: Python, Flask
- Frontend: HTML, CSS, JavaScript
- API: CoinGecko API
- Styling: Custom CSS with modern design principles

## API Reference

This application uses the CoinGecko API v3. The following endpoints are used:

- `/simple/supported_vs_currencies`: Get list of supported currencies
- `/coins/list`: Get list of supported cryptocurrencies
- `/simple/price`: Get current price of cryptocurrencies

## Contributing

Feel free to submit issues and enhancement requests!
