import re


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    regexp = r'(.*{0})?(.+(?={1}){2})'.format(re.escape(begin) or '^', re.escape(end) or '$',
                                              end not in text and '?' or '')
    m = re.search(regexp, text)
    if m.group(1) is None and (begin in text and end in text):
        return ''
    return m.group(2)


if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')
