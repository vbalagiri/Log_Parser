"""parser.py
Basic log parsing helpers for images, IPs, emails, dates, and URLs.
This module provides simple regex-based extraction functions and JSON helpers.
"""
from collections import Counter
import json
import re
from typing import List, Dict, Union

# Regex patterns
EMAIL_RE = re.compile(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", re.IGNORECASE)
URL_RE = re.compile(r"https?://[^"]+")
IMAGE_RE = re.compile(r"[\w\-/]+\.(?:png|jpg|jpeg|gif|svg)", re.IGNORECASE)
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")  # YYYY-MM-DD
IP_RE = re.compile(r"\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b")

# Extraction functions
def get_image_list(log_text: str) -> List[str]:
    return IMAGE_RE.findall(log_text or "")

def count_image(log_text: str) -> int:
    return len(get_image_list(log_text))

def counter_image(log_text: str) -> Counter:
    return Counter(get_image_list(log_text))

# Email
def get_email(log_text: str) -> List[str]:
    return EMAIL_RE.findall(log_text or "")

def counter_email(log_text: str) -> Counter:
    return Counter(get_email(log_text))

# IPs
def get_ip_list(log_text: str) -> List[str]:
    return IP_RE.findall(log_text or "")

def create_json_file_ip(data: Union[Dict, List], filename: str = "ip_address.json") -> None:
    create_json_file(data, filename)

# Dates
def get_date_list(log_text: str) -> List[str]:
    return DATE_RE.findall(log_text or "")

def counter_date(log_text: str) -> Counter:
    return Counter(get_date_list(log_text))

# URLs
def get_url_list(log_text: str) -> List[str]:
    return URL_RE.findall(log_text or "")

def counter_url(log_text: str) -> Counter:
    return Counter(get_url_list(log_text))

# Generic JSON helpers
def create_json_file(data: Union[Dict, List, Counter], filename: str) -> None:
    # Accept Counter or dict or list
    writeable = data
    if isinstance(data, Counter):
        writeable = dict(data)
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(writeable, f, indent=2)

def create_json_file_email(data: Union[Dict, List, Counter], filename: str = "email.json") -> None:
    create_json_file(data, filename)

def create_json_file_date(data: Union[Dict, List, Counter], filename: str = "date.json") -> None:
    create_json_file(data, filename)

def create_json_file_url(data: Union[Dict, List, Counter], filename: str = "url.json") -> None:
    create_json_file(data, filename)

# Backwards-compatible aliases referenced in Project_Assignment.txt
count_ip = count_image
counter_ip = counter_image
get_image_list = get_image_list

if __name__ == "__main__":
    # Quick smoke test
    sample = """
    2025-01-01 GET /static/logo.png 200
    Visitor 192.168.0.1 contacted https://example.com/page.html and sent contact@domain.com
    """
    print(get_image_list(sample))
