import unittest
from unittest import TestCase
import requests


class MainTest(TestCase):
    API_URL = 'http://127.0.0.1:5000/api'
    CONTRIBUYENTES_URL = f'{API_URL}/contribuyentes'
    FOLDERS_URL = f'{API_URL}/folders'

    fake_contribuyente = {
        'name': 'Test',
        'ruc': '00557'
    }

    contrib_expected_result = {
        'contribuyente': {
            'id': 1,
            'name': 'Yvan',
            'ruc': '5255645'
        }
    }

    fake_contribuyente_update = {
        'name': 'Martha',
        'ruc': '00000215'
    }

    fake_folder = {
        'contribuyente_id': 1,
        'color': 'Test2',
        'time': 'Test 2022'
    }

    folder_expected_result = {
        "color": "Blanco",
        "contribuyente_id": 1,
        "id": 1,
        "time": "Julio 2022"
    }

    fake_folder_update = {
        'contribuyente_id': 1,
        'color': 'Verde',
        'time': 'Agosto 2022'
    }

    def test_post_contribuyente(self):
        url = self.CONTRIBUYENTES_URL
        response = requests.post(url, json=self.fake_contribuyente)

        self.assertEqual(response.status_code, 201)
        print('Test post contribuyente completed')

    def test_get_contribuyentes(self):
        url = self.CONTRIBUYENTES_URL
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)
        print('Test get contribuyentes completed')

    def test_get_contribuyente(self):
        url = f'{self.CONTRIBUYENTES_URL}/1'
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), self.contrib_expected_result)
        print('Test get contribuyente completed')

    def test_update_contribuyente(self):
        url = f'{self.CONTRIBUYENTES_URL}/4'
        response = requests.put(url, json=self.fake_contribuyente_update)

        self.assertEqual(response.status_code, 200)
        print('Test update contribuyente completed')

    def test_delete_contribuyente(self):
        url = f'{self.CONTRIBUYENTES_URL}/6'
        response = requests.delete(url)

        self.assertEqual(response.status_code, 200)
        print('Test delete contribuyente completed')

    # Folders

    def test_post_folder(self):
        url = self.FOLDERS_URL
        response = requests.post(url, json=self.fake_folder)

        self.assertEqual(response.status_code, 201)
        print('Test post folder completed')

    def test_get_folders(self):
        url = self.FOLDERS_URL
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)
        print('Test get folders completed')

    def test_get_folder(self):
        url = f'{self.FOLDERS_URL}/1'
        response = requests.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertDictEqual(response.json(), self.folder_expected_result)
        print('Test get folder completed')

    def test_update_folder(self):
        url = f'{self.CONTRIBUYENTES_URL}/2'
        response = requests.put(url, json=self.fake_folder_update)

        self.assertEqual(response.status_code, 200)
        print('Test update folder completed')

    def test_delete_folder(self):
        url = f'{self.CONTRIBUYENTES_URL}/3'
        response = requests.delete(url)

        self.assertEqual(response.status_code, 200)
        print('Test delete folder completed')


if __name__ == '__main__':
    unittest.main()
