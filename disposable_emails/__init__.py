import os


def read_blacklist():
    source_dir = os.path.dirname(__file__)
    blacklist_path = os.path.join(source_dir, 'data/domains.txt')

    with open(blacklist_path) as f:
        return {line.rstrip() for line in f.readlines()}


def is_disposable_email(email: str) -> bool:
    return is_disposable_domain(email.rsplit('@')[-1])


def is_disposable_domain(domain: str) -> bool:
    return domain in blacklist


blacklist = read_blacklist()
