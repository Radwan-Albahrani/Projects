# Getting Imports
from kivy.garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from propertymarker import PropertyMarker

# Class that connects to Mapview module
class PropertyMapView(MapView):

    # Timer variable
    getting_properties_timer = None

    # Property Name list Variable.
    property_names = []

    # Function to get properties visible in POV
    def start_getting_properties_in_fov(self):

        # After one second, get the properties in FOV
        try:
            self.getting_properties_timer.cancel()
        except:
            pass

        # Set timer once for one second, then start getting properties in FOV
        self.getting_properties_timer = Clock.schedule_once(
            self.get_properties_in_fov, 1
        )

    # Function to actually get properties if any in FOV
    def get_properties_in_fov(self, *args):
        # Get border coordinates min and max
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        # Get reference to main app and database cursor
        app = App.get_running_app()

        # Sql statement to get everything from properties table IF its in border of mapview
        ## HERE YOU NEED TO CHANGE TABLE NAME INSIDE SQL STATEMENT
        ## MAKE SURE TABLE INCLUDES LATITUDE AS y AND LONGITUDE AS x OF SIMULATED PROPERTY
        sql_statement = (
            "SELECT * FROM properties WHERE x > %s AND x < %s AND y > %s AND y < %s"
            % (min_lon, max_lon, min_lat, max_lat)
        )
        app.cursor.execute(sql_statement)
        properties = app.cursor.fetchall()

        # For next video
        for property in properties:
            # Get name of current property
            ## MAKE SURE NAMES IS IN FIRST INDEX, WHICH IS SECOND COLUMN
            name = properties[1]

            # Check if name has already been marked with marker before
            if name in self.property_names:
                pass

            # If name not found, Add marker to map
            else:
                self.add_property(property)

    # Function to add property
    def add_property(self, property):
        # Getting lat and lon from property given when called
        ## THESE INDEXES NEED TO BE CHANGED DEPENDING ON DATABASE INDEX. UNLESS YOUR TAABLE HAS THEM IN THE SAME LOCATION
        ## DO NOT RUN APP WHILE THESE INDEXES ARE INCORRECT
        lat, lon = property[6], property[5]
        
        # Add marker from PropertyMarker class
        marker = PropertyMarker(lat=lat, lon=lon)

        # Add Marker to Map
        self.add_widget(marker)

        # get the name of the added property
        ## MAKE SURE NAMES IS IN FIRST INDEX, WHICH IS SECOND COLUMN
        name = property[1]

        # get all property data
        marker.property_data = property

        # Add name to property names list
        self.property_names.append(name)
