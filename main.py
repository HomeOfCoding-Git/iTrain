# iTrain Plot (version 0.0.1)
from tkinter import *
from tkinter import ttk
from time import ctime
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

app = Tk()

# App Name
app_name = 'iTrain'

# Window Defaults
bg_color = '#fff'
fg_color = '#296296'
default_font = 'Arial, 11'

# Plot Chart: Style
plt.style.use('seaborn')

# _________________________________________________________________
# Functions

# Clicked Item (discipline)
def clicked(event):
    global selected_item
    global clicked_second_item
    global combo_two_item
    global selected_jogging
    global selected_hiking
    global selected_cycling

    # Getter
    selected_item = clicked_item.get()

    # If discipline choose route options
    if selected_item == 'Jogging':
        clicked_second_item = StringVar()
        combo_two_item = ttk.Combobox(combo_frame, textvariable=clicked_second_item,
                          width=22, foreground=fg_color,
                          value=['Rossmore Hill', 'Park Jog'])
        combo_two_item.bind('<<ComboboxSelected>>', second_click)
        combo_two_item.set('Select..')
        combo_two_item.pack(side='left', padx=(5, 0), pady=(20, 5))
        
        selected_jogging = 1
        selected_hiking = 0
        selected_cycling = 0
        
    elif selected_item == 'Hiking':
        clicked_second_item = StringVar()
        combo_two_item = ttk.Combobox(combo_frame, textvariable=clicked_second_item,
                          width=22, foreground=fg_color,
                          value=['Carlton Hill', 'Park Hike', 'Pond Hike', 'Heath'])
        combo_two_item.bind('<<ComboboxSelected>>', second_click)
        combo_two_item.set('Select..')
        combo_two_item.pack(side='left', padx=(5, 0), pady=(20, 5))
        
        selected_jogging = 0
        selected_hiking = 1
        selected_cycling = 0
        
    elif selected_item == 'Cycling':
        clicked_second_item = StringVar()
        combo_two_item = ttk.Combobox(combo_frame, textvariable=clicked_second_item,
                          width=22, foreground=fg_color,
                          value=['Park Laps', 'Pond Sprint', 'Tally Ho',
                                 'Bushey Trail', 'Kent', 'Great Bull Run'])
        combo_two_item.bind('<<ComboboxSelected>>', second_click)
        combo_two_item.set('Select..')
        combo_two_item.pack(side='left', padx=(5, 0), pady=(20, 5))

        selected_jogging = 0
        selected_hiking = 0
        selected_cycling = 1
        
    else:
        output_box['text'] = 'Error: Not found!'


