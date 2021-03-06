#!/usr/bin/python
# -*- coding: utf-8 -*-

# "Con quien carallo estoy conectado"
# Copyright (C) 2014  Marcos Chavarría Teijeiro.

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


try:
    from setuptools import setup
except ImportError:
    print "You must have setuptools package installed. Try \"sudo apt-get" + \
          " install python-setuptools\""
    quit()

dependency_links = ["git+https://github.com/juliensobrier/google-safe-browsing-lookup-python.git#egg=google-safe-browsing-lookup-python",
                    "git+https://github.com/ftao/python-ifcfg.git#egg=ifcfg"]
install_requires = ["requests", "BeautifulSoup", "whois", "python-nmap",
                    "ifcfg"]

setup(
    name="CQCEC",
    version="0.97Beta",
    scripts=["cqcec", "conn_hist_daemon"],
    packages=["cqcec_lib"],
    dependency_links=dependency_links,
    install_requires=install_requires,
    data_files=[('/etc', ["cqcec_config.cfg"])]
)
