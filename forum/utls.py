import re




def extract_at_users(content):
    users = re.findall(r"@(.+?) ", content)
    return users