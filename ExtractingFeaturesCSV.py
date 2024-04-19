import csv
import re
import urllib.parse

#Getting all the urls and their results (1 is phishing and 0 is legitimate)
url_data = []
result_data = []
with open("phishing_data.csv", "r", newline='') as fr:
    data = csv.DictReader(fr)
    for row in data:
        url = row["url"]
        result = row["result"]
        url_data.append(url)
        result_data.append(result)

#Getting Feature 1 url length
url_length_phishing = []
for i in range(0, len(url_data)):
    urlLength = len(url_data[i])
    if urlLength >= 54:
        url_length_phishing.append(1)
    else:
        url_length_phishing.append(0)

#Getting Feature 2 Use of non standard ports
nonstandard_ports_phishing = []
for i in range(0, len(url_data)):
    url = url_data[i]
    parsed_url = urllib.parse.urlparse(url)
    port = parsed_url.port
    if port is not None and port not in [80, 443]:
        nonstandard_ports_phishing.append(1)
    else:
        nonstandard_ports_phishing.append(0)

#Getting Feature 3 Use of HTTPS
https_usage_phishing = []
for i in range(0, len(url_data)):
    url = url_data[i]
    if url.startswith("https://"):
        https_usage_phishing.append(0)
    else:
        https_usage_phishing.append(1)

#Getting Feature 4 Presence of Special Characters
special_characters_phishing = []
special_characters = ["@", "!", "$", "-", "_", "#"]
for i in range(0, len(url_data)):
    url = url_data[i]
    if any(char in url for char in special_characters):
        special_characters_phishing.append(1)
    else:
        special_characters_phishing.append(0)

#Getting Feature 5 Presence of Numeric Characters
numeric_characters_phishing = []
numeric_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in range(0, len(url_data)):
    url = url_data[i]
    if any(char in url for char in numeric_characters):
        numeric_characters_phishing.append(1)
    else:
        numeric_characters_phishing.append(0)

#Getting Feature 6 Number of Redirects
no_of_redirects_phishing = []
for i in range(0, len(url_data)):
    url = url_data[i]
    redirect_count = len(re.findall("//", url))
    if redirect_count > 6:
        no_of_redirects_phishing.append(1)
    else:
        no_of_redirects_phishing.append(0)

#Getting Feature 7 Shortening of URL
shortening_phishing = []
for i in range(0, len(url_data)):
    url = url_data[i]
    shortening_services = r"bit\.ly|goo\.gl|shorte\.st|go2l\.ink|x\.co|ow\.ly|t\.co|tinyurl|tr\.im|is\.gd|cli\.gs|" \
                      r"yfrog\.com|migre\.me|ff\.im|tiny\.cc|url4\.eu|twit\.ac|su\.pr|twurl\.nl|snipurl\.com|" \
                      r"short\.to|BudURL\.com|ping\.fm|post\.ly|Just\.as|bkite\.com|snipr\.com|fic\.kr|loopt\.us|" \
                      r"doiop\.com|short\.ie|kl\.am|wp\.me|rubyurl\.com|om\.ly|to\.ly|bit\.do|t\.co|lnkd\.in|db\.tt|" \
                      r"qr\.ae|adf\.ly|goo\.gl|bitly\.com|cur\.lv|tinyurl\.com|ow\.ly|bit\.ly|ity\.im|q\.gs|is\.gd|" \
                      r"po\.st|bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|u\.bb|yourls\.org|x\.co|" \
                      r"prettylinkpro\.com|scrnch\.me|filoops\.info|vzturl\.com|qr\.net|1url\.com|tweez\.me|v\.gd|" \
                      r"tr\.im|link\.zip\.net"
    match = re.search(shortening_services, url)
    if match:
        shortening_phishing.append(1)
    else:
        shortening_phishing.append(0)

#Writing all the data to another csv file
with open("url_specifications.csv", "w", newline='') as fw:
    writer = csv.writer(fw)
    writer.writerow(["URL", "URL Length", "Non Standard Ports", "HTTPS", "Special Characters", "Numeric Characters", "Number of Redirects", "Shortening of URL", "Phishing"])
    for i in range(0, len(url_data)):
        writer.writerow([url_data[i], url_length_phishing[i], nonstandard_ports_phishing[i], https_usage_phishing[i], special_characters_phishing[i], numeric_characters_phishing[i], no_of_redirects_phishing[i], shortening_phishing[i], result_data[i]])