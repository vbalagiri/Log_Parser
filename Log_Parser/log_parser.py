"""
What is the purpose : This log parser will extract,parse the below details in form of
list and dict
IP
DATE
pics
URL

# version : 1.1
# Author : Venkatesh Balagiri
# Deployment date: Aug-28th 2023
"""

import re
import os
import collections
import json
import \
    logging  # to print log format  # datetime - log mode - message # Ex:  2023-08-29 09:09:30,847 - DEBUG - Find Email list:
import configparser
import datetime

# Get the path to the config directory
# E:\Projects\Technical\Python\Python_Digital_Mastery_Basic\Project\Log_Parser\config
config_dir = os.path.join(os.path.dirname(__file__), 'config')

# Get the path to the config file
# "E:\Projects\Technical\Python\Python_Digital_Mastery_Basic\Project\Log_Parser\config\"  + "config.ini"
config_file_path = os.path.join(config_dir, 'config.ini')

# Read the configuration file
config = configparser.ConfigParser()
config.read(config_file_path)
# config.read("E:\Projects\Technical\Python\Python_Digital_Mastery_Basic\Project\Log_Parser\config\config.ini")

logfilename = config['file_config']['logfilename']  # config[header config tag][variable tag]
# E:\Projects\Technical\Python\Python_Digital_Mastery_Basic\Project\Log_Parser\log_output\app.log

jsonfile = config['file_config']['jsonfile']
# E:\Projects\Technical\Python\Python_Digital_Mastery_Basic\Project\Log_Parser\image.json

# Configure the logging settings
logging.basicConfig(level=logging.DEBUG,  # Set the logging level
                    format='%(asctime)s - %(levelname)s - %(message)s',  # Define log message format
                    filename=logfilename,  # Specify the log file
                    filemode='w')  # Set filemode to 'w' to write mode

# Create a logger
logger = logging.getLogger('log_parser')


def log_file_reader(filename):
    with open(filename) as f:
        log = f.read()
    return log


# Get all IP addresses from the log file
def get_ips(log_file):
    regex = r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}'
    ip_list = re.findall(regex, log_file)
    return ip_list


# Get total count of IPs
def count_ip(ip_list):
    return len(ip_list)


# Get total counter of IPs
def counter_ip(ip_list):
    return collections.Counter(ip_list)


# Function to check if the string is palindrome or not
def find_palindrome(log_file):
    palindrome_list = list()
    words_list = log_file.split()
    print(words_list)
    for word in words_list:
        if ((word == word[::-1]) and (word.isalpha()) and (len(word) > 1)):
            palindrome_list.append(word)
    return palindrome_list


# Function to check if the string exist in a line.
def find_word(log_file):
    # search_word = input("Enter word to search: ")
    search_word = config['file_config']['search_word']
    data_lines = log_file.split('\n')
    for line in data_lines:
        if search_word in line.lower():
            return line


# Function to search for the images and add them to dictionary.
def find_images(log_file):
    words_list = log_file.split()
    image_dict = dict()
    for word in words_list:
        if word.lower().endswith(('.gif', '.jpeg', '.png', '.jpg')):
            # print(word)
            if 'gif' in word:
                if image_dict.get('GIF'):
                    image_dict['GIF'] = image_dict.get('GIF') + ', ' + word
                else:
                    image_dict['GIF'] = word
            elif 'jpeg' in word:
                if image_dict.get('JPEG'):
                    image_dict['JPEG'] = image_dict.get('JPEG') + ', ' + word
                else:
                    image_dict['JPEG'] = word
            elif 'png' in word:
                if image_dict.get('PNG'):
                    image_dict['PNG'] = image_dict.get('PNG') + ', ' + word
                else:
                    image_dict['PNG'] = word
            elif 'jpg' in word:
                if image_dict.get('JPG'):
                    image_dict['JPG'] = image_dict.get('JPG') + ', ' + word
                else:
                    image_dict['JPG'] = word
            else:
                if image_dict.get('OTHERS'):
                    image_dict['OTHERS'] = image_dict.get('OTHERS') + ', ' + word
                else:
                    image_dict['OTHERS'] = word
    # if image_dict:
    # print("Images: ", image_dict)
    # logger.debug('Function to search for the images and add them to dictionary' + str(image_dict))
    return image_dict


# Function to search for the Email ID's.
def find_emails(log_file):
    emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", log_file)
    # print("Email ID's: ", emails)
    return emails


def convert_to_json(log_file):
    data_dict = find_images(log_file)
    json_data = json.dumps(data_dict)
    logger.debug('Function to convert_to_json')
    return json_data


def create_json_file(filename, data):
    """
    Create a JSON file and write data to it.
    
    Args:
        filename (str): The name of the JSON file to be created.
        data (dict): The data to be written to the JSON file.
        
    Returns:
        None
    """
    with open(filename, 'w') as json_file:
        json.dump(data, json_file, indent=2)


# Fetching log file from configuration file
filename = config['file_config']['filename']

# Reading logfile
log_file = log_file_reader(filename)

# Extracting IP Address list from log file
ip_list = get_ips(log_file)
# print("IP Address list:", ip_list)
logger.debug("IP Address list: ")
logger.debug(str(ip_list))

# Extracting No of IP Addresses count from IP Address list
ip_count = count_ip(ip_list)
# print("IP Address count:", ip_count)
logger.debug("No of IP Addresses count: " + str(ip_count))

# Extracting IP Address counter from IP Address list
ip_counter = counter_ip(ip_list)
# print("IP Address counter:", ip_counter)
logger.debug("IP Address counter: ")
logger.debug(str(ip_counter))

# Extracting Images Groups from log file
logger.debug("Images Groups:")
logger.debug(str(find_images(log_file)))
logger.debug("Images Groups data type: " + str(type(find_images(log_file))))

# Creating Image.json by reading log file
data = find_images(log_file)
create_json_file(jsonfile, data)

# Find Email list by reading log file
logger.debug("Find Email list:")
logger.debug(str(find_emails(log_file)))

# convert_to_json from dict to json by reading log file
json_output = convert_to_json(log_file)
logger.debug("json_output: ")
logger.debug(str(json_output))
logger.debug("json_output data type: " + str(type(json_output)))

# find_palindrome by reading log file
logger.debug("Palindrome words: ")
logger.debug(str(find_palindrome(log_file)))

# find word by reading log file
logger.debug("Find word: ")
logger.debug(str(find_word(log_file)))

# shutting down logging module
logging.shutdown()

# Get today's date
current_time = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# Generate the new file name with the current date
new_filename = logfilename + str("_") + current_time

# Rename the file
os.rename(logfilename, new_filename)

print(f"Log '{new_filename}' has been created successfully")
