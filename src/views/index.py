#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Blueprint, render_template
from ..utils.http import success

bp = Blueprint('', __name__)
prefix = ''


@bp.route('/', methods=['GET'])
def index():
    return success()


@bp.route("/i18n", methods=['GET'])
def i18n_test():
    """
    国际化测试
    :return:
    """
    return render_template("i18n/i18n.html")


@bp.route("/test", methods=['GET'])
def test():
    return render_template("test.html")


@bp.route('/web', methods=['GET'])
def web():
    import subprocess

    commands = '''
        cd src/bdd/web
        lettuce
    '''

    process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = process.communicate(commands.encode('utf-8'))
    print out.decode('utf-8')

    return success()


@bp.route('/ios', methods=['GET'])
def ios():
    import subprocess

    commands = '''
        cd src/bdd/ios
        py.test ios_simple.py
    '''

    process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = process.communicate(commands.encode('utf-8'))
    print out.decode('utf-8')

    return success()


@bp.route('/android', methods=['GET'])
def android():
    import subprocess

    commands = '''
        cd src/bdd/android
        py.test android_simple.py
    '''

    process = subprocess.Popen('/bin/bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = process.communicate(commands.encode('utf-8'))
    print out.decode('utf-8')

    return success()