# codeTantra_class_status_automation
# Selenium Web Scraping Automation with Twilio Integration

This Python script automates the process of checking the status of a meeting/class on MyClass LPU platform and sends a WhatsApp message using Twilio when the meeting has started.

## Prerequisites

Before running the script, ensure you have the following:

- Python installed on your system.
- Google Chrome browser installed.
- ChromeDriver installed and added to your system's PATH.
- Twilio account SID, auth token, and phone numbers (Twilio phone number and your phone number).

## Installation

1. Clone this repository to your local machine.
2. Install the required Python packages using pip:

pip install selenium twilio


## Configuration

Before running the script, update the following variables in the code with your Twilio account details:

- `TWILIO_ACCOUNT_SID`: Your Twilio account SID.
- `TWILIO_AUTH_TOKEN`: Your Twilio auth token.
- `TWILIO_PHONE_NUMBER`: Your Twilio phone number.
- `YOUR_PHONE_NUMBER`: Your phone number.

The script will continuously check the status of the meeting. Once the meeting has started, it will send a WhatsApp message to your specified phone number.

## Author

Kartik Sharma

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


