import os
from watchdog.observers import Observer
from handler.event_handler import Handler

def main():
    dir_path = os.getcwd()
    print('Initialized in: ', dir_path)

    # Initialize the observer and event handler
    event_handler = Handler()
    observer = Observer()
    observer.schedule(event_handler, path=dir_path, recursive=True)

    # Start the observer
    observer.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()

if __name__ == "__main__":
    main() 
