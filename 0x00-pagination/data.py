#!/usr/bin/env python3

import type_annotations_generator

data = {'page_size': 2, 'page': 2, 'data': [['2016', 'FEMALE' 'ASIAN AND PACIFIC ISLANDER' 'Olivia', '172', '1'], ['2016', 'FEMALE' 'ASIAN AND PACIFIC ISLANDER', 'Emma', '112', '2']], 'next_page': 2, 'prev_page': None, 'total_pages': 9709}

print(type_annotations_generator.generate_annotations(data))
