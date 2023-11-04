### Searches for a target color within a specified region of the screen and clicks on it at regular intervals.

AutoTrainerColor(target_color, x_offset=0, y_offset=0, search_interval=0, top_left=[0,0], bottom_right=[1080,1920])

#### Arguments

- `target_color` (tuple): RGB tuple of the target color to click on.
- `x_offset` (int, optional): Pixels to offset clicks in the x direction. Defaults to 0.
- `y_offset` (int, optional): Pixels to offset clicks in the y direction. Defaults to 0.
- `search_interval` (float, optional): Time interval between search attempts in seconds. Defaults to 0.
- `top_left` (list, optional): List of [x, y] representing the top-left corner of the search region. Defaults to [0, 0].
- `bottom_right` (list, optional): List of [x, y] representing the bottom-right corner of the search region. Defaults to [1080, 1920].

#### Returns

- `bool`: Returns `False` if the search is interrupted by a `KeyboardInterrupt` or a `pyautogui.FailSafeException`.

#### Raises

- `ValueError`: If the `target_color` argument is not passed or if your bottom_right values are bigger than your screen size.
