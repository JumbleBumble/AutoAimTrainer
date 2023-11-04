#### Searches for a target color within a region of the screen and clicks on it.

find_color(target_color, step=1, x_offset=0, y_offset=0, interval=0, max_attempts=1, x_min=0, y_min=0, x_max=1080, y_max=1920)

#### Args:

- `target_color` (tuple): RGB tuple of the target color to click on.
- `step` (int, optional): Steps taken when scanning the region. Defaults to 1.  
- `x_offset` (int, optional): Pixels to offset clicks in x direction. Defaults to 0.
- `y_offset` (int, optional): Pixels to offset clicks in y direction.  Defaults to 0.  
- `interval` (float, optional): Time between attempts. Defaults to 0.
- `max_attempts` (int, optional): Maximum number of attempts. Defaults to 1. 
- `x_min` (int, optional): The minimum x value for the region. Defaults to 0.
- `y_min` (int, optional): The minimum y value for the region. Defaults to 0.
- `x_max` (int, optional): The maximum x value for the region. Defaults to 1080.  
- `y_max` (int, optional): The maximum y value for the region. Defaults to 1920.

#### Returns: 
 - `None`: Returns nothing if target not found after `max_attempts`.

#### Raises:
 - `ValueError`: If the `target_color` argument is not passed. Also raises a ValueError if it finds your `x_max` or `y_max` are bigger than your screen size after taking screenshot.

Scans the given region in steps, checking each pixel against the target 
color. If it finds it then it will click at the target offset by the `x_offset` and `y_offset `
values. Retries up to max_attempts times if not found initially.
