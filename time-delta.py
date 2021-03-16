import datetime
format_string = "%a %d %b %Y %H:%M:%S %z"


def delta(t1, t2):

    parsed_t1 = datetime.datetime.strptime(t1, format_string)
    parsed_t2 = datetime.datetime.strptime(t2, format_string)
    diff = parsed_t2 - parsed_t1
    return (int(abs(diff.total_seconds())))


if __name__ == "__main__":
    # t1 = input()
    # t2 = input()
    t1 = "Sun 10 May 2015 13:54:36 -0700"
    t2 = "Sun 10 May 2015 13:54:36 -0000"
    print(delta(t1, t2))
