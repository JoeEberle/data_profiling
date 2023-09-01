import ydata_profiling # provides descriptive statistics in html for any dataframe


def get_descriptive_statistics(df,data_set_name): 
    ''' the get_descriptive_statistics create a html page descriptive ststistics profile for any dataset passed to it.'''
    profile = ydata_profiling.ProfileReport(df)
    profile  
    data_profile_name = 'descriptive_statistics_profile.html'
    html_path = 'C:\\working_directory\\html\\'
    html_file_name =  html_path + data_set_name + data_profile_name
    profile.to_file(html_file_name)
    status = f'Outputting descriptive statistics profile to: {html_file_name}'
    print(status)
    return html_file_name

def display_descriptive_statistics(html_file_name):
    ''' the display_descriptive_statistics opens a new browser tab and displays html of a descriptive ststistics profile.'''    
    import  webbrowser 
    webbrowser.open_new_tab(html_file_name) 
    return f'Displaying {html_file_name} in web brower' 