#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def get_descriptive_name(year,make,model):
        """返回简洁描述性信息"""
        long_name = str(year) + " " +make + " " + model
        return long_name.title()