# Route
def second_click(event):
    global selected_item_two
    
    global rossmore_hill
    global park_jog
    global carlton_hill
    global park_hike
    global pond_hike
    global heath
    global park_laps
    global pond_sprint
    global tally_ho
    global bushey_trail
    global kent
    global great_bull_run
    
    global dist
    global plot_dist

    # Getter
    selected_item_two = clicked_second_item.get()

    # Setting the distance for each route
    if selected_item_two == 'Rossmore Hill':
        
        rossmore_hill = 1
        park_jog = 0
        carlton_hill = 0
        park_hike = 0
        pond_hike = 0
        heath = 0
        park_laps = 0
        pond_sprint = 0
        tally_ho = 0
        bushey_trail = 0
        kent = 0
        great_bull_run = 0
        
        dist = '1.5 Miles'
        plot_dist = 1.5
    
    elif selected_item_two == 'Park Jog':
        
        rossmore_hill = 0
        park_jog = 1
        carlton_hill = 0
        park_hike = 0
        pond_hike = 0
        heath = 0
        park_laps = 0
        pond_sprint = 0
        tally_ho = 0
        bushey_trail = 0
        kent = 0
        great_bull_run = 0
        
        dist = '2.7 Miles'
        plot_dist = 2.7
    
    elif selected_item_two == 'Carlton Hill':
        
        rossmore_hill = 0
        park_jog = 0
        carlton_hill = 1
        park_hike = 0
        pond_hike = 0
        heath = 0
        park_laps = 0
        pond_sprint = 0
        tally_ho = 0
        bushey_trail = 0
        kent = 0
        great_bull_run = 0
        
        dist = '2.4 Miles'
        plot_dist = 2.4
    
    elif selected_item_two == 'Park Hike':
        
        rossmore_hill = 0
        park_jog = 0
        carlton_hill = 0
        park_hike = 1
        pond_hike = 0
        heath = 0
        park_laps = 0
        pond_sprint = 0
        tally_ho = 0
        bushey_trail = 0
        kent = 0
        great_bull_run = 0
        
        dist = '4 Miles'
        plot_dist = 4.0
    
    elif selected_item_two == 'Pond Hike':
        
        rossmore_hill = 0
        park_jog = 0
        carlton_hill = 0
        park_hike = 0
        pond_hike = 1
        heath = 0
        park_laps = 0
        pond_sprint = 0
        tally_ho = 0
        bushey_trail = 0
        kent = 0
        great_bull_run = 0
        
        dist = '7 Miles'
        plot_dist = 7.0
    
    elif selected_item_two == 'Heath':
        
        rossmore_hill = 0
        park_jog = 0
        carlton_hill = 0
        park_hike = 0
        pond_hike = 0
        heath = 1
        park_laps = 0
        pond_sprint = 0
        tally_ho = 0
        bushey_trail = 0
        kent = 0
        great_bull_run = 0
        
        dist = '10 Miles'
        plot_dist = 10.0
    
    elif selected_item_two == 'Park Laps':
        
        rossmore_hill = 0
        park_jog = 0
        carlton_hill = 0
        park_hike = 0
        pond_hike = 0
        heath = 0
        park_laps = 1
        pond_sprint = 0
        tally_ho = 0
        bushey_trail = 0
        kent = 0
        great_bull_run = 0
        
        dist = '10 Miles'
        plot_dist = 10.0
    
    elif selected_item_two == 'Pond Sprint':
        
        rossmore_hill = 0
        park_jog = 0
        carlton_hill = 0
        park_hike = 0
        pond_hike = 0
        heath = 0
        park_laps = 0
        pond_sprint = 1
        tally_ho = 0
        bushey_trail = 0
        kent = 0
        great_bull_run = 0
        
        dist = '6 Miles'
        plot_dist = 6.0
    
    elif selected_item_two == 'Tally Ho':
        
        rossmore_hill = 0
        park_jog = 0
        carlton_hill = 0
        park_hike = 0
        pond_hike = 0
        heath = 0
        park_laps = 0
        pond_sprint = 0
        tally_ho = 1
        bushey_trail = 0
        kent = 0
        great_bull_run = 0
        
        dist = '18 Miles'
        plot_dist = 18.0
    
    elif selected_item_two == 'Bushey Trail':
        
        rossmore_hill = 0
        park_jog = 0
        carlton_hill = 0
        park_hike = 0
        pond_hike = 0
        heath = 0
        park_laps = 0
        pond_sprint = 0
        tally_ho = 0
        bushey_trail = 1
        kent = 0
        great_bull_run = 0
        
        dist = '30 Miles'
        plot_dist = 30.0
    
    elif selected_item_two == 'Kent':
        
        rossmore_hill = 0
        park_jog = 0
        carlton_hill = 0
        park_hike = 0
        pond_hike = 0
        heath = 0
        park_laps = 0
        pond_sprint = 0
        tally_ho = 0
        bushey_trail = 0
        kent = 1
        great_bull_run = 0
        
        dist = '30 Miles'
        plot_dist = 30.0
    
    elif selected_item_two == 'Great Bull Run':
        
        rossmore_hill = 0
        park_jog = 0
        carlton_hill = 0
        park_hike = 0
        pond_hike = 0
        heath = 0
        park_laps = 0
        pond_sprint = 0
        tally_ho = 0
        bushey_trail = 0
        kent = 0
        great_bull_run = 1
        
        dist = '47 Miles'
        plot_dist = 47.0
    
    else:
        pass


