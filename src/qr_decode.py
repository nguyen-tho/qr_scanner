"""QR code reader"""
from qreader import QReader

def decode_qr_code(image):
    """Read and return the content of the QR code"""
    qr_reader = QReader()
    result = qr_reader.detect_and_decode(image)
    return result
