from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.test import TestCase
from django.test import Client
from mock import *
import json
from web.models import *
from web.views import *
import urllib.request

import web.urls
from codex.baseerror import InputError

class TestValidateUser(TestCase):
    fixtures = ['users.json','courses.json','posts.json']
#以下内容暂时可忽略
    def setUp(self):
        self.client = Client()

    def test_get_without_openid(self):
        found = resolve('/login/', urlconf=userpage.urls)
        request = Mock(wraps=HttpRequest(), method='GET')
        request.body = Mock()
        request.body.decode = Mock(return_value='{}')
        response = json.loads(found.func(request).content.decode())
        self.assertEqual(response['code'], 1)

    def test_get_with_openid(self):
        found = resolve('/login/', urlconf=userpage.urls)
        request = Mock(wraps=HttpRequest(), method='GET')
        request.body = Mock()
        request.body.decode = Mock(return_value='{"openid": "1"}')
        with patch.object(User, 'get_by_openid', return_value=Mock(student_id=1)) as MockUser:
            response = json.loads(found.func(request).content.decode())
            self.assertEqual(response['code'], 0)

    def test_validate_user_raise_error_without_input(self):
        user_bind_view = UserBind()
        with self.assertRaises(ValidateError):
            user_bind_view.validate_user()

    @patch('urllib.request.urlopen')
    def test_validate_user_with_username_password(self, mock_open: MagicMock):
        user_bind_view = UserBind()
        user_bind_view.input = {'student_id': '1', 'password': 'x'}
        mock_response = MagicMock()
        mock_response.read = MagicMock(return_value=b'{"ticket":"ticket","status":"RESTLOGIN_OK"}')
        mock_open.return_value = MagicMock()
        mock_open.return_value.__enter__ = MagicMock(return_value=mock_response)
        user_bind_view.validate_user()
        self.assertTrue(mock_open.called)

        mock_open.assert_called_once_with(
            'https://id.tsinghua.edu.cn/do/off/ui/auth/login/post/fa8077873a7a80b1cd6b185d5a796617/0?/j_spring_security_thauth_roaming_entry',
            b'username=1&password=x'
        )
        self.assertTrue(mock_response.read.called)

    
    @patch('urllib.request.urlopen')
    def test_validate_user_with_wrong_username_password(self, mock_open: MagicMock):
        user_bind_view = UserBind()
        user_bind_view.input = {'student_id': 1, 'password': 'x'}
        mock_response = MagicMock()
        mock_response.read = MagicMock(return_value=b'{"authCode":261,"status":"RESTLOGIN_ERROR_AUTH"}')
        mock_open.return_value = MagicMock()
        mock_open.return_value.__enter__ = MagicMock(return_value=mock_response)
        with self.assertRaises(ValidateError):
            user_bind_view.validate_user()
            self.assertTrue(mock_open.called)
            mock_open.assert_called_once_with(
                'https://id.tsinghua.edu.cn/do/off/ui/auth/login/post/fa8077873a7a80b1cd6b185d5a796617/0?/j_spring_security_thauth_roaming_entry',
                b'username=1&password=x'
            )
            self.assertTrue(mock_response.read.called)

    def test_post_with_wrong_info(self):
        response = self.client.post('/api/u/user/bind', {'openid': '1', 'student_id': '2014013460', 'password': 'wrong'})
        result = json.loads(response.content.decode())
        self.assertGreater(result['code'], 0)
    
    def test_post_with_right_info(self):
        response = self.client.post('/api/u/user/bind', {'openid': '1', 'student_id': '2014013460', 'password': 'wrong'})
        result = json.loads(response.content.decode())
        self.assertEqual(result['code'], 0)

#以上内容暂时可忽略
