This will be the making of a website of shopping e commerce from scratch in python.

I think to make it a extensable website.

Below i am keep record of how i am using the bs's icons:
(bootstrap-icons-1.13.1.zip) [https://github.com/twbs/icons/releases/latest/]
from this link i will download the zip.

    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.css">

    <link rel="stylesheet" href="{{ url_for('static', filename='css/bootstrap-icons.css') }}">

i need to keep the icons css and the fonts in same dir.


Some Variable Globally:

* BUSINESS_NAME



## How i can run the application:

```
uv run main.py
```