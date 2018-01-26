# -*- coding: utf-8 -*-
import wda

c = wda.Client()
s = c.session()
c.screenshot('screenshot.png')