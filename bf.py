def increment(x):
    return "+" * x


def decrement(x):
    return "-" * x


def shift_right(x):
    return ">" * x


def shift_left(x):
    return "<" * x


def output():
    return "."


def input():
    return ","


def open_loop():
    return "["


def close_loop():
    return "]"


def output_word(str):
    res = ""
    for char in str:
        res += increment(ord(char))
        res += output()
        res += shift_right(1)
    return res


def main():
    # bf_prog = ""
    # for i in range(15, 29):
    #     bf_prog += increment(i)
    #     bf_prog += output()
    #     bf_prog += shift_right(1)
    bf_prog = output_word("hello world!")

    f = open("program.bf", "w")
    f.write(bf_prog)
    f.close()
    print(bf_prog)


if __name__ == "__main__":
    main()
