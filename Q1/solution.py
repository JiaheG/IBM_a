def read_data():
    len_stock = int(input())
    stock_str = input()
    stock = stock_str.strip().split(' ')

    len_request = int(input())
    request_str = input()
    request = request_str.strip().split(' ')
    return stock, request
def can_fulfill_requests(sizes_available, requests):
    # find max in stock
    stock_max = -1000
    for w in instore:
        if 'L' in w:
            stock_max = max(len(w)-1, stock_max)
        elif 'S' in w:
            stock_max = max(-len(w), stock_max)
        else: 
            stock_max = 0

    # find min in stock
    request_max = -1000
    for w in requests:
        if 'L' in w:
            request_max = max(len(w)-1, request_max)
        elif 'S' in w:
            request_max = max(-len(w), request_max)
        else: 
            request_max = 0
    # print(stock_max,request_max)
    res = True if stock_max>=request_max else False
    if res:
        print("Yes")
    else:
        print('No')
    return res

instore,request  = read_data()
ans = can_fulfill_requests(instore,request)
