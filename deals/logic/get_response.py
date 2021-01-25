from deals.models import HistoryDeals


# class Client:
#     def __init__(self, username, spent_money, gems):
#         self.username = username
#         self.spent_money = spent_money
#         self.gems = gems


def sort_data():
    try:
        last_history = HistoryDeals.objects.all().order_by('-id')[0]
    except IndexError:
        raise RuntimeError("No have data in database")
    deals = last_history.deal_set.all()

    clients = {}
    for deal in deals:
        if deal.customer in clients:
            clients[deal.customer]['spent_money'] += deal.total  # sum for all deals
            clients[deal.customer]['gems'].add(deal.item)

        else:
            clients[deal.customer] = {}
            clients[deal.customer]['username'] = deal.customer
            # clients[deal.customer]['item'] = deal.item
            clients[deal.customer]['spent_money'] = deal.total
            # clients[deal.customer]['quantity'] = deal.quantity
            # clients[deal.customer]['date'] = deal.date
            clients[deal.customer]['gems'] = set([deal.item])

    # names of five buyers
    five_clients = sorted(clients.keys(), key=lambda x: clients[x]['spent_money'], reverse=True)[:5]    #

    # for five_clients
    all_gems = [gem for client in five_clients for gem in clients[client]['gems']]
    gem_count_two_or_more = set()
    for gem in all_gems:
        if all_gems.count(gem) >= 2:
            gem_count_two_or_more.add(gem)

    # intersection gems
    for cl in five_clients:
        clients[cl]['gems'] = list(clients[cl]['gems'].intersection(gem_count_two_or_more))

    return [clients[cl] for cl in five_clients]
