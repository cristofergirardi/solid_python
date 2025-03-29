from datetime import datetime


if __name__ == '__main__':
    date = '27/03/25'
    # date_parts = date.split('/')
    date2 = datetime.strptime(date, '%d/%m/%y').strftime('%Y-%m-%d')
    print(date2)
    # print(date_parts)
    # new_date = '20' + '-'.join(reversed(date_parts))
    # print(new_date)
    # print(date2.strptime(date, '%Y-%m-%d'))
    # print(date2.strftime('%Y-%m-%d'))

    