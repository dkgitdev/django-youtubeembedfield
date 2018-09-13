import urlparse
from django.db import models


class YouTubeEmbedField(models.URLField):
    description = 'YouTube embed field'

    def to_python(self, value):
        youtube_embed_url_template = 'https://youtube.com/embed/%s'

        if value and not value.startswith(youtube_embed_url[:-2]):
            parsed_url = urlparse.urlparse(value)
            parse_qs = urlparse.parse_qs(parsed_url.query)
            youtube_id = parse_qs['v'][0]
            return youtube_embed_url_template % youtube_id

        return value


try:
    from south.modelsinspector import add_introspection_rules

    add_introspection_rules([],
        [
            "youtubeembedfield\.fields\.YouTubeEmbedField"
        ])
except ImportError:
    pass
