import logging
import os
import sys
from .conversation import Statement, Response
from . import utils


class Trainer(object):
    """
    Base class for all other trainer classes.
    """

    def __init__(self, storage, **kwargs):
        self.chatbot = kwargs.get('chatbot')
        self.storage = storage
        self.logger = logging.getLogger(__name__)
        self.show_training_progress = kwargs.get('show_training_progress', True)

    def get_preprocessed_statement(self, input_statement):
        """
        Preprocess the input statement.
        """

        # The chatbot is optional to prevent backwards-incompatible changes
        if not self.chatbot:
            return input_statement

        for preprocessor in self.chatbot.preprocessors:
            input_statement = preprocessor(self, input_statement)

        return input_statement

    def train(self, *args, **kwargs):
        """
        This method must be overridden by a child class.
        """
        raise self.TrainerInitializationException()

    def get_or_create(self, statement_text):
        """
        Return a statement if it exists.
        Create and return the statement if it does not exist.
        """
        temp_statement = self.get_preprocessed_statement(
            Statement(text=statement_text)
        )

        statement = self.storage.find(temp_statement.text)

        if not statement:
            statement = Statement(temp_statement.text)

        return statement

    class TrainerInitializationException(Exception):
        """
        Exception raised when a base class has not overridden
        the required methods on the Trainer base class.
        """

        def __init__(self, value=None):
            default = (
                'A training class must be specified before calling train(). ' +
                'See http://chatterbot.readthedocs.io/en/stable/training.html'
            )
            self.value = value or default

        def __str__(self):
            return repr(self.value)

    def _generate_export_data(self):
        result = []
        for statement in self.storage.filter():
            for response in statement.in_response_to:
                result.append([response.text, statement.text])

        return result

    def export_for_training(self, file_path='./export.json'):
        """
        Create a file from the database that can be used to
        train other chat bots.
        """
        import json
        export = {'conversations': self._generate_export_data()}
        with open(file_path, 'w+') as jsonfile:
            json.dump(export, jsonfile, ensure_ascii=False)

