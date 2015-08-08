import mock

from unittest import TestCase
from rest_framework.response import Response

from web_ide.common.utils import custom_exception_handler


class CustomExceptionHandlerTest(TestCase):

    @mock.patch('web_ide.common.utils.exception_handler')
    @mock.patch('web_ide.common.utils.DEBUG', False)
    def test_exception_handler(self, mock_exception_handler):

        reason = 'validation failed'
        exception = Exception(reason)
        expected_resp_data = {'error': reason}

        resp = custom_exception_handler(exception, None)

        self.assertTrue(mock_exception_handler.called)
        self.assertIsInstance(resp, Response)
        self.assertEqual(resp.data, expected_resp_data)
