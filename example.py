import whois

def get_domain_age(domain_name):
    try:
        domain_info = whois.whois(domain_name)
        if domain_info.creation_date:
            return (domain_info.creation_date - domain_info.updated_date).days
        else:
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

domain_name = "https://web.whatsapp.com/"  
domain_age = get_domain_age(domain_name)

if domain_age is not None:
    print(f"The domain {domain_name} is approximately {domain_age} days old.")
else:
    print(f"Unable to determine the domain age.")
