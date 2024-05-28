from praktikum.car import Car


class TestCar:

    def test_car_weight(self, mock_engine, mock_frame):
        testCar = Car("test data engine")
        testCar.set_engine(mock_engine)
        testCar.set_frame(mock_frame)

        expected_result = (mock_engine.get_weight() + mock_frame.get_weight()) * 1.2

        assert testCar.get_weight() == expected_result
