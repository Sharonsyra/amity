"""
Usage:
    amity create_room (living_space|office) <room_name>...
    amity add_person <first_name> <last_name> (fellow|staff)
    [<wants_accommodation>]
    amity print_room <room_name>
    amity print_unallocated [--file=text_file]
    amity print_allocations [--file=text_file]
    amity reallocate_person <person_id> <new_room>
    amity save_state [--db=sqlite_database]
    amity load_state <db>
    amity load_state <text_file>
    amity print_person_id
    amity (-i | --interactive)
    amity (-h | --help | --version)
Options:
    -i, --interactive  Interactive Mode
    -h, --help  Show this screen and exit.
"""

import sys
import cmd
from docopt import docopt, DocoptExit
from pyfiglet import figlet_format
from termcolor import cprint

from app.amity import Amity

amity = Amity()


def docopt_cmd(func):
    """To provide a decorator used to simplify the try/except block.
    and pass the result of the docopt parsing to the called action.
    """

    def fn(self, arg):
        try:
            opt = docopt(fn.__doc__, arg)

        except DocoptExit as e:
            # The DocoptExit is thrown when the args do not match.
            # We print a message to the user and the usage block.

            print('Invalid Command!')
            print(e)
            return

        except SystemExit:
            # The SystemExit exception prints the usage for --help
            # We do not need to do the print here.

            return

        return func(self, opt)

    fn.__name__ = func.__name__
    fn.__doc__ = func.__doc__
    fn.__dict__.update(func.__dict__)
    return fn


class Amity(cmd.Cmd):
    """Define contain methods/commands for docopt interface on terminal."""

    def intro():
        """Contain introductory message when in interactive mode."""
        cprint(figlet_format("Amity", font="univers"), "blue")
        cprint(__doc__)

    intro = intro()
    prompt = '(Amity) '
    file = None

    @docopt_cmd
    def do_create_room(self, args):
        """Usage: create_room (living_space|office) <room_name>..."""
        room_type = None
        if args["office"]:
            room_type = "office"
        else:
            room_type = "living_space"

        amity.create_room(args["<room_name>"], room_type)

    @docopt_cmd
    def do_add_person(self, args):
        """Usage: add_person <first_name> <last_name> (fellow|staff)
        [<wants_accommodation>]"""
        person_type = None
        if args["fellow"]:
            person_type = "fellow"
        elif args["staff"]:
            person_type = "staff"
        first_name = args["<first_name>"]
        last_name = args["<last_name>"]
        amity.add_person(first_name, last_name, person_type, args
                         ["<wants_accommodation>"])

    @docopt_cmd
    def do_print_room(self, args):
        """Usage: print_room <room_name>"""
        room_name = args["<room_name>"]
        amity.print_room(room_name)

    @docopt_cmd
    def do_print_unallocated(self, args):
        """Usage: print_unallocated [--file=text_file]"""
        if args["--file"]:
            print(args["--file"])
            amity.print_unallocated(args["--file"])
        amity.print_unallocated()

    @docopt_cmd
    def do_print_allocations(self, args):
        """Usage: print_allocations [--file=text_file]"""
        if args["--file"]:
            print(args["--file"])
            print(amity.print_allocations(args["--file"]))
        amity.print_allocations()

    @docopt_cmd
    def do_reallocate_person(self, args):
        """Usage: reallocate_person <person_id> <new_room>"""
        if args["<person_id>"].isalpha():
            print("person id cannot be string")
            return
        else:
            (amity.reallocate_person(int(args['<person_id>']),
                                     args['<new_room>']))

    @docopt_cmd
    def do_save_state(self, args):
        """Usage: save_state [--db=sqlite_database]"""
        # print(args['--db'])
        amity.save_state(args['--db'])

    @docopt_cmd
    def do_load_state(self, args):
        """Usage: load_state <db>"""
        db_name = args["<db>"]
        amity.load_state(db_name)

    @docopt_cmd
    def do_load_people(self, args):
        """Usage: load_state <text_file>"""
        amity.load_people(args["<text_file>"])

    @docopt_cmd
    def do_print_person_id(self, args):
        """ Usage: print_person_id """
        amity.print_person_id()

    def do_quit(self, args):
        """Quits out of Interactive Mode."""

        print('Ciao Adios!!')
        exit()


opt = docopt(__doc__, sys.argv[1:])

if opt['--interactive']:
    Amity().cmdloop()

print(opt)
