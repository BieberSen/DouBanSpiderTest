#coding=utf-8
from bs4 import BeautifulSoup
import requests
import json
import time
import random
import fake_useragent


''' 获得传入url的解析数据，返回BeautifulSoup解析对象'''
def get_url_soup_obj(url):
    agent_list = [  'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0',
                    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36'
                ]
    cookie_list = ['bid=huBW9whOZO4; douban-fav-remind=1; ll="108288"; __utma=30149280.83978963.1501202332.1534991386.1540086444.5; __utmc=30149280; __utmz=30149280.1540086444.5.5.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; __utmb=30149280.1.10.1540086444; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1540086445%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.377904312.1540086445.1540086445.1540086445.1; __utmb=223695111.0.10.1540086445; __utmc=223695111; __utmz=223695111.1540086445.1.1.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __yadk_uid=aWWNLk4usDp5PDSJ3Ecya5xaOIYUXlKI; _vwo_uuid_v2=DF4C56CD8DE5B71DF8C4ADC7060B11FFC|e2198d7e91e17f22314249ffddac8eab; _pk_id.100001.4cf6=46b63bc59e350816.1540086445.1.1540086498.1540086445.',
                   'bid=ciaCskwM-B4; douban-fav-remind=1; __utmz=30149280.1539571568.1.1.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ll="108288"; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1540086732%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3D%25E8%25B1%2586%25E7%2593%25A3%26rsv_pq%3Dc1ea416c000087d4%26rsv_t%3DfbbehW4%252Fn2OEIH5jU9kpcbJtsBBrOho7TYuKrPwKOYwms5ygv3PU5jLOmkc%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug3%3D6%26rsv_sug1%3D6%26rsv_sug7%3D101%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1792192201.1539571568.1539571568.1540086732.2; __utmb=30149280.0.10.1540086732; __utmc=30149280; __utma=223695111.636155497.1540086732.1540086732.1540086732.1; __utmb=223695111.0.10.1540086732; __utmc=223695111; __utmz=223695111.1540086732.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; __yadk_uid=rUuvkYOfTNHKDX0l8bG4uvYGREmAA8Xo; _vwo_uuid_v2=DAAA5B0522697319C686272FDCB2E38BE|9c0fc19f503ebeaef98e0a12403634f4; _pk_id.100001.4cf6=4c2b2017e11718f7.1540086732.1.1540086748.1540086732.',
                   'bid=0kZGG-Zfv30; douban-fav-remind=1; ll="108288"; __yadk_uid=wWrSiJH5qAnviyTOcd6FqfCnpFdLWhHh; _vwo_uuid_v2=DEEC48C65E7DE43EADB1CFC93DF2F34B6|f9e3c725448c3cf8f3a215a8d07d2441; viewed="1011228"; gr_user_id=531d67a6-eb5a-4cb9-ba2f-6ad7aa1a06d1; __utmc=30149280; __utmc=223695111; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1540086761%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fwd%3D%25E8%25B1%2586%25E7%2593%25A3%26rsv_spt%3D1%26rsv_iqid%3D0xa65ba5e4000081e0%26issp%3D1%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D2%26ie%3Dutf-8%26tn%3Dbaiduhome_pg%26rsv_enter%3D1%26rsv_sug3%3D6%26rsv_sug1%3D6%26rsv_sug7%3D101%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.880355898.1536137890.1539925267.1540086761.4; __utmb=223695111.0.10.1540086761; __utmz=223695111.1540086761.4.4.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; __utma=30149280.771055282.1534754849.1540086761.1540086761.9; __utmz=30149280.1540086761.9.8.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; __utmt_t1=1; ap_v=0,6.0; Hm_lvt_1cf880de4bc3c11500482f152b3353c0=1539925272,1540086767; ct=y; Hm_lpvt_1cf880de4bc3c11500482f152b3353c0=1540086783; RT=s=1540086802548&r=https%3A%2F%2Fmovie.douban.com%2Ftyperank%3Ftype_name%3D%25E7%2588%25B1%25E6%2583%2585%26type%3D13%26interval_id%3D100%3A90%26action%3D; _pk_id.100001.4cf6=d6b12b7a6d2473eb.1536137890.4.1540086803.1539925267.; __utmb=30149280.15.8.1540086803027',
                   'll="108288"; bid=YSQV_Py1sCI; __guid=223695111.3278876595296546300.1540092744511.7078; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1540092745%2C%22https%3A%2F%2Fwww.so.com%2Fs%3Fie%3Dutf-8%26src%3Dhao_360so_a1004%26shb%3D1%26hsid%3D184bb3a5624043c3%26q%3D%25E8%25B1%2586%25E7%2593%25A3%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1088639247.1540092745.1540092745.1540092745.1; __utmb=30149280.0.10.1540092745; __utmc=30149280; __utmz=30149280.1540092745.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.272870948.1540092745.1540092745.1540092745.1; __utmb=223695111.0.10.1540092745; __utmc=223695111; __utmz=223695111.1540092745.1.1.utmcsr=so.com|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; __yadk_uid=PIL9t6ALay9qgbVqXsTBW9O5GDLcFD8J; _vwo_uuid_v2=D9B7FD000AC7C97E977887FF869B44548|1e3497f36af2a90e41d594ad6e1bb9d1; monitor_count=3; _pk_id.100001.4cf6=e3a7671613a71cb6.1540092745.1.1540092753.1540092745.',
                   'll="108288"; bid=TQ-NgpVIAGg; ap_v=0,6.0; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1540092825%2C%22https%3A%2F%2Fwww.baidu.com%2Fs%3Fie%3Dutf-8%26f%3D8%26rsv_bp%3D0%26rsv_idx%3D1%26tn%3Dbaidu%26wd%3D%25E8%25B1%2586%25E7%2593%25A3%26rsv_pq%3Da2a7bdb00001b465%26rsv_t%3D6af7tL1pz3pJpCoctHSssUGvdVjwIOrsMV8K2vVYbKU9WPMTVHQ%252BoRkjaSs%26rqlang%3Dcn%26rsv_enter%3D1%26rsv_sug3%3D5%26rsv_sug1%3D5%26rsv_sug7%3D100%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.851546008.1540092825.1540092825.1540092825.1; __utmb=30149280.0.10.1540092825; __utmc=30149280; __utmz=30149280.1540092825.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.904781343.1540092825.1540092825.1540092825.1; __utmb=223695111.0.10.1540092825; __utmc=223695111; __utmz=223695111.1540092825.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic|utmctr=%E8%B1%86%E7%93%A3; __yadk_uid=OHHXDbVYbMnbrNqwuVvDG7SxgMqOWO94; _vwo_uuid_v2=D061A77475AA2507DD6ADACECE504BE29|505865327e529145a862b8f852c48831; _pk_id.100001.4cf6=d6e9ac36b2f0a467.1540092825.1.1540092864.1540092825.',
                   'll="108288"; bid=BUkm8gD4PGk; _vwo_uuid_v2=D6BDD7BE210FA0C23843C4A835FEF43F8|a872cc55fa4d4dbc3bd4c145ee532b1d; douban-fav-remind=1; __utmz=30149280.1538908744.7.6.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ct=y; __utma=30149280.1249192018.1532233875.1539873226.1540002637.12; __utmc=30149280; __utmt=1; __utmb=30149280.1.10.1540002637; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1540002641%2C%22https%3A%2F%2Fwww.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=223695111.633013097.1532233880.1539873226.1540002641.10; __utmb=223695111.0.10.1540002641; __utmc=223695111; __utmz=223695111.1540002641.10.9.utmcsr=douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; ap_v=0,6.0; RT=nu=https%3A%2F%2Fmovie.douban.com%2Fchart&cl=1540002657077&r=https%3A%2F%2Fmovie.douban.com%2F&ul=1540002657088&hd=1540002657731; _pk_id.100001.4cf6=94053667f7ee5a99.1532233880.10.1540002701.1539873251.'
                ]
    #代理iP
    proxies = ['118.190.95.35:9001', '124.235.145.79:80', '177.71.95.6:8080', '111.7.130.101:8080', '116.62.168.236:8080', '119.28.195.93:8888', '120.77.249.46:8080', '212.90.59.163:56413', '120.131.9.254:1080', '39.137.69.7:8080']
    proxy = {'http':random.choice(proxies)}
    # proxy = get_proxyip_enable(get_proxyip())

    headers = {
        'User-Agent' : agent_list[random.randint(0, 6)],           #
        'Cookie' : cookie_list[random.randint(0, 5)]
    }

    response = requests.get(url, headers=headers, proxies=proxy)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
        return soup
    else:
        print("豆瓣请求返回码为：" + response.status_code)
        return None


