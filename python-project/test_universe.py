from universe import try_matplotlib
import builtins

sum_builtin_used = False


def new_sum(x):
    global sum_builtin_used
    sum_builtin_used = True
    return orig_sum(x)


orig_sum = builtins.sum
builtins.sum = new_sum


def send_msg(channel, msg):
    print("TECHIO> message --channel \"{}\" \"{}\"".format(channel, msg))


def success():
    print("TECHIO> success false")
    print("TECHIO> open -s /project/target/www index.html")
    print('Finished')
 
def fail():
    print("TECHIO> success false")
    

def test_count_all_stars():
    try:
        try_matplotlib()
        success()
    except AssertionError as e:
        fail()
        send_msg("Oops! 🐞", e)


if __name__ == "__main__":
    test_count_all_stars()
