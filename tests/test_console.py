import unittest
from unittest.mock import patch
from io import StringIO
import console
import models


class TestHBNBCommand(unittest.TestCase):
    def setUp(self):
        self.console = console.HBNBCommand()

    def tearDown(self):
        self.console = None

    @patch('sys.stdout', new_callable=StringIO)
    def test_help_show(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("help show")
        self.assertIn("Prints string representation", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("create BaseModel")
        self.assertTrue(len(mock_stdout.getvalue()) > 0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        models.storage.new(models.BaseModel())
        models.storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("show BaseModel {}".format(
                list(models.storage.all().keys())[0].split(".")[1]))
        self.assertIn(str(models.storage.all().popitem()[1]),
                      mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        models.storage.new(models.BaseModel())
        models.storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("destroy BaseModel {}".format(
                list(models.storage.all().keys())[0].split(".")[1]))
        self.assertFalse(models.storage.all())

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        models.storage.new(models.BaseModel())
        models.storage.new(models.User())
        models.storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("all BaseModel")
        self.assertIn(str(models.storage.all().popitem()[1]),
                      mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        models.storage.new(models.BaseModel())
        models.storage.save()
        with patch('sys.stdout', new=StringIO()) as f:
            self.console.onecmd("update BaseModel {} name 'New Name'".format(
                list(models.storage.all().keys())[0].split(".")[1]))
        self.assertEqual("New Name\n",
                         models.storage.all().popitem()[1].name)


if __name__ == '__main__':
    unittest.main()
