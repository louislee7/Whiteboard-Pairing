def reconstructTrip(tickets):
        route = [None]*(len(tickets)-1)
        dict = {}
        for ticket in tickets:
            if ticket[0] == None:
                route[0] = ticket[1]
            else:
                dict[ticket[0]] = ticket[1]
        for i in range(1, len(tickets) - 1):
            route[i] = dict[route[i-1]]
        return route

##Test
myTickets = [
  ['PIT', 'ORD'],
  ['XNA', 'CID'],
  ['SFO', 'BHM'],
  ['FLG', 'XNA'],
  [None, 'LAX'], 
  ['LAX', 'SFO'],
  ['CID', 'SLC'],
  ['ORD', None],
  ['SLC', 'PIT'],
  ['BHM', 'FLG'],
]

print(reconstructTrip(myTickets))  # should print [ 'LAX', 'SFO', 'BHM', 'FLG', 'XNA', 'CID', 'SLC', 'PIT', 'ORD' ]
