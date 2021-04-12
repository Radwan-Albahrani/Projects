from kivy.garden.mapview import MapMarkerPopup

from kivymd.uix.useranimationcard import MDUserAnimationCard
from kivy.factory import Factory
from kivy.lang import Builder
from kivymd.uix.button import MDIconButton
from kivymd.uix.list import ILeftBodyTouch

# Your content for a contact card.
Builder.load_string(
    """
#:import get_hex_from_color kivy.utils.get_hex_from_color


<TestAnimationCard@MDBoxLayout>
    orientation: 'vertical'
    padding: dp(10)
    spacing: dp(10)
    adaptive_height: True

    MDLabel:
    MDLabel:
    MDLabel:
    MDLabel:
    MDLabel:
    MDLabel:
        text: "Situated within a mixed development township, Alanis is the first service apartment in Warisan Puteri @ Sepang. It brings you yet another promising living experience away from the city hassle. With various layout types available."
    MDLabel:
    MDLabel:
    MDLabel:
    MDLabel:
    MDLabel:
    MDLabel:
    

    OneLineIconListItem:
        text: "1-3 Bedroom(s)"
        IconLeftSampleWidget:
            icon: 'home-outline'

    OneLineIconListItem:
        text: "2 Bathrooms"
        IconLeftSampleWidget:
            icon: 'shower'

    TwoLineIconListItem:
        text: "Built up max: 926sqft"
        secondary_text: "[color=%s]Built up min: 441sqft[/color]" % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'image-size-select-small'

    OneLineIconListItem:
        text: "24 hr security"
        IconLeftSampleWidget:
            icon: 'cctv'

    OneLineIconListItem:
        text: "1.5km to Salak Tinggi ERL station"
        IconLeftSampleWidget:
            icon: 'train'

    TwoLineIconListItem:
        text: "Price: 253,000rm"
        secondary_text: "[color=%s]Price per sqft: 420[/color]" % get_hex_from_color(app.theme_cls.primary_color)
        IconLeftSampleWidget:
            icon: 'square-inc-cash'

    MDRoundFlatButton:
        text: "                      Register                      "
        pos_hint: {"center_x": 0.5, "center_y": 0}
"""
)


class IconLeftSampleWidget(ILeftBodyTouch, MDIconButton):
    pass


class PropertyMarker(MapMarkerPopup):
    ## IF WE WANT TO CHANGE MARKER COLOR OR SHAPE OR IMAGE
    ## USE THIS LINE
    source = "img\\marker.png"

    # This variable will hold property data
    property_data = []

    def on_release(self):
        # every time this is called, Create menu from data
        menu = MDUserAnimationCard(
            user_name="Alanis Warisan Puteri",
            path_to_avatar="img\\inside.jpg",
            callback=lambda: menu.dismiss(),
        )
        menu.box_content.add_widget(Factory.TestAnimationCard())
        menu.open()
