"""
coding: utf8
@time: 2020/12/13 19:55
@author: cjr
@file: factory_method.py
"""

"""
应用：
1、django框架使用工厂方法来创建表单字段
2、实际工作中我们可以创建更多的工厂方法，并且将逻辑上具有相似性的对象创建过程划分为一个分组
优点：
1、工厂方法将对象的创建过程集中化，更方便追踪对象的创建过程
2、将对象的使用和创建解耦。
3、工厂方法将在绝对必要时候才创建新对象，以提升性能以及内存使用率
"""


# 下面的例子完成了一个工厂方法，用来读取json文件或者XML文件

import json
import xml.etree.ElementTree as etree


class JSONDataExtractor:
    def __init__(self, filepath):
        self.data = {}
        with open(filepath, mode='r', encoding='utf8') as f:
            self.data = json.load(f)

    @property
    def parsed_data(self):
        return self.data


class XMLDataExtractor:
    def __init__(self, filepath):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data(self):
        return self.tree


def data_extraction_factory(filepath):
    if filepath.endswith('json'):
        extraction = JSONDataExtractor
    elif filepath.endswith('xml'):
        extraction = XMLDataExtractor
    else:
        raise ValueError(f'Cannot extract data from {filepath}')
    return extraction(filepath)


def extract_data_from(filepath):
    factory_obj = None
    try:
        factory_obj = data_extraction_factory(filepath)
    except ValueError as e:
        print(e)
    return factory_obj


def main():
    sqlite_factory = extract_data_from('data/person.sql')
    print(sqlite_factory)

    json_factory = extract_data_from('data/movies.json')
    movies = json_factory.parsed_data
    print(f'Found: {len(movies)} movies')
    for movie in movies:
        year = movie['year']
        if year:
            print(f'Year: {year}')
        director = movie['director']
        if director:
            print(f'director: {director}')

    xml_factory = extract_data_from('data/person.xml')
    person = xml_factory.parsed_data
    liars = person.findall(f'.//person[lastName="Liar"]')
    print(f'Found: {len(liars)} person')


if __name__ == '__main__':
    main()
