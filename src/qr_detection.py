from qrdet import QRDetector
import cv2

def qr_detection(image):
    """
    Detect QR codes in an image and return the detected QR codes.

    Args:
        image_path (str): Path to the input image.

    Returns:
        list: List of detected QR codes.
    """
    # Initialize the QR detector
    qr_detector = QRDetector(model_size='s')

    # Read the image
    #image = cv2.imread(image_path)

    # Detect QR codes
    qr_codes = qr_detector.detect(image, is_bgr=True)

    return qr_codes

def draw_qr_codes(image, qr_codes):
    """
    Draw detected QR codes on the image.

    Args:
        image (numpy.ndarray): The input image.
        qr_codes (list): List of detected QR codes.

    Returns:
        numpy.ndarray: Image with drawn QR codes.
    """
    detections = qr_codes
    for detection in detections:
        # Extract bounding box coordinates
        x1_float, y1_float, x2_float, y2_float = detection['bbox_xyxy']

        # Convert coordinates to integers
        x1 = int(x1_float)
        y1 = int(y1_float)
        x2 = int(x2_float)
        y2 = int(y2_float)

        confidence = detection['confidence']

        # Draw the rectangle
        cv2.rectangle(image, (x1, y1), (x2, y2), color=(0, 255, 0), thickness=2)

        # Draw the text (also requires integer coordinates for the starting point)
        cv2.putText(image, f'{confidence:.2f}', (x1, y1 - 10), fontFace=cv2.FONT_HERSHEY_SIMPLEX,
                    fontScale=1, color=(0, 255, 0), thickness=2)
    return image
