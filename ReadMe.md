# it-solutions-task
function converts text to mp4.

# Installation


# OpenCV
Option 1 - Main modules package: 
```pip install opencv-python```

Option 2 - Full package (contains both main modules and contrib/extra modules): 
```pip install opencv-contrib-python```

(check contrib/extra modules listing from OpenCV documentation)
b. Packages for server (headless) environments (such as Docker, cloud environments etc.), no GUI library dependencies

These packages are smaller than the two other packages above because they do not contain any GUI functionality (not compiled with Qt / other GUI components). This means that the packages avoid a heavy dependency chain to X11 libraries and you will have for example smaller Docker images as a result. You should always use these packages if you do not use cv2.imshow et al. or you are using some other package (such as PyQt) than OpenCV to create your GUI.

Option 3 - Headless main modules package: 
```pip install opencv-python-headless```

Option 4 - Headless full package (contains both main modules and contrib/extra modules): 
```pip install opencv-contrib-python-headless```

 (check contrib/extra modules listing from OpenCV documentation)

# Pillow
```pip install --upgrade Pillow```

# Running
```python main.py```