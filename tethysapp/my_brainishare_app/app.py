from tethys_sdk.base import TethysAppBase, url_map_maker


class MyBrainishareApp(TethysAppBase):
    """
    Tethys app class for My Brainishare App.
    """

    name = 'My Brainishare App'
    index = 'my_brainishare_app:home'
    icon = 'my_brainishare_app/images/brain.jpg'
    package = 'my_brainishare_app'
    root_url = 'my-brainishare-app'
    color = '#2c3e50'
    description = 'Place a brief description of your app here.'
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='my-brainishare-app',
                controller='my_brainishare_app.controllers.home'
            ),
        )

        return url_maps
