"""QR code reader"""
from qreader import QReader

def decode_qr_code(image):
    """Read and return the content of the QR code"""
    qr_reader = QReader()
    result = qr_reader.detect_and_decode(image)
    return result


def show_result(result):
    if result:
        print("QR Code detected:")
        print(result)
    else:
        print("No QR Code content found.")

