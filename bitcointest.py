import unittest
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin

class TestBitCoin(TestCase):

    @patch('bitcoin.getBitcoinRate')
    def test_get_usd_price(self, mock_rates):
        mock_rate = 8594.25
        example_api_response = {'rate': mock_rate}
        mock_rates.side_effect = [ example_api_response ]
        bitcoins = float(bitcoin.getCoins())
        expected = bitcoins * mock_rate
        converted = bitcoin.convert(mock_rate, bitcoins)
        self.assertEqual(expected, converted)


##Tests my convert function in bitcoin.py
##I have a mock rate and an example api response
##calls get coins to get user input of coins, calculates
##expected conversion, compares it with what my function does
## and asserts they are the same