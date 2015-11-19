import inspect
import sys
from pygments import highlight
from pygments.lexers import PythonLexer
from pygments.formatters import TerminalFormatter


def start():
    """
    Hi!
    Welcome to Python tips, tricks and dark magic
    I'm Jordi Soucheiron and I work @ serverdensity
    an awesome SaaS server and website monitoring tool.
    Feel free to ask any comments/questions during
    the presentation or over here:
      - @jordixou
      - jordi@soucheiron.cat

    You can download this presentation here:
    https://github.com/jsoucheiron/pybcn-talk-pttdm/
    """


def slide_1():
    """ This dictionary constructions are very usual,
    but we have better ways of handling this in python
    """
    my_dict = {'my_key': 'my_value'}
    key = 'my_key'
    if my_dict.has_key(key):
        print my_dict[key]
        del my_dict[key]
    else:
        print "default value"
    """ Or in a more pythonic way... (has_key is deprecated)"""
    if key in my_dict:
        print my_dict[key]
        del my_dict[key]
    else:
        print "default value"


def slide_1_1():
    """ Dictionaries have a get method with a default value.
    If the key doesn't exist it will return the default
    """
    my_dict = {
        'my_key': 'my_value'
    }
    print my_dict.get('my_key', 'default value')
    print my_dict.get('my_missing_key', 'default value')


def slide_1_2():
    my_dict = {
        'my_key': 'my_value'
    }
    print my_dict.pop('my_key', "I don't care if it doesn't exist")
    print my_dict.pop('my_key', "I don't care if it doesn't exist")
    print my_dict


def slide_2():
    """ Lists offer a wide variety of ways of accessing its elements.
    I'd like to show you a few you may not now
    """


def slide_2_1():
    """ Negative indexes
    """
    my_list = [1, 2, 3, 4, 5]
    print my_list[-1]


def slide_2_2():
    """ List slicing
    """
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    start = 1
    end = 8
    step = 2
    print my_list[start:end:step]
    print my_list[end:start:-step]
    print my_list[::-1]


def slide_2_3():
    """ List zipping
    """
    my_list_1 = ['a', 'b', 'c', 'd', 'e']
    my_list_2 = [1, 2, 3, 4, 5]
    print zip(my_list_1, my_list_2)


def slide_3():
    """ Advanced "and" and "or" usage.

    When concatenated, "and" will give back the value
    of the first non-true operand or True if the operands
    are True.
    When concatenated, "or" will give back the last non-true
    value if all arguments are False or the first True value.
    """
    print "---and---"
    print True and False and None
    print True and None and False
    print True and 1 and 10 < 20
    print "---or---"
    print True or False or None
    print True or None or False
    print False or None or 0


def my_wrong_append(value, my_list=[]):
    my_list.append(value)
    return my_list


def my_append(value, my_list=None):
    my_list = my_list or []
    my_list.append(value)
    return my_list


def slide_4():
    """ Default arguments are only evaluated once
    Assume we have this method (we do):

def my_wrong_append(value, my_list=[]):
    my_list.append(value)
    return my_list

    What's going to happen?
    """

    print my_wrong_append(1)
    print my_wrong_append(2)


def slide_4_1():
    """ So... unless you're doing it on purpose
    We can take advantadge of "or" and do this:

def my_append(value, my_list=None):
    my_list = my_list or []
    my_list.append(value)
    return my_list

    And now?
    """

    print my_append(1)
    print my_append(2)


def slide_5():
    """ Unpacking
    """

    a = 'rules!'
    b = 'Pybcn'

    a, b = b, a

    print "{0} {1}".format(a, b)


def slide_6():
    """ Exceptions

    Disclamer: DON'T EVER DO THIS. Unless:
      - You want everyone to hate you
      - You want the FSM to kill a kitten every time this code runs
    """

    try:
        """Some very dangerous stuff"""
    except:
        pass

    try:
        """Some very dangerous stuff"""
    except Exception:
        pass


