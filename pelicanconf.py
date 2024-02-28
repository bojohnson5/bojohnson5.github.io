AUTHOR = 'Bo Johnson'
SITENAME = 'Physical Constants'
SITESUBTITLE = "Personal site for Bo Johnson"
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
)

# Social widget
SOCIAL = (
    ("Github", "https://github.com/bojohnson5"),
    ("envelope", "mailto:bojohn@iu.edu"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

# Personal additions
OUTPUT_PATH = "docs/"
THEME = "attila"

MENUITEMS = (("Home", "/"),)
