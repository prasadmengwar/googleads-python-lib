#!/usr/bin/env python
#
# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This example gets all teams.
"""

# Import appropriate modules from the client library.
from googleads import dfp


def main(client):
  # Initialize appropriate service.
  team_service = client.GetService('TeamService', version='v201802')

  # Create a statement to select teams.
  statement = dfp.StatementBuilder()

  # Retrieve a small amount of teams at a time, paging
  # through until all teams have been retrieved.
  while True:
    response = team_service.getTeamsByStatement(statement.ToStatement())
    if 'results' in response and len(response['results']):
      for team in response['results']:
        # Print out some information for each team.
        print('Team with ID "%d" and name "%s" was found.\n' % (team['id'],
                                                                team['name']))
      statement.offset += statement.limit
    else:
      break

  print '\nNumber of results found: %s' % response['totalResultSetSize']


if __name__ == '__main__':
  # Initialize client object.
  dfp_client = dfp.DfpClient.LoadFromStorage()
  main(dfp_client)