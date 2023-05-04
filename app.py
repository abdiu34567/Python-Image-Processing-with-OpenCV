from image_processing import show_image, apply_filter, resize_image, detect_faces, extract_channels

img = 'im2.jpg'
# Show an image
show_image(img)

# Apply a filter to an image
apply_filter(img)

# Resize an image
resized_img = resize_image(img, 500, 500)

# Detect faces in an image
detect_faces(img)

extract_channels(img)
