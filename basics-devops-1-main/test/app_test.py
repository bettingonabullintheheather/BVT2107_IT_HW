import sys
import os
sys.path.append(sys.path[0][0:sys.path[0].rindex(os.sep)])
from src.app import app


def test_main() -> None:
    test_table = [
        [4, 2, 'plus', 6],   
        [0, 0, 'plus', 0],
        ['aaaaaaaaa', 42, 'plus', "Неверный тип данных"],
        [42, 'aaaaaaaaaaaa', 'plus', "Неверный тип данных"],
        ['aaaaaaaaa', 'aaaaaAAA', 'plus', "Неверный тип данных"],
        [42, -42, 'minus', 84],
        [4, 2, 'minus', 2],
        [-42, -42, 'minus', 0], 
        [4, -2, 'minus', 6],
        [42, 'sdfsdfsdf', 'minus', "Неверный тип данных"],
        ['sdfsdas', 42, 'minus', "Неверный тип данных"],
        ['sdfsdas', 'sdfsdfsdf', 'minus', "Неверный тип данных"],
        [42, -2, 'mult', -84],
        [-42, -4, 'mult', 168],
        [4, 2, 'del', 2.0],
        [2, 4, 'del', 0.5],  
        [42, 0, 'del', "Деление на ноль"],
        [0, 42, 'del', 0.0],
        [0, 0, 'del', "Деление на ноль"],
        [42, 42, 'TYSDH', "Неверный операнд"]
        ]
    with app.test_client() as client:
        for test_case in test_table:
            PATH = "/?first_numb={}&second_numb={}&operator={}".format(
                str(test_case[0]),
                str(test_case[1]),
                str(test_case[2])
                )
            response = client.get(PATH)
            assert response.status_code == 200
            assert response.json["rezult"] == test_case[3]