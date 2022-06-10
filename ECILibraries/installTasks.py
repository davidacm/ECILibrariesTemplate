# -*- coding: UTF-8 -*-
#Copyright (C) 2009 - 2019 David CM, released under the GPL.
# Author: David CM <dhf360@gmail.com> and others.
TTSPath = r"..\..\eciLibraries"
dllName = "eci.dll"
import config
def onInstall():
	config.conf.profiles[0]['ibmeci'] = {}
	config.conf.profiles[0]['ibmeci']['TTSPath'] = TTSPath
	config.conf.profiles[0]['ibmeci']['dllName'] = dllName
	config.conf.save()