import csv


input_file = csv.reader(open("data.csv"), delimiter =';')

#trial_one = { 'trial': row[0]}

#print (trial_one)
all_trials =[]

for row in input_file: #creates a list with all trials
      
    trial = {
    'trial': row[0],
    'sample' : row[1],
    'comp1' : row[2],
    'comp2' : row[3],
    }
    
    all_trials.append(trial)

count_down_trials = len(all_trials)
#print (count_down_trials)
#print (trial)
#print (all_trials)

trial_number = 0
current_trial = all_trials[trial_number] #preparation for the loop


while count_down_trials > 0: #this iteration runs through all trials
    count_down_trials = count_down_trials - 1
    current_trial = all_trials[trial_number] #preparation for the loop
    print (current_trial) #important to know what trial is this
    #print (trial_number)
    trial_number = trial_number + 1
    


