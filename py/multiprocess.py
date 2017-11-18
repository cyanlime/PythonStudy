from multiprocessing import Pool
import os, time

def get_more_pages(page):
    #for page in range(start, end):
    #print '1'
    print 'Run task %s(%s)' % (page, os.getpid())
    start = time.time()
    if page==1:
        url = 'http://maoyan.com/board/4?'
    else:
        url = 'http://maoyan.com/board/4?offset=%s' % ((page-1)*10)
    #save_to_sqlite3(url, page)
    #time.sleep(2)
    end = time.time()
    print url
    print 'Task %s takes %s seconds' % (page, end-start)   

if __name__ == '__main__':
    print 'Parent process: %s' % os.getpid()
    p = Pool()
    for i in range(1, 10):
        p.apply_async(get_more_pages, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done'