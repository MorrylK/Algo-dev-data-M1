from appmeteo.Test.Test import Test
from appmeteo.Test.TestMissing import TestMissing


class TestBatch(Test):
    @staticmethod
    def test(data):
        for i in range(data.shape[0]):
            if not TestMissing.test(data.iloc[i]):
                #print(f"Erreur ligne {i}")
                return False
            else:
                return True