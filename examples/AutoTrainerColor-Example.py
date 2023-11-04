from library import AutoAimTrainer #Assuming you have the library in a folder named library and named it AutoAimTrainer

target_color = (255,0,0)          
y_min = 331
x_min = 567
y_max = 760
x_max = 1478
AutoAimTrainer.AutoTrainerColor(target_color, top_left=[x_min, y_min], bottom_right=[x_max, y_max])