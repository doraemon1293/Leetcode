import collections


class Solution:
    def invalidTransactions(self, transactions: list) -> list:
        d = collections.defaultdict(dict)
        invalids = set()
        transactions.sort(key=lambda x: int(x.split(",")[1]))
        for transaction in transactions:
            name, minute, amount, city = transaction.split(",")
            minute = int(minute)
            amount = int(amount)
            if amount > 1000:
                invalids.add(",".join([name, str(minute), str(amount), city]))
            for other_city in d[name]:
                if other_city != city:
                    for minute1, amount1 in d[name][other_city][::-1]:
                        if minute - minute1 <= 60:
                            invalids.add(",".join([name, str(minute1), str(amount1), other_city]))
                            invalids.add(",".join([name, str(minute), str(amount), city]))
                        else:
                            break
            d[name].setdefault(city, [])
            d[name][city].append((minute, amount))
        return invalids
transactions=["bob,689,1910,barcelona","alex,696,122,bangkok","bob,832,1726,barcelona","bob,820,596,bangkok","chalicefy,217,669,barcelona","bob,175,221,amsterdam"]
print(Solution().invalidTransactions(transactions))