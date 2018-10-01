#This application runs the main windows and the experimenter window
#The software is repeating the first trial twice

import tkinter as tk

import time

import random

import csv


class Application(tk.Frame):
    # main application window
    def __init__(self, master=None):
        super().__init__(master)
        # set the attributes of the main window
        self.grid(column=0, row=0, sticky=('N', 'W', 'E', 'S'), padx=20, 
        pady=20)
        self.cicle = 0 #variable that will control the stimuli of the cicle
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        
        #building a list of trials from a csv file
        self.input_file = csv.reader(open("data.csv"), delimiter =';')
        self.all_trials =[]

        for row in self.input_file: #creates a list with all trials
            self.trial = {
            'trial': row[0],
            'sample' : row[1],
            'comp1' : row[2],
            'comp2' : row[3],
            }
            self.all_trials.append(self.trial)
        self.count_down_trials = len(self.all_trials) #number of trials based on number of rows in csv file
        self.trial_number = 0
        self.current_trial = self.all_trials[self.trial_number] #preparation for the loop
        
        self.create_widgets()

    def create_widgets(self):
        # creates set the widgets in the main window
        self.start = tk.Button(self, fg="green")
        self.start["text"] = "Start \nSession"
        self.start["command"] = self.open_window
        self.start["height"] = 4
        self.start["width"] = 8
        self.start.grid(column=2, row=7, sticky='W')

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=root.destroy)
        self.quit.grid(column=2, row=1, sticky='E')
        
        self.version = tk.Label(self, text='Version 1.0')
        self.version.grid(column=1, row=1, sticky=('N', 'W'))
        
        self.var = tk.IntVar(self)
        
        self.delay0 = tk.Radiobutton(self, value=0, variable=self.var)
        self.delay0["text"] = "Delay 0s"
        self.delay0.grid(column=1, row=2, sticky='W')
        
        self.delay2 = tk.Radiobutton(self, value=2000, variable=self.var)
        self.delay2["text"] = "Delay 2s"
        self.delay2.grid(column=1, row=3, sticky='W')
        
        self.delay5 = tk.Radiobutton(self, value=5000, variable=self.var)
        self.delay5["text"] = "Delay 5s"
        self.delay5.grid(column=1, row=4, sticky='W')
        
        self.delay10 = tk.Radiobutton(self, value=10000, variable=self.var)
        self.delay10["text"] = "Delay 10s"
        self.delay10.grid(column=1, row=5, sticky='W')
        
        self.delay20 = tk.Radiobutton(self, value=20000, variable=self.var)
        self.delay20["text"] = "Delay 20s"
        self.delay20.grid(column=1, row=6, sticky='W')
    
    def open_window(self):
        # creates the window the child will interact
        
        self.delay_option = self.var.get()
        
        self.user_window = tk.Toplevel(bg='white')
        self.user_window.attributes('-fullscreen', True)
                      
        self.frame_sample = tk.Frame(self.user_window, bg='white')
        self.frame_sample["height"] = 180
        self.frame_sample["width"] = 320
        self.frame_sample.grid(column=2, row=1, padx=60, pady = 150)
        
        self.frame_comparissons1 = tk.Frame(self.user_window, bg='white')
        self.frame_comparissons1["height"] = 180
        self.frame_comparissons1["width"] = 320
        self.frame_comparissons1.grid(column=1, row=2, padx=100)
        
        self.frame_comparissons2 = tk.Frame(self.user_window, bg='white')
        self.frame_comparissons2["height"] = 180
        self.frame_comparissons2["width"] = 320
        self.frame_comparissons2.grid(column=2, row=2, padx=100)
        
        self.frame_comparissons3 = tk.Frame(self.user_window, bg='white')
        self.frame_comparissons3["height"] = 180
        self.frame_comparissons3["width"] = 320
        self.frame_comparissons3.grid(column=3, row=2, padx=100)
        
        self.set_stimuli()
        self.log_header()
        
    def log_header(self):
        # put the session header in the log file
        self.logfile = 'log.txt'
        
        with open(self.logfile, 'a') as file_object:
            file_object.write('\n\n\n')
            file_object.write('=======================================')
            file_object.write(time.strftime("\n%c"))
            file_object.write('\n\nChoosen position and result:')
    
    def trial_control(self): #control the cicles
    
        self.bsample.grid_forget() #hides the sample for next trial
        self.bcompa1.grid_forget() #hides bcompa1 for next trial
        self.bcompa2.grid_forget() #hides bcompa2 for next trial
    
        if self.count_down_trials > 0:
            self.count_down_trials = self.count_down_trials - 1
            self.current_trial = self.all_trials[self.trial_number] #preparation for the loop
            print (self.current_trial) #important to know what trial is this
            #print (trial_number)
            self.trial_number = self.trial_number + 1
            
            self.after(5000, self.set_stimuli)
            
        else: root.destroy()
        
    def set_stimuli(self):
        self.bsample = tk.Button(self.frame_sample, relief='flat', bg='white')
        self.photo1 = tk.PhotoImage(file=self.current_trial['sample']) #set the image of sample
        self.bsample["command"] = self.hide_sample
        self.bsample.config(image=self.photo1, width="300", height="162")
        self.bsample.grid(column=2, row=1)
        
        self.bcompa1 = tk.Button(self.frame_comparissons1, bg='white')
        self.photo2 = tk.PhotoImage(file=self.current_trial['comp1']) #set the image of comp1
        self.bcompa1["command"] = self.mark_response_left
        self.bcompa1.config(image=self.photo2, width="300", height="162")
        
        
        self.bcompa2 = tk.Button(self.frame_comparissons3, bg='white')
        self.bcompa2["command"] = self.mark_response_right
        self.photo3 = tk.PhotoImage(file=self.current_trial['comp2']) #set the image of comp1
        self.bcompa2.config(image=self.photo3, width="300", height="162")
        
    def mark_response_left(self):
        
        if self.current_trial['sample'] == self.current_trial['comp1']:
            with open(self.logfile, 'a') as file_object:
                file_object.write('\nLEFT     correct')
                #file_object.write('\n')
        else:
            with open(self.logfile, 'a') as file_object:
                file_object.write('\nLEFT     incorrect')
                #file_object.write('\n')
            
        self.trial_control()
    
    def mark_response_right(self):
        
        if self.current_trial['sample'] == self.current_trial['comp2']:
            with open(self.logfile, 'a') as file_object:
                file_object.write('\nRIGHT     correct')
                #file_object.write('\n')
        else:
            with open(self.logfile, 'a') as file_object:
                file_object.write('\nRIGHT     incorrect')
                #file_object.write('\n')
            
        self.trial_control()
    
    def hide_sample(self):
        
        self.bsample.grid_forget() #hides the sample
        #print (self.delay_option)
        self.after(self.delay_option, self.show_comparissons) #show the comparissons after a presetted delay
        
    def show_comparissons(self):
        self.bcompa1.grid(column=2, row=2)
        self.bcompa2.grid(column=3, row=2)
        
         
        #self.log_header()
        #self.create_widgets_experimenter()

    #def cicle_ctrl(self):
        #while self.cicle < 5:
        
    #def set_schedule():
            

root = tk.Tk()
app = Application(master=root)
app.master.title('Delayed MTS')
app.mainloop()
