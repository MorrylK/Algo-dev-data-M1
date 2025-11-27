from appmeteo.test.test import Test
from appmeteo.test.test_missing import TestMissing


class TestBatch(Test):
    @staticmethod
    def test(data):
        for i in range(data.shape[0]):
            if not TestMissing.test(data.iloc[i]):
                #print(f"Erreur ligne {i}")
                return False
            else:
                return True