# Log_Parser

## Project overview
This repository contains utilities to parse log files and extract lists, counts and JSON outputs for images, IPs, emails, dates, and URLs as described in Project_Assignment.txt.

## Prerequisites
- Python 3.8+
- Standard library modules: re, json, collections
- No external packages required by default; if you add any, install via pip.

## Files and expected functions
Implement (or confirm) functions matching the assignment. The README below maps suggested names to the assignment items.

1. get_image_list(log_text)  (assignment: get_ip_list / get_image_list)
   - Returns a list of image file names or paths found in the log.

2. count_image(log_text)  (assignment: count_ip / count_image)
   - Returns the total number of images found (int).

3. counter_image(log_text)  (assignment: counter_ip / counter_image)
   - Returns a dict or collections.Counter mapping image -> occurrences.

4. counter_email(log_text)  (assignment: counter_ip / counter_email)
   - Returns a dict or Counter mapping email -> occurrences.

5. create_json_file_ip(data, filename='ip_address.json')  (assignment: create_json_file_ip)
   - Write IP-related data to a JSON file.

6. create_json_file_email(data, filename='email.json')  (assignment: create_json_file_email)
   - Write email-related data to a JSON file.

7. get_date_list(log_text)  (assignment: get_date_list)
   - Returns a list of dates found in the log.

8. get_url_list(log_text)  (assignment: get_url_list)
   - Returns a list of URLs found in the log.

9. counter_date(log_text)  (assignment: counter_date)
   - Returns a dict/Counter mapping date -> occurrences.

10. counter_url(log_text)  (assignment: counter_url)
   - Returns a dict/Counter mapping url -> occurrences.

11. create_json_file_date(data, filename='date.json')  (assignment: create_json_file_date)
   - Write date-related data to a JSON file.

12. create_json_file_url(data, filename='url.json')  (assignment: create_json_file_url)
   - Write URL-related data to a JSON file.

Notes on naming
- The Project_Assignment.txt lists alternative names (for example, get_ip_list -> get_image_list). Use consistent names in code and update this README accordingly.

## Usage examples

1) Read a log file into Python

```python
with open('access.log', 'r', encoding='utf-8') as f:
    log_text = f.read()
```

2) Import and call parsing functions (adjust module name as needed, e.g., parser.py)

```python
from parser import (
    get_image_list, get_date_list, get_url_list, get_email,
    count_image, counter_image, counter_email, counter_date, counter_url,
    create_json_file_ip, create_json_file_email, create_json_file_date, create_json_file_url,
)

images = get_image_list(log_text)
dates = get_date_list(log_text)
urls = get_url_list(log_text)
emails = get_email(log_text)

total_images = count_image(log_text)
image_counts = counter_image(log_text)
email_counts = counter_email(log_text)

create_json_file_ip(image_counts, 'ip_address.json')
create_json_file_email(email_counts, 'email.json')
create_json_file_date(counter_date(log_text), 'date.json')
create_json_file_url(counter_url(log_text), 'url.json')
```

## JSON file format
Prefer a simple mapping of item -> count. Example:

```json
{
  "image1.png": 12,
  "image2.jpg": 4
}
```

Alternatively you may output an array of objects when order matters.

## Regular expression examples
- Email (from Project_Assignment.txt):

```python
regex = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
emails = re.findall(regex, log_text)
```

- URL (simple):

```python
regex = r"https?://[^\s]+"
urls = re.findall(regex, log_text)
```

- Date (YYYY-MM-DD):

```python
regex = r"\d{4}-\d{2}-\d{2}"
dates = re.findall(regex, log_text)
```

- Image files:

```python
regex = r"[\w\-/]+\.(?:png|jpg|jpeg|gif|svg)"
images = re.findall(regex, log_text)
```

## Example helper implementations
Below are short helper snippets you can add to parser.py.

```python
# Example: aggregate a list into counts
from collections import Counter

def list_to_counter(items):
    return Counter(items)

# Example: write JSON file
import json

def create_json_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2)
```

## Best practices and troubleshooting
- Open logs with the correct encoding (utf-8 recommended).
- Use collections.Counter to aggregate duplicates.
- When matching complex date formats or URLs, refine regexes and test on representative log lines.

## Next steps (suggested)
- Confirm which function names your code uses; I can update this README to match them exactly.
- I can add a parser.py module with working implementations and unit tests.
- I can add sample logs and expected JSON outputs for testing.

---

This README was generated to replace Readme.txt with a Markdown README for easier viewing on GitHub.