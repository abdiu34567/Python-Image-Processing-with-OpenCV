import cv2
import numpy as np


def show_image(myfile):
    # Load an image file
    img = cv2.imread(myfile)

    # Display the image
    cv2.imshow('Image', img)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()


def apply_filter(file):
    # Load an image file
    img = cv2.imread(file)

    # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply a Gaussian blur filter
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # Display the filtered image
    cv2.imshow('Filtered Image', blurred)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()


def resize_image(file, width, height):
    # Load an image file
    img = cv2.imread(file)

    # Resize the image
    resized = cv2.resize(img, (width, height))

    # Display the resized image
    cv2.imshow('Resized Image', resized)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()


def detect_faces(file):
    # Load an image file
    img = cv2.imread(file)

    # Load the face detection classifier
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

    # Detect faces in the image
    faces = face_cascade.detectMultiScale(
        img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the image with faces detected
    cv2.imshow('Faces Detected', img)
    cv2.waitKey(4000)
    cv2.destroyAllWindows()


def apply_sepia_filter(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Apply sepia filter
    kernel = np.array([[0.393, 0.769, 0.189],
                       [0.349, 0.686, 0.168],
                       [0.272, 0.534, 0.131]])
    sepia_img = cv2.transform(img, kernel)

    # Display the filtered image
    cv2.imshow('Sepia Filter', sepia_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def apply_grayscale_filter(image_path):
    # Load the image
    img = cv2.imread(image_path)

    # Apply grayscale filter
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Display the filtered image
    cv2.imshow('Grayscale Filter', gray_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def apply_edge_detection(image_path, threshold1=100, threshold2=200):
    # Load the image
    img = cv2.imread(image_path)

    # Apply Canny edge detection
    edges = cv2.Canny(img, threshold1, threshold2)

    # Display the edge detection result
    cv2.imshow('Canny Edge Detection', edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def extract_channels(file):
    # Load an image file
    img = cv2.imread(file)

    # Split the image into color channels
    blue, green, red = cv2.split(img)

    # Create a new image by merging the color channels
    height, width = img.shape[:2]
    channel_image = np.zeros((height, width * 3, 3), dtype=np.uint8)
    channel_image[:, :width] = cv2.merge(
        [blue, np.zeros_like(blue), np.zeros_like(blue)])
    channel_image[:, width:width *
                  2] = cv2.merge([np.zeros_like(green), green, np.zeros_like(green)])
    channel_image[:, width *
                  2:] = cv2.merge([np.zeros_like(red), np.zeros_like(red), red])

    # Display the extracted color channels
    cv2.imshow('Extracted Channels', channel_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
