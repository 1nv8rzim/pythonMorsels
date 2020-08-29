from html.parser import HTMLParser


class TagParser(HTMLParser):
    def handle_starttag(self, tag, attr_pairs):
        attributes = {}
        for key, value in attr_pairs:
            attributes.setdefault(key, value)
        self.value = (tag, attributes)


def parse_tag(html_tag):
    """Return tuple of tag name and sorted attributes."""
    parser = TagParser()
    parser.feed(html_tag)
    return parser.value


def tags_equal(tag1, tag2):
    return parse_tag(tag1) == parse_tag(tag2)
