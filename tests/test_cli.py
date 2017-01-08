#! /usr/bin/env python
# -*- coding: utf-8 -*-
#
# vim: fenc=utf-8
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4
#
#

"""
File name: test.py
Author: dhilipsiva <dhilipsiva@gmail.com>
Date created: 2016-12-29
"""

from click.testing import CliRunner
from hostscli.cli import websites

runner = CliRunner()


def test_hostscli():
    result = runner.invoke(websites)
    assert 'Available Websites:' in result.output
    assert 'test' in result.output
    assert result.exit_code == 0


test_hostscli()
