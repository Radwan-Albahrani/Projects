# Imports
from kivymd.uix.dialog import MDInputDialog
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.button import Button
from urllib import parse
from kivy.network.urlrequest import UrlRequest
from kivy.app import App

# A Class that controls search popup menu
class SearchPopupMenu(MDInputDialog):
    # Changing title and search labels
    title = "Search by Address"
    text_button_ok = "Search"

    # Initiating class and inheriting its parent initiating funcion
    def __init__(self):
        super().__init__()
        # Changing size of the popup menu
        self.size_hint = [.8,.3]

        # When button is clicked, use callback function
        self.events_callback = self.callback

    def callback(self, *args):
        #When called, Take address from text field
        address = self.text_field.text

        #Set text field to none
        self.text_field.text = ""
        
        # Call geocode function
        self.geocode_get_lat_lon(address)

    def geocode_get_lat_lon(self, address):
        # Parsing the address
        address = parse.quote(address)
        
        # Inserting the app key
        app_key = "5E-OFPUbXNWw8Xe94ItKOYZHgWXEhBUE8kIj3MRPaqc"
        
        # Putting address and app keyinto the url
        url = "https://geocode.search.hereapi.com/v1/geocode?q=%s&apiKey=%s"%(address, app_key)

        # Requesting data from url, and requesting success failure or error functions
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error)

    def success(self, urlrequest, result):
        # Assigning Variables
        latitude = None
        longitude = None

        # Getting Lat and Lon of search result, If address is valid
        try:
            latitude = result['items'][0]['position']['lat']
            longitude = result['items'][0]['position']['lng']
        except:
            IndexError
        
        # Reference to app
        app = App.get_running_app()

        # Reference to Mapview
        mapview = app.root.ids.Mapview

        # if address is valid go to location
        if latitude != None:
            # Center on Search query.
            mapview.center_on(latitude, longitude)
        
        #Else, Popup saying There was an error
        else:
            popup = Popup(title='Error', title_size = 20, title_color = [0.9,0.2,0.1,1], separator_color = [0.9,0.2,0.2,1], content=Label(text='Invalid Address, Try Again'),size_hint = [.3,.2])
            popup.open()

    #If No internet connection, show popup
    def error(self, urlrequest, result):
        popup = Popup(title='Error', title_size = 20, title_color = [0.9,0.2,0.1,1], separator_color = [0.9,0.2,0.2,1], content=Label(text='No Internet Connection'), size_hint = [.3,.2])
        popup.open()

    #If failed, Show popup
    def failure(self, urlrequest, result):
        popup = Popup(title='Error', title_size = 20, title_color = [0.9,0.2,0.1,1], separator_color = [0.9,0.2,0.2,1], content=Label(text='Invalid input'), size_hint = [.3,.2])
        popup.open()