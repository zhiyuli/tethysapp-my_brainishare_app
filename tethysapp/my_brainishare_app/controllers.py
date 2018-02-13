from django.shortcuts import render  # import Django built-in module
import subprocess  # import Python built-in module
import requests  # import 3rd party python module/lib


def home(request):
    """
    Controller for the app home page.
    Once user visits url http://Tethys_Server_Domain/apps/my-brainishare-app/,  this home controller function gets executed.
    This linkage is defined in file app.py Line 27-31 and is called URL Mapping (map a url to a python function)

    User can pass in parameters by appending query strings (&NAME1=VALUE1&NAME2=VALUE2) to url,
    like:   http://Tethys_Server_Domain/apps/my-brainishare-app/?res_id=123456&script_name=myscript
    """

    ################# Receive parameters encoded in url (read user inputs) #######################
    # Get the BrianIShare resource id from url (&res_id=XXXXXXXXXX)
    res_id = request.GET.get("res_id", "Parameter 'res_id' does not exist in url")


    ################## Do something here (your business)#####################
    # Call an external executable/command/script (located on this Tethys server) using Python built-in subprocess module
    # call system command "date -u" (display current UTC time) and, save its screen outputs into a string
    utc_time_string = subprocess.check_output(["date", "-u"])

    # Call external services (served on other servers) using 3rd party python HTTP tool -- requests
    # get weather info for London using openweathermap.org rest api
    api_call_obj = requests.get("http://samples.openweathermap.org/data/2.5/weather?q=London,uk&appid=b6907d289e10d714a6e88b30761fae22")
    london_weather_data = api_call_obj.content



    ################# Show results on webpage (return a webpage to user) ##########################
    # put all info you want to display on webpage into a dictionary obj called context
    #   context = {"Name1": Value1,
    #               "Name2": Value2,
    #               "Name3": Value3}
    context = {"res_id": res_id,
               "utc_time":  utc_time_string,
               "london_weather_data": london_weather_data
    }

    # change html template file 'my_brainishare_app/home.html' (location: my_brainishare_app/templates/my_brainishare_app/home.html)
    # to customize webpage layout, which contains placeholders like {{Name1}}, {{Name2}}

    # call function "render()" to replace placeholders in html template with corresponding values (Value1, Value2) stored in context obj
    # and return completed webpage back to user
    return render(request, 'my_brainishare_app/home.html', context)