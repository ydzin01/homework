def tag(tag, text):
    a = {
        "a",
        "abbr",
        "b",
        "body",
        "caption",
        "cite",
        "code",
        "div",
        "form",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "i",
        "s",
    }
    return f"<{tag}>{text}</{tag}>" if tag in a else "Введён неверный тег"


print(tag(input(), input()))
