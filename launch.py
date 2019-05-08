# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 15:35:05 2019

@author: LENOVO
"""

from convert import *
from train import *
#from translation import *

def trainer(x='') :
    
    
    if x == '' :
        
        x = input(' Enter the user to which conversion is to be made : \n AL. Abhilash\n AP. Aiswarya\n AM. Aravindan\n GK. Gautham\n C. Cancel\n : ')
        x = x.upper()
        
    
    if x in ['AL', 'AP', 'AM', 'GK'] :        
        
        
        lang = input(' Enter the language : \n en. Eng\n ml. Mal\n : ')
        
        if lang in ['en', 'ml'] :
            
            train_A_dir = './data/training/'+lang+'/SM'
            train_B_dir = './data/training/'+lang+'/'+x
            model_dir = './model/'+lang+'_SM_'+x
            model_name = 'SM_'+x+'.ckpt'
            random_seed = 0
            validation_A_dir = './data/validation/'+lang+'/'+'SM'
            validation_B_dir = './data/validation/'+lang+'/'+x
            output_dir = './validation_output/'+lang
            tensorboard_log_dir = './train_log/'+lang+'/'+'SM_'+x
            
            train(train_A_dir = train_A_dir, train_B_dir = train_B_dir, model_dir = model_dir, model_name = model_name, random_seed = random_seed, validation_A_dir = validation_A_dir, validation_B_dir = validation_B_dir, output_dir = output_dir, tensorboard_log_dir = tensorboard_log_dir)
    
        else :

            converter(x)
            
    else :
        
        choose()
            
        
def choose () :
    
    
    choice = input(' Enter the choice : \n 1. Train\n 2. Convert\n 3. Exit\n : ')
    
    if choice == '1' :
        
        #train_main()
        
        trainer()    
                
                
        
    elif choice == '2' :
        
        str_input1 = 'en'
        x = input(' Enter the user to which conversion is to be made : \n AL. Abhilash\n AP. Aiswarya\n AM. Aravindan\n GK. Gautham\n C. Cancel\n : ')
        x = x.upper()
        
        if x in ['AL', 'AP', 'AM', 'GK'] :        
            
            model_dir = './model/'+str_input1+'_SM_'+x
            model_name = 'SM_'+x+'.ckpt'
            data_dir = './data/evaluation/'+x
            conversion_direction = 'A2B'
            output_dir = './converted_voices/'+str_input1+'/'+x
            
            conversion(model_dir = model_dir, model_name = model_name, data_dir = data_dir, conversion_direction = conversion_direction, output_dir = output_dir)
        
        
        else :
            
            choose()
        
    elif choice == '3' :
        
        exit()
        
    else :
        
        print("Invalid choice ... Please try again...\n")
        choose()
        
choose()
    