''' 返回西刺快速代理IP列表，返回文件中存储的ip列表 '''
def get_proxyip():
    ip_list = []

    try:
        with open('Proxy-IP.txt', 'r', encoding='utf-8') as ipfile:
            ips = ipfile.readlines()
            for ip in ips:
                ip = ip.strip()
                ip_list.append(ip)
    finally:
        if ipfile:
            ipfile.close()
        return ip_list


''' 输入代理ip列表，返回可用的ip列表 '''
def get_proxyip_enable(proxies_list):
    available_list = []
    header = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
    }

    for ip_port in proxies_list:
        proxy = {'http' : ip_port}
        response = requests.get('http://www.baidu.com', headers=header, proxies=proxy)      # http://httpbin.org/ip
        code = response.status_code
        if code == 200:
            available_list.append(proxy)

    return available_list


''' 得到电影的初级链接，返回为字符串。包含名称、评分、评论、二级链接 '''
def get_urlcontext_as_str(url):
    str_list = []

    soup = get_url_soup_obj(url)
    str0 = soup.get_text().strip('[').strip(']')      # 得到链接字符串,去掉首尾中括号
    str1 = str0.split('},')                             # 切割字符串
    time.sleep(random.randint(3, 5))
    # print(soup.find_all('p'))

    for s in str1:                          # 拼接成字典样式的字符串
        if s[-1] != '}':
            s += '}'
        str_list.append(s)
        # print(s + '\n')
    str_list.append('\n')
    tranf_str = '\n'.join(str_list)

    return tranf_str


