# QR Code Generator – Biox Systems

## Project Description

This project is a Python-based QR Code Generator developed for Biox Systems.
The application generates a QR (Quick Response) code from a user-provided URL and saves it as an image file. QR codes are a two-dimensional, machine-readable representation of information and were invented in 1994 by Denso Wave.

---

## Features

* Accepts a URL as user input
* Generates a QR code based on the provided URL
* Saves the QR code as a PNG image
* Simple command-line interface
* Uses Python best practices and clear code documentation

---

## Technologies Used

* Python 3.x
* qrcode library
* Pillow (image processing)
* PyCharm IDE
* GitHub for version control

---

## Installation Instructions

1. Install Python 3.x from [https://www.python.org](https://www.python.org)
2. Clone this repository or download the source code
3. Open the project in PyCharm or any Python IDE
4. Install dependencies using:

   ```bash
   pip install -r requirements.txt
   ```

---

## How to Run the Application

1. Navigate to the project directory
2. Run the program:

   ```bash
   python QR_code_generator.py
   ```
3. Enter a valid URL when prompted
4. The QR code image will be saved in the `output` folder

---

## Example Output

After entering a URL such as:

```
https://www.bioxsystems.com
```

A QR code image (`qr_code.png`) is generated and stored in the `output` directory.

---

## Project Structure

```
PythonProject13/
│
├── QR_code_generator.py
├── requirements.txt
├── README.md
└── output/
    └── qr_code.png
```

---

## Author
Garrett Whiteker
Biox Systems

---

## License

This project is for educational purposes only.
