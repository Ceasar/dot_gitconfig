import staticjinja


def ignore_underscores(name):
    return not name.startswith('_')

if __name__ == "__main__":
    staticjinja.main(autoreload=False,
                     filter_func=ignore_underscores)
