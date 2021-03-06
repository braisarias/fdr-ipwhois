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


class ConnectionInfo(object):
    """Class that encapsulates info about a connection."""

    def check_ip(self, ip):
        import re
        COMPLEX_IP_REGEX = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25" + \
            "[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
        regex = re.compile(COMPLEX_IP_REGEX)
        return regex.match(ip) is not None

    def check_port(self, port):
        try:
            num = int(port)
            return num > 0 and num < 65535
        except ValueError:
            return False

    def check_dir(self, direct):
        return direct.lower() in ("incoming", "outgoing")

    def __init__(self, ip_orig, port_orig, ip_dest, port_dest, proto,
                 direction, size_in, size_out, nat_ip, nat_port):
        super(ConnectionInfo, self).__init__()
        if not self.check_ip(ip_orig):
            raise ValueError("IP origen")
        if not self.check_ip(ip_dest):
            raise ValueError("IP dest")
        if not self.check_ip(nat_ip):
            raise ValueError("NAT IP")
        if port_orig != "" and not self.check_port(port_orig):
            raise ValueError("port origen")
        if port_orig != "" and not self.check_port(nat_port):
            raise ValueError("NAT PORT")
        if port_dest != "" and not self.check_port(port_dest):
            raise ValueError("Port dest")
        if direction != "" and not self.check_dir(direction):
            raise ValueError("Direction")
        self.ip_orig = ip_orig
        self.port_orig = port_orig
        self.proto = proto
        self.ip_dest = ip_dest
        self.port_dest = port_dest
        self.dir = direction
        self.number = 0
        self.size_in = float(size_in)
        self.size_out = float(size_out)
        self.port_nat = nat_port
        self.ip_nat = nat_ip

    def json_dump(self):
        return {"ip_orig": self.ip_orig,
                "port_orig": self.port_orig,
                "ip_dest": self.ip_dest,
                "port_dest": self.port_dest,
                "proto": self.proto,
                "dir": self.dir,
                "number": self.number,
                "size_in": self.size_in,
                "size_out": self.size_out,
                "ip_nat": self.ip_nat,
                "port_nat": self.port_nat
                }

    def __eq__(self, other):
        my_important_port = self.port_dest if self.dir.lower() == "outgoing" else self.port_orig
        other_important_port = other.port_dest if other.dir.lower() == "outgoing" else other.port_orig
        return my_important_port == other_important_port \
               and self.proto == other.proto \
               and self.ip_dest == other.ip_dest \
               and self.ip_orig == other.ip_orig \
               and self.dir == other.dir
