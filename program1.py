   try:

        while worker.is_alive():
            yield zmq_recv_batch(socket)

    except StopIteration:
        pass

    except:
        six.reraise(*sys.exc_info())