# Time Duration (Hour)
def clicked_hour(event):
    global get_hours
    
    get_hours = select_hour.get()


# Time Duration (Minutes)
def clicked_mins(event):
    global get_mins
    
    get_mins = select_mins.get()

    try:
        # Exercise duration
        duration = get_hours + ':' + get_mins

        # File Path: Write Record Log Data
        # Note: There is no dot extention..
        # Example: .txt
        # However, you can add an extention if you prefer
        filename = 'Logs/Records'

        # Write exercise log data to file
        with open(filename, 'a') as f_append:
            f_append.write('_____________________________\n\n' \
                           f'Logged: {ctime()}\n\n' \
                           f'Discipline: {selected_item}\n' \
                           f'Route: {selected_item_two}\n' \
                           f'Distance: {dist} \n' \
                           f'Duration: {duration} \n')


        # File Path: Write Record Log Data to (csv file)
        file_name = 'CSV/ex_chart.csv'
        
        # Write exercise log data to file
        with open(file_name, 'a') as f_append:
            f_append.write(selected_item + ',' + \
                           str(selected_jogging) + ',' + \
                           str(selected_hiking) + ',' + \
                           str(selected_cycling) + ',' + \
                           selected_item_two + ',' + \
                           str(rossmore_hill) + ',' + \
                           str(park_jog) + ',' + \
                           str(carlton_hill) + ',' + \
                           str(park_hike) + ',' + \
                           str(pond_hike) + ',' + \
                           str(heath) + ',' + \
                           str(park_laps) + ',' + \
                           str(pond_sprint) + ',' + \
                           str(tally_ho) + ',' + \
                           str(bushey_trail) + ',' + \
                           str(kent) + ',' + \
                           str(great_bull_run) + ',' + \
                           str(plot_dist) + ',' + duration + '\n')


    except:
        pass

    # Back to defaults
    combo_two_item.destroy()
    combo_hour.set('Hours 00:')
    combo_mins.set(' :00 Mins ')
    combo_item.set('Select..')
    # Go to function
    show_log_data()
    refresh_plot()


# Display Exercise Logs (log_box)
def show_log_data():

    log_box.delete(1.0, END)

    # From File Path: Read Record Log Data
    file_log = 'Logs/Records'

    with open(file_log, 'r') as f_read:
        show_log = f_read.read()


    # Display Record Log Data on Screen
    log_box.insert(END, show_log)
    # Remove focus from combo box..
    # Put focus somewhere else. (cursor blinker)
    header_frame.focus()


def refresh_plot():

    # Append Data for Plot (to csv file)
    data = pd.read_csv('CSV/ex_chart.csv')

    # Discipline
    discipline = data['Discipline']
    jogging = data['Jogging']
    hiking = data['Hiking']
    cycling = data['Cycling']
    # Jogging
    rossmore_hill = data['Rossmore Hill']
    park_jog = data['Park Jog']
    # Hiking
    carlton_hill = data['Carlton Hill']
    park_hike = data['Park Hike']
    pond_hike = data['Pond Hike']
    heath = data['Heath']
    # Cycling
    park_laps = data['Park Laps']
    pond_sprint = data['Pond Sprint']
    tally_ho = data['Tally Ho']
    bushey_trail = data['Bushey Trail']
    kent = data['Kent']
    great_bull_run = data['Great Bull Run']
    # Distance and Duration
    distance = data['Distance']
    duration = data['Duration']

    # Create Graph
    fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
    ax1.bar(duration, distance)
    ax2.bar(distance, duration)

    ax1.plot(duration, distance, color='purple', linestyle='--', label='Duration')
    ax2.plot(distance, duration, color='orange', linestyle='--', label='Distance')

    ax1.legend(loc='upper left')
    ax1.set_title('Exercise Chart')
    ax1.set_ylabel('Duration')
    ax1.set_xlabel('Distance')


    ax2.legend(loc='upper left')
    ax2.set_ylabel('Distance')
    ax2.set_xlabel('Duration')

    # Load Graph into Tkinter
    chart = FigureCanvasTkAgg(fig, chart_frame)
    chart.get_tk_widget().pack(padx=(0, 50), ipady=20)



