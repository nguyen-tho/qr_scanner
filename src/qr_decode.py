from qreader import QReader

def decode_qr_code(image):
    qr_reader = QReader()
    result = qr_reader.detect_and_decode(image)
    return result