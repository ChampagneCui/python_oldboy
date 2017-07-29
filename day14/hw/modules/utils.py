#!/usr/bin/env python
#_*_coding:utf-8_*_
import yaml

try:
	from yaml import CLoader as Loader, CDumper as Dumper
except ImportError:
	from yaml import Loader, Dumper


def print_err(msg, quit=False):
	output = "\033[31;1mError: %s\033[0m" % msg
	if quit:
		exit(output)
	else:
		print(output)


def yaml_parser(yml_filename):
	try:
		yaml_file = open(yml_filename, 'r',encoding='utf-8')
		data = yaml.load(yaml_file)
		return data
	except Exception as e:
		print_err(e)
