This is a manual of how to run the models and the application

FOR THE models

The model notebooks should only be run on kaggle as that is where the dataset is located
If you want to re run the notebook ensure the TPU is enable otherwise training will take too long

To test the model all the code after history = model.fit and a csv file with the predictions will be generated in the output section on kaggle
Then submit the csv to the SIIM-ISIC Melanoma Classification competition.

Model-1 is a very basic model to get a baseline for the accuracy - the AUC SCORE obtained was - 0.5

Model-2 is a builds on model one and adds more augmentation features an a more complex cnn structure is added on top of the base model  - AUC Score obtaines was - 0.54

for both of the models above, cause of the class disparity inital bias was set to account for disparity but this was not helping improve the result

After furthure experiemting I tried a different loss function in final model - 4 called focal loss - it improve AUC score alot and I obtained - 0.79


For the APPLICATON 

For the applicaition to run make sure you download all the relevant librarires imported like numpy, pillow, tensorflow, streamlit etc... otherwise the applicaiton will not work

To run the application in the command line type "streamlit run main.py"








