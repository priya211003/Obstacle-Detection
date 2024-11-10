import cv2
import numpy as np

# Set parameters for danger distance threshold (adjust these based on camera and environment setup)
DANGER_DISTANCE_THRESHOLD = 50  # Threshold distance (in arbitrary units)
SAFE_DISTANCE_THRESHOLD = 150  # Maximum safe distance threshold

# Function to estimate distance (placeholder - replace with actual depth calculation logic as needed)
def estimate_distance(contour):
    # Basic assumption: larger contours = closer objects. Adjust scaling based on calibration.
    _, _, w, h = cv2.boundingRect(contour)
    distance = 1000 / (w * h)  # Inverse of area as a proxy for distance
    return distance

# Initialize camera
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale and apply Gaussian blur
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Apply edge detection
    edges = cv2.Canny(blurred, 50, 150)

    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    for contour in contours:
        # Ignore small contours to reduce noise
        if cv2.contourArea(contour) < 500:
            continue

        # Calculate distance to obstacle
        distance = estimate_distance(contour)
        
        # Set label based on distance
        if distance < DANGER_DISTANCE_THRESHOLD:
            label = "Highly Dangerous"
            color = (0, 0, 255)  # Red color for dangerous
        elif distance < SAFE_DISTANCE_THRESHOLD:
            label = "Less Dangerous"
            color = (0, 255, 255)  # Yellow color for less dangerous
        else:
            label = "Safe"
            color = (0, 255, 0)  # Green color for safe distance
            
        # Draw contour and label on the frame
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)
        cv2.putText(frame, f"{label} - {distance:.2f} units", (x, y - 10), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        
        # Print the distance of the obstacle
        print(f"Obstacle detected at distance: {distance:.2f} units, Label: {label}")

    # Display the output frame
    cv2.imshow("Obstacle Detection", frame)

    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the capture and close windows
cap.release()
cv2.destroyAllWindows()
