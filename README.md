# search-image

This is kinda a speed run to create a Flask app as quickly as possible. It's a simple image gallery with a search function (also search by color).
All image data is pulled from Unsplashed's API. Focusing in on an image links to the image author's original.
The server side Flask component is very lightweight, however all asynchronous features (lazy loading, infinite scrolling, gallery lightbox, etc.)
could not be done in Python and are implemented in JS instead.
