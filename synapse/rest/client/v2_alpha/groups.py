# -*- coding: utf-8 -*-
# Copyright 2017 Vector Creations Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from twisted.internet import defer

from synapse.http.servlet import (
    RestServlet, parse_string, parse_integer
)
from synapse.events.utils import (
    serialize_event, format_event_for_client_v2_without_room_id,
)

from ._base import client_v2_patterns

import logging

logger = logging.getLogger(__name__)


class GroupRoomServlet(RestServlet):
    PATTERNS = client_v2_patterns("/group/(?P<room_id>[^/]*)/rooms$", releases=())

    def __init__(self, hs):
        super(GroupRoomServlet, self).__init__()
        self.store = hs.get_datastore()
        self.auth = hs.get_auth()
        self.clock = hs.get_clock()

    @defer.inlineCallbacks
    def on_GET(self, request):
        requester = yield self.auth.get_user_by_req(request)
        user_id = requester.user.to_string()

        # TODO

        defer.returnValue((200, {}))


def register_servlets(hs, http_server):
    GroupRoomServlet(hs).register(http_server)
