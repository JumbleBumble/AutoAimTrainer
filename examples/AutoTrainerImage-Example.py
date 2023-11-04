from library.AutoAimTrainer import AimTrainer as AutoAimTrainer #Assuming you have the library in a folder named library and named it AutoAimTrainer

  
y_min = 331
x_min = 567
y_max = 760
x_max = 1478
image = 'target.PNG'
AutoAimTrainer.AutoTrainerImage(image,0,[x_min,y_min],[x_max,y_max])

