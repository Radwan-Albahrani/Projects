# Importing MDAPP from kivymd
from kivymd.app import MDApp

# Importing Sqlite
import sqlite3

# importing local scripts
from propertymapview import PropertyMapView
from searchpopupmenu import SearchPopupMenu

# For simulating a phone screen
from kivy.core.window import Window

# Used during development only
Window.size = (330, 630)

# creating window and starting app
class MainApp(MDApp):
    # Connection to database variables
    connection = None
    cursor = None
    search_menu = None

    def build(self):
        # Setting the theme
        self.theme_cls.primary_palette = "Blue"
        # And title
        self.title = "IOI properties"

    # When app Starts, do the following.
    def on_start(self):
        # Connect to database and grab its cursor
        self.connection = sqlite3.connect("DataBases\\properties.db")
        self.cursor = self.connection.cursor()

        # Start the searchbar menu popup
        self.search_menu = SearchPopupMenu()


# Running said app
MainApp().run()

