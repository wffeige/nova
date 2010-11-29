# vim: tabstop=4 shiftwidth=4 softtabstop=4

# Copyright (c) 2010 Citrix Systems, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

"""
Helper methods for operations related to the management of network records and
their attributes like bridges, PIFs, QoS, as well as their lookup functions.
"""

from twisted.internet import defer


class NetworkHelper():
    def __init__(self, session):
        return

    @classmethod
    @defer.inlineCallbacks
    def find_network_with_bridge(self, session, bridge):
        expr = 'field "bridge" = "%s"' % bridge
        networks = yield session.call_xenapi('network.get_all_records_where',
                                           expr)
        if len(networks) == 1:
            defer.returnValue(networks.keys()[0])
        elif len(networks) > 1:
            raise Exception('Found non-unique network for bridge %s' % bridge)
        else:
            raise Exception('Found no network for bridge %s' % bridge)
