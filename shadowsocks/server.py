import time
import sys
import thread
import server_pool
import db_transfer

#def test():
#    thread.start_new_thread(DbTransfer.thread_db, ())
#    Api.web_server()

if __name__ == '__main__':
    thread.start_new_thread(db_transfer.DbTransfer.thread_db, ())
    """
    time.sleep(2)
    server_pool.ServerPool.get_instance().new_server(3333, '2333')
    while True:
        server_pool.ServerPool.get_instance().new_server(2333, '2333')
        server_pool.ServerPool.get_instance().del_server(2333)
        time.sleep(0.01)
    """
    while True:
        time.sleep(99999)
