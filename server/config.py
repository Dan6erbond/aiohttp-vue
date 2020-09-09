import os


class Config(object):
    def __init__(self):
        is_production = os.environ["SERVER_ENV"] == "production"
        self._config = dict(
            debug=not is_production,
            static_dir="dist",
            host="127.0.0.1",
            port=8080,
            description="A minimal Discord bot dashboard shipped with the DiscordPyCLI by Amelia Cabotte and RaviAnand Mohabir.",
            title="DiscordPyCLI Dashboard",
            contact_email="discordpycli@gmail.com",
        )

    def __getitem__(self, attr_name):
        return self._config[attr_name]

    def __getattr__(self, attr_name):
        return self._config[attr_name]


config = Config()
