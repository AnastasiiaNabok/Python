import unittest

from envelopes.envelopes_checking import Envelope


class TestEnvelope(unittest.TestCase):

    def test_contains(self):
        envelope1 = Envelope(7,6)
        envelope2 = Envelope(3,5)
        self.assertTrue(envelope1.contains(envelope2))
        self.assertFalse(envelope2.contains(envelope1))


if __name__ == '__main__':
    unittest.main()
