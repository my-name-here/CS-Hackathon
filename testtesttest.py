import cv2
import numpy as np
import tensorflow as tf
#import os
import pyttsx3


# Load MobileNetV2 pre-trained model
model = tf.keras.applications.MobileNetV2(weights="imagenet")
engine = pyttsx3.init()
def speak_alert(message):
    engine.say(message)
    engine.runAndWait()
    #os.system(f"say {message}")


def detect_obstacles(frame):
    # Resize and preprocess frame
    resized_frame = cv2.resize(frame, (224, 224))
    img_array = tf.keras.preprocessing.image.img_to_array(resized_frame)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = tf.keras.applications.mobilenet_v2.preprocess_input(img_array)

    # Run the model
    predictions = model.predict(img_array)
    decoded_predictions = tf.keras.applications.mobilenet_v2.decode_predictions(predictions, top=3)
    
    obstacles = []
    for _, label, confidence in decoded_predictions[0]:
        if confidence > .5: # Use a confidence threshold to filter detections
            obstacles.append(label)

    return obstacles

def main():
    # Open camera
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = camera.read()
        if not ret:
            break
        
        # Detect obstacles
        obstacles = detect_obstacles(frame)
        if obstacles:
            print(obstacles)
            message = "Warning: " + ", obstacle" + " detected."
            speak_alert(message)
        
        # Display video feed
        cv2.imshow("Camera Feed", frame)
        
        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()