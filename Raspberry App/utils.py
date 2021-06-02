def load_image(frame, new_size=(300, 300)):
  # Get the dimensions
  height, width, _ = frame.shape # Image shape
  new_width, new_height = new_size # Target shape 

  # Calculate the target image coordinates
  left = (width - new_width) // 2
  top = (height - new_height) // 2
  right = (width + new_width) // 2
  bottom = (height + new_height) // 2
  
  image = frame[left:right, top:bottom, :]
  return image
