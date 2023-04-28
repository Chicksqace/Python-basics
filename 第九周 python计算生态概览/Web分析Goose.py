#!/usr/bin/env python
# -- coding: utf-8 --
# @Time : 2023/4/27 21:54
# @File : Web分析Goose.py
from goose import Goose
url = 'http://www.elmundo.es/elmundo/2012/10/28/espana/1351388909.html'
g = Goose({'use_meta_language': False, 'target_language':'es'})
article = g.extract(url=url)
article.cleaned_text[:150]