# Window
# _________________________________________________________________
# Header

# Header Frame (for label)
header_frame = Frame(app, bg=fg_color)
header_frame.pack(fill='x')

# Header Image
header_img = PhotoImage(file = 'img/iTrain.png')
header_label = Label(header_frame, image=header_img, bg=fg_color, border=0)
header_label.pack(side='left', padx=(26, 0), pady=20)

left_frame = Frame(app, bg=bg_color)
left_frame.pack(side='left')

# _________________________________________________________________
# Discipline (choose option from combo box)

# Combo Frame (for combo box)
combo_frame = Frame(left_frame, bg=bg_color)
combo_frame.pack(fill='x', padx=20)

# Combo Selection Label
combo_label = Label(combo_frame, text='Discipline:',
                    bg=bg_color, fg=fg_color, font=default_font)
combo_label.pack(side='left', pady=(20, 5))

# Combo Box Getter
clicked_item = StringVar()
# Options List
options = ['Jogging', 'Hiking', 'Cycling']

# Combo Box Widget
combo_item = ttk.Combobox(combo_frame, textvariable=clicked_item, \
                          width=22, foreground=fg_color, value=options)
combo_item.bind('<<ComboboxSelected>>', clicked)
combo_item.set('Select..')
combo_item.pack(side='left', padx=(4, 0), pady=(20, 5))

# _________________________________________________________________
# Duration (time taken to finish exercise)

# Duration Combo Frame (combo box for time)
time_frame = Frame(left_frame, bg=bg_color)
time_frame.pack(fill='x', padx=20)

# Duration Selection Label
time_label = Label(time_frame, text='Duration:',
                    bg=bg_color, fg=fg_color, font=default_font)
time_label.pack(side='left', pady=(20, 5))

# Combo Box Getter
select_hour = StringVar()
select_mins = StringVar()

# Options List
hours = ['00', '01', '02', '03', '04', '05', '06']
mins = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10', \
        '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', \
        '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', \
        '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', \
        '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', \
        '53', '54', '55', '56', '57', '58', '59']

# Hours Combobox for: Options List (value=hours)
combo_hour = ttk.Combobox(time_frame, textvariable=select_hour,
                          width=9, justify='center', foreground=fg_color, value=hours)
combo_hour.bind('<<ComboboxSelected>>', clicked_hour)
combo_hour.set('Hours 00:')
combo_hour.pack(side='left', padx=(12, 0), pady=(20, 5))

# Minutes Combobox for: Options List (value=mins)
combo_mins = ttk.Combobox(time_frame, textvariable=select_mins,
                          width=9, justify='center', foreground=fg_color, value=mins)
combo_mins.bind('<<ComboboxSelected>>', clicked_mins)
combo_mins.set(':00 Mins')
combo_mins.pack(side='left', padx=0, pady=(20, 5))

# _________________________________________________________________
# Plot Frame (for chart)
chart_frame = Frame(app, bg=bg_color)
chart_frame.pack(fill='both')

# _________________________________________________________________
# Output: Label (errors) / Text (exercise logs)

# Error Output Frame
output_frame = Frame(left_frame, bg=bg_color)
output_frame.pack(fill='x', padx=20)

# Output: Label (for error message)
output_box = Label(output_frame, bg=bg_color, fg='red', font=default_font)
output_box.pack(pady=5)

# Log Frame
log_frame = Frame(left_frame, bg=bg_color)
log_frame.pack()

# Output: Exercise Logs (Text Widget)
log_box = Text(log_frame, wrap=WORD, bg=bg_color, fg=fg_color, \
               font=default_font, border=0)
log_box.pack(padx=(96, 0), pady=20, expand=True)

if __name__ == '__main__':

    show_log_data()
    refresh_plot()

    app.title(app_name)
    app.geometry('500x600+0-33')
    app.configure(bg=bg_color)
    app.mainloop()
