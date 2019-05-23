import unittest

from envelopes.envelopes_checking import Envelope


class TestEnvelope(unittest.TestCase):

    def test_contains(self):
        envelope1 = Envelope('7', '6')
        envelope2 = Envelope('3', '5')
        self.assertTrue(envelope1.contains(envelope2))
        self.assertFalse(envelope2.contains(envelope1))

    def test_negative_validation(self):
        height = '-2'
        width = '10'
        with self.assertRaises(ValueError):
            Envelope(width, height)

    def test_text_validation(self):
        height = 'shhs'
        width = '10'
        with self.assertRaises(ValueError):
            Envelope(width, height)

    def test_when_height_bigger_width(self):
        height = '15'
        width = '10'
        self.assertEqual(Envelope(width, height).width, 15)


if __name__ == '__main__':
    unittest.main()