def slide_6_1():
    try:
        try:
            raise KeyboardInterrupt()
        except Exception:
            print "We won't print this"
    except:
        print "We won't catch the exception with Exception."
        print "KeyboardInterrupt is not a subclass of Exception"
        print "only non-system-exiting exceptions are."
        print "But they are still a exceptions and can be captured"


def slide_7():
    """ Full try/except/else/finally flow
    """

    try:
        a = 0
    except:
        print "The exception won't be raised"
    else:
        print "We'll run the code in else if the exception is not raised"
    finally:
        print "and we'll always run finally (great for cleanup code)"


def print_point(x, y):
    print "({0}, {1})".format(x, y)


def slide_8():
    """ Other unpacking tricks:
    We have this helper function:
def print_point(x, y):
    print "({0}, {1})".format(x, y)
    """

    point_a = (3, 4)
    point_b = {'y': 4, 'x': 3}

    print_point(3, 4)
    print_point(*point_a)
    print_point(**point_b)


def slide_9():
    """ Chaining comparisons
    """

    x = 15
    y = 2 * x
    print 10 < x < 20 < y < 50
    print 20 < x > 10


def slide_10():
    """ In order to start a web file server on
    the current directory, simply run:
    python -m SimpleHTTPServer 5000
    """


def questions():
    """ That's all I have for now.
    If you have any questions I'll be happy to answer them :)

    I based most of this talk from the stuff I got from here:
    http://www.siafoo.net/article/52
    https://docs.python.org/3/library/functions.html
    http://stackoverflow.com/questions/101268/hidden-features-of-python
    http://sahandsaba.com/thirty-python-language-features-and-tricks-you-may-not-know.html
    """

def end():
    """ Thank you all!

    As a little present, you can access this link for a small Christmas gift:
        - https://www.serverdensity.com/meetup/
    """


def print_func(func):
    print "--- Code start ---"
    code = "".join(inspect.getsourcelines(func)[0])
    print highlight(code, PythonLexer(), TerminalFormatter(bg='dark'))
    print "--- Code end ---"


def print_func_result(func):
    print "--- Result start ---"
    func()
    print "--- Result end ---"


def index():
    r = ""
    for k, v in slides.iteritems():
        doc = inspect.getdoc(v[0])
        if doc is not None and k.isdigit():
            r += "{}: {}\n".format(k, doc.split('\n')[0])
    return r

def exit():
    sys.exit(0)


if __name__ == "__main__":
    next_slide = 'start'
    slides = {
        'start': (start, '1', False),
        '1': (slide_1, '1.1', True),
        '1.1': (slide_1_1, '1.2', True),
        '1.2': (slide_1_2, '2', True),
        '2': (slide_2, '2.1', False),
        '2.1': (slide_2_1, '2.2', True),
        '2.2': (slide_2_2, '2.3', True),
        '2.3': (slide_2_3, '3', True),
        '3': (slide_3, '4', True),
        '4': (slide_4, '4.1', True),
        '4.1': (slide_4_1, '5', True),
        '5': (slide_5, '6', True),
        '6': (slide_6, '6.1', False),
        '6.1': (slide_6_1, '7', True),
        '7': (slide_7, '8', True),
        '8': (slide_8, '9', True),
        '9': (slide_9, '10', True),
        '10': (slide_10, 'questions', False),
        'questions': (questions, 'end', False),
        'end': (end, 'exit', False),
        'exit': (exit, None, False),
        '0': (exit, None, False)
    }
    while True:
        try:
            print "Slide({0}):".format(next_slide)
            user_input = sys.stdin.readline().strip('\n')
            if user_input == '':
                user_input = next_slide

            func, next_slide, run = slides.get(
                user_input,
                (None, next_slide, False)
            )
            if func == exit:
                exit()
            elif func is not None:
                print_func(func)
                sys.stdin.readline()
                if run:
                    print_func_result(func)
                    sys.stdin.readline()
            else:
                print "Slide '{0}' not found. Available_slides:\n{1}".format(
                    user_input, index())
        except Exception:
            raise
        except:
            sys.exit(1)
