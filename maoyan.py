class Worker:
    def __init__(self):
        pass
    
    def get_more_pages(page):
        pass

    def get_page(url, page):
        pass

    def get_detail_imgs():
        pass

class Utils:
    def get_url(url):
        pass

    def make_dirs(path):
        pass

    def save_imgs():
        pass

    def is_img_download():
        pass



class DB:
    def __init__(self):
        pass

    def create_table():
        """
        is downloading: 0
        downloaded: 1
        """
        c.execute('''CREATE TABLE if not exists news
            (id integer primary key autoincrement,
            title text,
            link text,
            isdownloaded integer)''')

        c.execute('''CREATE TABLE if not exists images
            (id integer primary key autoincrement,
            url text,
            content text,
            path text,
            news_id integer,
            FOREIGN KEY(news_id) REFERENCES news(id))''')

        c.execute('''CREATE TABLE if not exists comments
            (id integer primary key autoincrement,
            nickname text,
            comment text,
            date integer,
            news_id integer,
            FOREIGN KEY(news_id) REFERENCES news(id))''')

        c.execute('''CREATE TABLE if not exists process
            (id integer primary key,
            pagenum integer,
            titleid integer)''')

    def save_news(title, link):
        c.execute('INSERT INTO news (title, link, isdownloaded) VALUES (?,?,?)', (title, link, 0))
        return c.fetchall()

    def news_download_completed(id):
        c.execute('UPDATE news set isdownloaded=1 where ID=id')
        return c.fetchall()

    def save_images(newsid, url, content, path):
        c.execute('INSERT INTO image (url, content, path, news_id) VALUES (?,?,?,?)', (url, content, path, news_id))
        return c.fetchall()

    def save_comments(newsid, nickname, comment, date)
        c.execute('INSERT INTO comment (headportrait, nickname, comment, date, news_id) VALUES (?,?,?,?,?)', (headportrait, nickname, comment, date, newsid))
        return c.fetchall()

    def save_process(pagenum, titleid):
        c.execute('INSERT OR REPLACE INTO process (id, pagenum, titleid) VALUES (?,?,?)', (1, pagenum, titleid))      
        return c.fetchall()

       
    def select_undownloaded_news():
        c.execute('SELECT * FROM news WHERE isdownloaded=0')
        return c.fetchall()

    def select_process(pagenum, ):
        c.execute('SELECT * FROM process WHERE id=1')
        return c.fetchall()