'''根据基本的链接拼接，返回链接列表
 例如https://movie.douban.com/j/chart/top_list?type=13&interval_id=100%3A90&action=&start=0&limit=20 '''
def tag_movie_urls(url, num):
    limit = 20
    urls = []
    pages = range(0, num//20+1)

    for i in pages:
        url_1 = url + str(i*20) + '&limit=' + str(limit)
        urls.append(url_1)

    return urls


def get_comment_text(filename, url, page):
    limit = 20
    flag = True

    try:
        with open('D:\\EveryProject\\Python\\PyCharm\\DouBan\\moves_comments\\' + filename + '.txt', 'a', encoding='utf-8') as comm_file:

            for i in range(0, page):
                start = i * 20
                time.sleep(random.randint(3, 5))
                comm_link = url + 'comments?start=' + str(start) + '&limit=' + str(limit) + '&sort=new_score&status=P'
                # print(comm_link)

                soup = get_url_soup_obj(comm_link)
                if soup != None:
                    username = soup.select('#comments > div > div.comment > h3 > span.comment-info > a')
                    theday = soup.select('#comments > div > div.comment > h3 > span.comment-info > span.comment-time')
                    comms = soup.select('#comments > div > div.comment > p > span')                         #评论
                    votes = soup.select('#comments > div > div.comment > h3 > span.comment-vote > span')    #评论觉得有用
                    #星级评价是动态加载的，未爬取

                    for uname, day, vote, comm in zip(username, theday, votes, comms):
                        comm_data = {
                            'username' : uname.get_text(),
                            'whichDay' : day.get_text().strip(),
                            'vote' : vote.get_text(),
                            'comm' : comm.get_text()                #.decode('gbk').encode('utf-8')
                        }
                        to_json = json.dumps(comm_data, ensure_ascii=False) + '\n'
                        comm_file.write(to_json)
                        print('已存储：' + to_json)

                else:
                    print("在" + time.strftime('%H:%M:%S',time.localtime(time.time())) + "又被封IP了")
                    print("当前网址为" + comm_link)
                    flag = False
                    break

    finally:
        if comm_file:
            comm_file.close()
        return flag


'''获得未看过的电影的数量，返回数值。MMP竟然是动态加载的'''
def how_many_movies(url):
    cont = requests.get(url)
    soup = BeautifulSoup(cont.text, 'lxml')
    str = soup.select('#content > div > div.article > div.option-panel > div.option-left > span:nth-of-type(1) > label > span')[0]
    print(str.get_text())


''' 存储电影的初级链接到指定txt文件 '''
def save_file(dir, cont):
    try:
        with open(dir, 'a', encoding='utf-8') as url_file:
            url_file.write(cont)
            print('存储完毕！')
    finally:
        if url_file:
            url_file.close()


''' 从指定txt文件中读取内容，返回列表 '''
def read_file(dir):
    try:
        with open(dir, 'r', encoding='utf-8') as url_file:
            return url_file.readlines()
    finally:
        if url_file:
            url_file.close()


if __name__ == '__main__':
    type = 6               # 爱情：13、科幻：17、战争：22、情色：6、
    movies_num = 51        # 要爬取多少部电影
    tag_link = 'https://movie.douban.com/j/chart/top_list?type=' + str(type) + '&interval_id=100%3A90&action=&start='
    loc_dir = 'D:/EveryProject/Python/PyCharm/DouBan/'
    file_name = 'context_src.json'
    num = 0                 #显示有多少条记录

    ''' 从本地文件解析链接访问评论 '''
    cont_list = read_file(loc_dir + file_name)
    for cont in cont_list:
        if cont != '\n':
            # num += 1
            json_src = json.loads(cont)
            # print(str(num), json_src['title'], ' ', json_src['score'], ' ', json_src['vote_count'], ' ', json_src['url'])
            if not get_comment_text(json_src['title'], json_src['url'], 11):       #获取多少页评论
                break

    ''' 以标签从豆瓣获取要爬取电影链接，存入本地 '''
    # for i in tag_movie_urls(tag_link, movies_num):
    #     print(i)
    #     url_cont = get_urlcontext_as_str(i)
    #     save_file(loc_dir + file_name, url_cont)

