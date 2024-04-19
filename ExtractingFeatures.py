import urllib.parse
import re

def urlFeatures(url):
    #Extracting Feature 1 URL Length
    url_length_phishing = 0
    url_length = len(url)
    if url_length >= 54:
        url_length_phishing = 1

    #Extracting Feature 2 Use of Non Standard Ports
    nonstandard_ports_phishing = 0
    parsed_url = urllib.parse.urlparse(url)
    port = parsed_url.port
    if port is not None and port not in [80, 443]:
        nonstandard_ports_phishing = 1

    #Extracting Feature 3 Use of HTTPS
    https_usage_phishing = 0
    if url.startswith("https://"):
        https_usage_phishing = 0
    else:
        https_usage_phishing = 1

    #Extracting Feature 4 Presence of Special Characters
    special_characters_phishing = 0
    special_characters = ["@", "!", "$", "-", "_", "#"]
    if any(char in url for char in special_characters):
        special_characters_phishing = 1

    #Extracting Feature 5 Presence of Numeric Characters
    numeric_characters_phishing = 0
    numeric_characters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    if any(char in url for char in numeric_characters):
        numeric_characters_phishing = 1
    
    #Extracting Feature 6 Number of Redirects
    no_of_redirects_phishing = 0
    redirect_count = len(re.findall("//", url))
    if redirect_count > 6:
        no_of_redirects_phishing = 1

    #Extracting Feature 7 Shortening of URL
    shortening_phishing = 0
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
        shortening_phishing = 1
    
    url_characteristics = [[url_length_phishing, nonstandard_ports_phishing, https_usage_phishing, special_characters_phishing, numeric_characters_phishing, no_of_redirects_phishing, shortening_phishing]]

    return url_characteristics

# print(urlFeatures("http://234.50.198.35.bc.googleusercontent.com/atendimento/home/04/signature/?key=ee9ac9ac"))
# print(urlFeatures("https://www.artscow.com/diy/mousepad"))