If you wanna use this particular code then follow the particular steps

1. You can go for anaconda or python , but most preferable is anaconda (Jupyter Notebook)    
2. Create a folder names as Images with subfolders of all alphabets and digits
3. copy collectdata.py and run it to save your images into a file named as Images 
4. Capture a few images and save them
5. copy and run function.py to run all the necessary functions which will create points on hand to track them 
6. copy and run data.py to save the end points of your hand and save thema as npy format for each alphabet
7. Copy and run trainmodel.py to run the model and train your model
8. If you want you can change the epoch size in a range of 200 and 500
9. A new file will be automatically saved model.h5 where your model will be saved
10. If your accuracy is greater than 0.8 then go ahead
11. Copy and run app.py to run the final code as required
    
Requirements 
1. tensorflow
2. mediapipe
3. opencv-python
4. scikit-learn

If you are using anaconda , Python 3.12 should be the supported version as there are many changes in the latest verion which could interfear with the code and the error might not be resolved ,  try uninstalling anaconda and download the latest version  
<Br>
The current version of anaconda which i am using is "conda 24.11.3"

Shortcut To Create Multiple Folders At once 
<br>
for %i in (A B C D E F G H I J K L M N O P Q R S T U V W X Y Z 0 1 2 3 4 5 6 7 8 9) do mkdir %i
<br>
copy the above command and past it in the cmd of the location you want to create these multiple folders at once
