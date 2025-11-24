README for Log_Parser

Project overview
- This repository contains utilities to parse log files and extract lists, counts and JSON outputs for images, IPs, emails, dates and URLs as described in Project_Assignment.txt.

Prerequisites
- Python 3.8+ installed
- Standard library modules: re, json
- If there are additional dependencies, install them with pip (none required by default).

Files and expected functions
- The repo should expose (or you should create) functions with these names to match the assignment:
  1. get_image_list(log_text) or get_ip_list: returns a list of image names/paths found in the log
  2. count_image(log_text) or count_ip: returns the total number of images found
  3. counter_image(log_text) or counter_ip: returns a dict counter mapping image -> occurrences
  4. counter_email(log_text) or counter_ip (for emails): returns a dict counter mapping email -> occurrences
  5. create_json_file_ip(data, filename): write IP-related data to ip_address.json
  6. create_json_file_email(data, filename): write email-related data to email.json
  7. get_date_list(log_text): returns a list of dates found in the log
  8. get_url_list(log_text): returns a list of URLs found in the log
  9. counter_date(log_text) or counter_ip (for dates): returns a dict counter mapping date -> occurrences
 10. counter_url(log_text) or counter_ip (for urls): returns a dict counter mapping url -> occurrences
 11. create_json_file_date(data, filename): write date-related data to date.json
 12. create_json_file_url(data, filename): write url-related data to url.json

Notes on naming
- The Project_Assignment.txt lists some alternative names (e.g., get_ip_list -> get_image_list). Implementations may use either naming convention; ensure your Readme maps the names used in your code to the assignment list.

Usage examples
1) Read a log file into Python
   with open('access.log', 'r', encoding='utf-8') as f:
       log_text = f.read()

2) Get lists
   from parser import get_image_list, get_date_list, get_url_list, get_email  # adjust module name as needed

   images = get_image_list(log_text)
   dates = get_date_list(log_text)
   urls = get_url_list(log_text)
   emails = get_email(log_text)

3) Get counts and counters
   from parser import count_image, counter_image, counter_email, counter_date, counter_url

   total_images = count_image(log_text)
   image_counts = counter_image(log_text)   # returns dict or collections.Counter
   email_counts = counter_email(log_text)

4) Create JSON files
   from parser import create_json_file_ip, create_json_file_email, create_json_file_date, create_json_file_url

   create_json_file_ip(image_counts, 'ip_address.json')       # or create_json_file_ip(list_of_ips, filename)
   create_json_file_email(email_counts, 'email.json')
   create_json_file_date(counter_date(log_text), 'date.json')
   create_json_file_url(counter_url(log_text), 'url.json')

JSON file format suggestion
- Each JSON file should contain an object mapping item -> count, or an array of objects. Example for counts:
  {
    "image1.png": 12,
    "image2.jpg": 4
  }

Regular expressions examples
- Email (example from Project_Assignment.txt):
  regex = r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+"
  emails = re.findall(regex, log_text)

- URL (simple example):
  regex = r"https?://[^\s]+"
  urls = re.findall(regex, log_text)

- Date (example common formats):
  regex = r"\d{4}-\d{2}-\d{2}"  # YYYY-MM-DD

- Image paths (example looking for file extensions):
  regex = r"[\w\-/]+\.(?:png|jpg|jpeg|gif|svg)"

Best practices and troubleshooting
- Ensure you open the log file with the correct encoding.
- If functions return lists of duplicates, use collections.Counter to aggregate counts:
    from collections import Counter
    counter = Counter(image_list)

- If you add or rename functions, update this Readme and Project_Assignment.txt to keep names consistent.

What I changed
- Added this Readme.txt describing the steps to perform the assignments in Project_Assignment.txt and example usage.