import qr_detection
import qr_decode
import cv2

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return
    confidence = 0.0  # Initialize confidence variable
    while True:
        # Activate the webcam and capture a frame
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break

        # Perform QR code detection
        qr_codes = qr_detection.qr_detection(frame)
        
        if qr_codes is None or len(qr_codes) == 0:
            print("No QR codes detected.")
            # No need for 'continue' here, just let it display the original frame
        else:
            print(f"Detected {len(qr_codes)} QR codes.")
            # Draw detected QR codes on the frame
            frame, confidence = qr_detection.draw_qr_codes(frame, qr_codes)
        
        if confidence > 0.8: 
            # Decode the QR code if confidence is high enough
            decoded_result = qr_decode.decode_qr_code(frame)
            if decoded_result:
                print(f"Decoded QR code: {decoded_result}")
            else:
                print("Failed to decode QR code.")

        # Display the frame (either original or with drawn QR codes)
        cv2.imshow("QR Code Detection", frame) # THIS IS THE CORRECT PLACEMENT

        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting...")
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()