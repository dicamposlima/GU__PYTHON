"""Core Model Test"""
import uuid

from django.test import TestCase
from model_mommy import mommy

from core.models import get_file_path


class GetFilePathTestCase(TestCase):
    def setUp(self) -> None:
        self.filename = f'{uuid.uuid4()}.png'

    def test_get_file_path(self):
        arquivo = get_file_path(None, 'teste.png')
        self.assertTrue(len(arquivo), len(self.filename))


class ServiceTestCase(TestCase):
    def setUp(self) -> None:
        self.service = mommy.make('Service')

    def test_str(self):
        self.assertEqual(str(self.service), self.service.service)


class PositionTestCase(TestCase):
    def setUp(self) -> None:
        self.position = mommy.make('Position')

    def test_str(self):
        self.assertEqual(str(self.position), self.position.position)


class TeamTestCase(TestCase):
    def setUp(self) -> None:
        self.team = mommy.make('Team')

    def test_str(self):
        self.assertEqual(str(self.team), self.team.name)
