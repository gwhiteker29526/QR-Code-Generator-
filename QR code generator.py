import qrcode


def generate_qr_code(url: str, output_file: str = "output/qr_code.png") -> None:
    """
    Generates a QR code for the given URL.

    Args:
        url (str): The URL to encode in the QR code
        output_file (str): File path to save the generated QR code
    """

    # Create QR code object with configuration
    qr = qrcode.QRCode(
        version=1,  # Controls size of the QR code
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )

    # Add data to QR code
    qr.add_data(url)
    qr.make(fit=True)

    # Create image
    img = qr.make_image(fill_color="black", back_color="white")

    # Save image
    img.save(output_file)

    print("QR Code successfully generated!")
    print(f"Saved as: {output_file}")


if __name__ == "__main__":
    user_url = input("Enter a URL to generate a QR code: ")
    generate_qr_code(user_url)