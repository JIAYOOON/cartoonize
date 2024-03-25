import cv2
import numpy as np

def cartoonize_video(input_video_path, output_video_path, cartoonize_function):
    # Open the video file
    video = cv2.VideoCapture(input_video_path)
    input_video_path = 'input_video.mp4'

    
    # Get video properties
    fps = int(video.get(cv2.CAP_PROP_FPS))
    width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    
    # Define the codec and create VideoWriter object
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))
    
    # Process each frame of the video
    while video.isOpened():
        ret, frame = video.read()
        if not ret:
            break
        
        # Apply cartoonize function to the frame
        cartoon_frame = cartoonize_function(frame)
        
        # Write the cartoonized frame to the output video
        out.write(cartoon_frame)
        
        # Display the cartoonized frame
        cv2.imshow('Cartoonized Video', cartoon_frame)
        
        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video objects
    video.release()
    out.release()
    cv2.destroyAllWindows()

# Define the function to cartoonize a single frame
def cartoonize_frame(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply median blur to reduce noise
    gray = cv2.medianBlur(gray, 5)
    
    # Detect edges using adaptive thresholding
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    
    # Convert the frame to color
    color = cv2.bilateralFilter(frame, 9, 300, 300)
    
    # Combine the color frame with the edges mask
    cartoon_frame = cv2.bitwise_and(color, color, mask=edges)
    
    return cartoon_frame

# Path to the input video
input_video_path = 'input_video.mp4'

# Path to save the output cartoonized video
output_video_path = 'output_cartoonized_video.avi'

# Cartoonize the input video
cartoonize_video(input_video_path, output_video_path, cartoonize_frame)
