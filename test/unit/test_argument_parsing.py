import sys
import unittest.mock

from album.argument_parsing import create_parser

from album.server import argument_parsing


class TestArgumentParsing(unittest.TestCase):

    def test_create_parser(self):
        parser = create_parser()

        # check parsing of subcommands
        self.assertSubcommandParsed(parser, "server", argument_parsing.start_server, "1234")

    def assertSubcommandParsed(self, parser, name, method, arguments=None):
        sys.argv = ["", name]
        if arguments:
            sys.argv = sys.argv + [arguments]
        args = parser.parse_known_args()
        self.assertEqual(method, args[0].func)


if __name__ == '__main__':
    unittest.main()
