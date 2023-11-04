### Searches for a target image on the screen and clicks on it if found. 

find_image(image_path, top_left=[0,0], bottom_right=[1080,1920])

### Args:

- image_path (str): File path to target image. 
- top_left (list, optional): Top left [x, y] of search region. Defaults to [0, 0].
- bottom_right (list, optional): Bottom right [x, y] of search region. Defaults to [1080, 1920].

### Returns:
 - None: Returns nothing if image is not found.

### Raises:
 - ValueError: If image_path is not provided.

