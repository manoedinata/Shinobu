import tldextract

# Known websites mapping with multiple domains
known_websites = {
    "youtube": ["youtube.com", "youtu.be"]
}

def detect_website(url):
    extracted = tldextract.extract(url)
    domain = extracted.fqdn
    domain = domain.replace("www.", "") # Remove www prefix just to be sure
    print(domain)

    for site, domains in known_websites.items():
        if domain in domains:
            return site

    return None
