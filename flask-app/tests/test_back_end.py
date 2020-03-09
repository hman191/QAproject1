import unittest
import pytest
from flask import abort, url_for
from flask_testing import TestCase
from os import getenv
from application import app, db
from application.models import User, Deck, car_list

class TestBase(TestCase):

    def create_app(self):

        config_name = 'testing'
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        db.session.commit()
        db.drop_all()
        db.create_all()

        admin = User(username="admin", email="admin@test.com", password="admin")

        employee = User(username="user", email="test@test.com", password="user")

        db.session.add(admin)
        db.session.add(employee)
        db.session.commit()

    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()

class TestViews(TestBase):

    def test_homepage_view(self):
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get(url_for('login'))
        self.assertEqual(response.status_code, 200)

    def test_account_view(self):
        target_url = url_for('account', user_id=2)
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)

    def test_deck_view(self):
        target_url = url_for('deck', user_id=2)
        redirect_url = url_for('login', next=target_url)
        response = self.client.get(target_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, redirect_url)
