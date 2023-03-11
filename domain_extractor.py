links = [
    "https://github.com/AnasNadeem",
    "https://twitter.com/whoareyouanas",
    "https://www.instagram.com/whoareyouanas/",
    "https://www.youtube.com/watch?v=iWomYr2dlsM&list=PLmUgeKw7vSS6zpu1ZZMk1BtNBqkFgIOyv&index=13",
    "https://anas.abc.com",
    "www.google.com",
]


def platform_extractor(link):
    platform = None
    have_protocol = link.startswith('http')
    dot_split = link.split('.')
    count_dots = len(dot_split)
    if count_dots == 3:
        platform = dot_split[1]
        return platform

    if have_protocol and (count_dots == 2):
        platform = dot_split[0].split('//')[1]
    elif count_dots == 2:
        platform = dot_split[0]
    else:
        return None
    return platform


for link in links:
    print(f"{link}: {platform_extractor(link)}")
